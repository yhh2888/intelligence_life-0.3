import torch, random
import torch.nn as nn
import torch.optim as optim

num_samples = 1000
max_seq_length = 50
num_classes = 5

data = []
for i in range(num_samples):
    seq_length = torch.randint(1, max_seq_length, size=(1,))
    seq = torch.randn(seq_length, max_seq_length)
    data.append(seq)

data_padded = nn.utils.rnn.pad_sequence(data, batch_first=True)
    
labels = []
lab = []
c= [0]*4
for j in range(len(data)):
    for i in range(len(data[j])):
        lab.append(sum(data[j][i][0:13]))
        lab.append(sum(data[j][i][13:25]))
        lab.append(sum(data[j][i][25:38]))
        lab.append(sum(data[j][i][38:50]))
        c[torch.argmax(torch.tensor(lab)).item()] += 1
        lab = []
    labels.append(torch.argmax(torch.tensor(c)).item())
    c = [0]*4

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
num_epochs = 100
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
    
