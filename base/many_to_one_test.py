import torch, random, os
import torch.nn as nn
import torch.optim as optim
from pathlib import Path
import json

num_samples = 1000
max_seq_length = 2
num_classes = 4

paths = str(Path(os.getcwd()).parent)
tensors = []
                          
with open(paths+'\\\\'+'mobs_data.json') as f:
    t = json.load(f)

for i in t:
    out = False
    if torch.tensor(i[0][0]).size()[0] != 0 and i[0][1] != [0, 0, 0, 0, 0]:
        for j in i[0][0]:
            for k in j:
                 if k<-150 or k>149:
                     out = True
        if out == True:
            continue
        tensors.append((torch.tensor(i[0][0], dtype=torch.float32), [torch.argmax(torch.tensor(i[0][1])) if max(i[0][1]) != 0 else torch.tensor(5)][0]))

data = []
for i in range(len(tensors)):
    data.append(tensors[i][0])
    
data_padded = nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=-150)

labels = []
for i in range(len(tensors)):
	labels.append(tensors[i][1])

labels = torch.tensor(labels)

class Classifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(Classifier, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])
        return out

input_size = max_seq_length
hidden_size = 128
num_epochs = 1000
batch_size = 10
learning_rate = 0.001

model = Classifier(input_size, hidden_size, num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for i in range(0, num_samples, batch_size):
        inputs = data_padded[i:i+batch_size]
        label = labels[i:i+batch_size]
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, label)
        loss.backward()
        optimizer.step()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
    
