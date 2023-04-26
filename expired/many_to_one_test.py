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

past_tensors = []   
for i in range(3, len(tensors)):
    past_tensors.append((torch.tensor([torch.cat(([tensors[i-j][0][k][0:] if len(tensors[i-j][0]) >= k+1 else torch.tensor([-150, -150]) for j in range(3)])).tolist() \
                                       for k in range(max([len(i[0]) for i in tensors[i-2:i+1]]))]), tensors[i][1]))

embedding = nn.Embedding(num_embeddings = 90000, embedding_dim = 2, padding_idx=1)
em_tensors = []
for i in range(len(tensors)):
  tens = []
  for j in range(len(tensors[i][0])):
    tens.append(embedding.weight[int((tensors[i][0][j][0].item()+150)*300+tensors[i][0][j][1].item()+150)].tolist())
  em_tensors.append(torch.tensor(tens).unsqueeze(0))

data = []
for i in range(len(em_tensors)):
    data.append(em_tensors[i][0])
    
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
num_epochs = 10000
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
    
