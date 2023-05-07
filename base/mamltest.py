import torch
import torch.nn.functional as F
from torch import nn, optim
import sys, json

sys.path.append(r'C:\Users\hyunhoyang\Desktop\IL\base')
import network

network.paths = r'C:\Users\hyunhoyang\Desktop\IL'

mod, tensors = network.savingmodel()

class MAML(nn.Module):
    def __init__(self, input_size, output_size, num_inner_updates=1):
        super(MAML, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.num_inner_updates = num_inner_updates
        
        self.weights = nn.Parameter(torch.Tensor(output_size, input_size))
        nn.init.xavier_uniform_(self.weights)
        
        self.loss_fn = nn.CrossEntropyLoss()
        
    def forward(self, x):
        logits = F.linear(x, self.weights)
        return logits
    
    def inner_loop(self, x, y, lr=0.01):
        weights = self.weights
        for i in range(self.num_inner_updates):
            logits = self.forward(x)
            loss = self.loss_fn(logits, y)
            gradients = torch.autograd.grad(loss, self.parameters(), create_graph=True)
            # 새로운 weight 계산
            weights = weights - lr * gradients[0]
        self.weights = nn.Parameter(weights)
            
    def meta_loss(self, x, y, x_val, y_val):
        self.inner_loop(x, y)
        logits = self.forward(x_val)
        loss = self.loss_fn(logits, y_val)
        return loss

x_train = torch.tensor([i[0].tolist()[0] for i in mod.trd.dataset[:2000]])
y_train = torch.tensor([i[1].tolist() for i in mod.trd.dataset[:2000]])
x_val = torch.tensor([i[0].tolist()[0] for i in mod.trd.dataset[2000:]])
y_val = torch.tensor([i[1].tolist() for i in mod.trd.dataset[2000:]])

model = MAML(100, 6)
optimizer = optim.Adam(model.parameters(), lr=0.01)

train_accuracy = []
val_accuracy = []

for step in range(100000):
    optimizer.zero_grad()
    loss = model.meta_loss(x_train, y_train, x_val, y_val)
    loss.backward()
    optimizer.step()
    
    if step % 1000 == 0:
        train_accuracy = []
        val_accuracy = []

        logits = model.forward(x_train)
        accuracy = torch.mean((torch.argmax(logits, axis=1) == y_train).float())
        train_accuracy.append(accuracy)
        
        logits = model.forward(x_val)
        accuracy = torch.mean((torch.argmax(logits, axis=1) == y_val).float())
        val_accuracy.append(accuracy)
        print("Step: {}, Train Accuracy: {:.2f}%, Validation Accuracy: {:.2f}%".format(step, accuracy * 100, train_accuracy[-1] * 100))
