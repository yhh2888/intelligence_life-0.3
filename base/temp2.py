import torch, json
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import numpy as np
import time

with open(r'C:\Users\hyunhoyang\Desktop\Intelligence Life\field_data.json') as f:
        p = json.load(f)

#preprocessing data

for i in range(len(p)-1):
    p[0].extend(p[i+1])

p = p[0]

for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(p[i][0]).reshape(11, 11)))])
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])

for i in range(len(p)):
        if max(p[i][1])!=0:
                p[i] = (p[i][0], np.argmax(p[i][1]))
        else:
                p[i] = (p[i][0], torch.tensor(5))

setter = 0

for j in range(len(p)):
    disc = False
    j -= setter
    for i in p[j][0][0].tolist():
        if len(set(i)) != 1:
               disc = True
    if disc == False:
        del p[j]
        setter += 1

#--------------------------------------------

p_ = DataLoader(p, batch_size=350)

torch.set_num_threads(2)

'''training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)'''

train_dataloader = p_
test_dataloader = DataLoader(p, batch_size=350)

class NeuralNetwork(nn.Module):
    def __init__(self, layer):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()

        networks = []
        self.layers = layer
        for i in range(len(self.layers)-1):
            networks.append(nn.Linear(layer[i], layer[i+1]))
            if i != len(layer)-1:
                networks.append(nn.ReLU())
        
        self.linear_relu_stack = nn.Sequential(*networks)

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork([11*11, 256, 128, 128, 6])

learning_rate = 0.001
batch_size = 64

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 100 == 0 and batch != 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn, alert=False):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    if alert == True:
        print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=0,
                             amsgrad=True)

epochs = 1000


def test(epochs, alert=1):
        times = time.time()
        ale = False
        for t in range(epochs):
            if t % alert == 0:
                print(f"Epoch {t+1}\n")
                ale = True
            train_loop(train_dataloader, model, loss_fn, optimizer)
            test_loop(test_dataloader, model, loss_fn, ale)
            ale = False
        print(time.time()-times)
            
print("Done!")


def primecall():
	global train_dataloader, test_dataloader, model, data, optimizer
	with open('tensored_stockdata.json') as f:
		data = json.load(f)

	main_digit = len(str(data[0][0][0]))
	classify_count = 2
	
	for i in range(len(data)):
		data[i] = torch.tensor(data[i])
		
	del data[2000:]
	for i in range(len(data)-1):
		data[i] = [data[i], int(min(torch.tensor(max(0, (data[i][3][24]-(sum(data[i+1].T[0:5])/5)[0])//20+classify_count/2)).tolist(), classify_count))]
		
	del data[1999]
	for i in range(len(data)):
		data[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(data[i][0], dtype=torch.float32).reshape(5, 100)))])
		data[i][0][0][0:4] = (data[i][0][0][0:4]-min(data[i][0][0][2]))/(10**main_digit)
		data[i][0][0][4] = (data[i][0][0][4]/50000)**0.7*10
		
	model = NeuralNetwork([500, 1024, 128, classify_count+1])
	train_dataloader = DataLoader(data[0:int(len(data)//1.2)], batch_size=1000)
	test_dataloader = DataLoader(data[int(len(data)//1.2):], batch_size=1000)
                                     
	optimizer = torch.optim.SGD(model.parameters(), lr=0.1, nesterov=False, momentum=0.01)
                    
