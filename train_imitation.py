import json
import math
import os
import random

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


ACTION_NAMES = ('right', 'down', 'left', 'up', 'stop')
INPUT_SIZE = 121
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imitation_data.jsonl')
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imitation_policy.pt')


class ImitationPolicy(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(INPUT_SIZE, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, len(ACTION_NAMES)),
        )

    def forward(self, observation):
        return self.layers(observation.reshape(-1, INPUT_SIZE))

    def predict(self, observation):
        with torch.no_grad():
            inputs = torch.as_tensor(observation, dtype=torch.float32).reshape(1, INPUT_SIZE)
            action_index = int(self(inputs).argmax(dim=1).item())
        return ACTION_NAMES[action_index]


def _read_dataset(path):
    observations = []
    labels = []
    action_indices = {action: index for index, action in enumerate(ACTION_NAMES)}

    with open(path, encoding='utf-8') as dataset_file:
        for line_number, line in enumerate(dataset_file, 1):
            sample = json.loads(line)
            observation = sample.get('observation')
            action = sample.get('action')
            if not isinstance(observation, list) or len(observation) != INPUT_SIZE:
                raise ValueError(
                    '{}:{}: observation must contain {} values'.format(path, line_number, INPUT_SIZE)
                )
            if action not in action_indices:
                raise ValueError(
                    '{}:{}: unknown action {!r}'.format(path, line_number, action)
                )
            if any(not isinstance(value, (int, float)) or not math.isfinite(value)
                   for value in observation):
                raise ValueError(
                    '{}:{}: observation values must be finite numbers'.format(path, line_number)
                )
            observations.append(observation)
            labels.append(action_indices[action])

    if not observations:
        raise ValueError('No training samples found in {}'.format(path))
    missing_actions = [
        action for index, action in enumerate(ACTION_NAMES)
        if index not in labels
    ]
    if missing_actions:
        raise ValueError('Dataset is missing action labels: {}'.format(', '.join(missing_actions)))

    inputs = torch.tensor(observations, dtype=torch.float32)
    targets = torch.tensor(labels, dtype=torch.long)
    return inputs, targets


def _split_indices(inputs, targets, validation_fraction, seed):
    states = {}
    for sample_index, observation in enumerate(inputs.tolist()):
        states.setdefault(tuple(observation), []).append(sample_index)

    groups = list(states.values())
    validation_group_count = max(1, round(len(groups) * validation_fraction))
    expected_actions = set(range(len(ACTION_NAMES)))
    for seed_offset in range(100):
        shuffled_groups = groups[:]
        random.Random(seed + seed_offset).shuffle(shuffled_groups)
        validation_indices = [
            index for group in shuffled_groups[:validation_group_count] for index in group
        ]
        validation_set = set(validation_indices)
        training_indices = [
            index for index in range(len(targets)) if index not in validation_set
        ]
        training_actions = set(targets[training_indices].tolist())
        validation_actions = set(targets[validation_indices].tolist())
        if training_actions == expected_actions and validation_actions == expected_actions:
            return training_indices, validation_indices

    raise ValueError('Could not split unique observations while keeping every action in both sets')


def _evaluate(model, inputs, targets, indices, criterion):
    model.eval()
    with torch.no_grad():
        logits = model(inputs[indices])
        loss = criterion(logits, targets[indices]).item()
        predictions = logits.argmax(dim=1)
        accuracy = (predictions == targets[indices]).float().mean().item()
        per_action_accuracy = {}
        for action_index, action in enumerate(ACTION_NAMES):
            action_mask = targets[indices] == action_index
            if action_mask.any():
                per_action_accuracy[action] = (
                    (predictions[action_mask] == targets[indices][action_mask])
                    .float().mean().item()
                )
            else:
                per_action_accuracy[action] = None
    return loss, accuracy, per_action_accuracy


def train_imitation_model(
    data_path=DATA_PATH,
    model_path=MODEL_PATH,
    epochs=60,
    batch_size=128,
    learning_rate=0.001,
    validation_fraction=0.2,
    seed=42,
):
    if not 0 < validation_fraction < 1:
        raise ValueError('validation_fraction must be between 0 and 1')
    if epochs < 1 or batch_size < 1:
        raise ValueError('epochs and batch_size must be positive')

    torch.manual_seed(seed)
    inputs, targets = _read_dataset(data_path)
    training_indices, validation_indices = _split_indices(
        inputs, targets, validation_fraction, seed
    )
    train_inputs = inputs[training_indices]
    train_targets = targets[training_indices]
    train_counts = torch.bincount(train_targets, minlength=len(ACTION_NAMES)).float()
    class_weights = train_counts.sum() / (len(ACTION_NAMES) * train_counts)
    class_weights /= class_weights.mean()

    training_data = TensorDataset(train_inputs, train_targets)
    training_loader = DataLoader(
        training_data, batch_size=batch_size, shuffle=True,
        generator=torch.Generator().manual_seed(seed),
    )

    model = ImitationPolicy()
    criterion = nn.CrossEntropyLoss(weight=class_weights)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    best_validation_loss = float('inf')
    best_macro_accuracy = -1.0
    best_state = None
    epochs_without_improvement = 0
    patience = 10

    for epoch in range(epochs):
        model.train()
        for batch_inputs, batch_targets in training_loader:
            optimizer.zero_grad()
            loss = criterion(model(batch_inputs), batch_targets)
            loss.backward()
            optimizer.step()

        validation_loss, _, per_action_accuracy = _evaluate(
            model, inputs, targets, validation_indices, criterion
        )
        macro_accuracy = sum(
            accuracy for accuracy in per_action_accuracy.values()
            if accuracy is not None
        ) / len(ACTION_NAMES)
        if (macro_accuracy > best_macro_accuracy or
                (macro_accuracy == best_macro_accuracy and validation_loss < best_validation_loss)):
            best_macro_accuracy = macro_accuracy
            best_validation_loss = validation_loss
            best_state = {
                name: tensor.detach().clone()
                for name, tensor in model.state_dict().items()
            }
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= patience:
                break

    model.load_state_dict(best_state)
    validation_loss, validation_accuracy, per_action_accuracy = _evaluate(
        model, inputs, targets, validation_indices, criterion
    )
    os.makedirs(os.path.dirname(os.path.abspath(model_path)), exist_ok=True)
    torch.save({
        'input_size': INPUT_SIZE,
        'actions': ACTION_NAMES,
        'state_dict': model.state_dict(),
    }, model_path)

    print('Training samples: {}; validation samples: {}'.format(
        len(training_indices), len(validation_indices)
    ))
    print('Validation loss: {:.4f}; accuracy: {:.1%}'.format(
        validation_loss, validation_accuracy
    ))
    print('Validation macro accuracy: {:.1%}'.format(best_macro_accuracy))
    print('Validation accuracy by action: {}'.format({
        action: None if accuracy is None else '{:.1%}'.format(accuracy)
        for action, accuracy in per_action_accuracy.items()
    }))
    print('Saved model to {}'.format(os.path.abspath(model_path)))
    return model


def load_imitation_model(model_path=MODEL_PATH):
    checkpoint = torch.load(model_path, map_location='cpu', weights_only=True)
    if checkpoint.get('input_size') != INPUT_SIZE:
        raise ValueError('Checkpoint input size does not match this policy')
    if tuple(checkpoint.get('actions', ())) != ACTION_NAMES:
        raise ValueError('Checkpoint action order does not match this policy')
    model = ImitationPolicy()
    model.load_state_dict(checkpoint['state_dict'])
    model.eval()
    return model


if __name__ == '__main__':
    train_imitation_model()
