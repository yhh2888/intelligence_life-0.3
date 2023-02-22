import torch, json
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import numpy as np
import time, os, sys
from pathlib import Path
from feature_analysis import *
from torch.optim.lr_scheduler import ExponentialLR

paths = str(Path(os.getcwd()).parent)

try:
    with open(paths+'\\\\'+'field_data.json') as f:
        p = json.load(f)
except Exception:
    pass

#preprocessing data--------------------------

for i in range(len(p)-1):
    p[0].extend(p[i+1])

p = p[0]

for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(p[i][0]).reshape(11, 11)))])
	p[i][1] = torch.tensor(p[i][1])
	p[i] = list(p[i])

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
        
def featurecall(name):
    with open(os.getcwd()+'\\\\'+name+'_data.json') as f:
        flist = json.load(f)
    return flist

def feature_change(data, feature):
    goer = 0
    flist = []
    labelist = []
    for i in range(len(data)):
        if feature[goer][0] == i:
            flist.append((data[i][0], torch.tensor(feature[goer][1])))
            goer += 1
            labelist.append(data[i][1])
    return (flist, labelist)

#--------------------------------------------

p_ = DataLoader(p[0:int(len(p)//1.2)], batch_size=100)

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
test_dataloader = DataLoader(p[int(len(p)//1.2):], batch_size=100)

class NeuralNetwork(nn.Module):
    def __init__(self, layer, drop_prob = 0.1):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()

        networks = []
        self.layers = layer
        for i in range(len(self.layers)-1):
            networks.append(nn.Linear(layer[i], layer[i+1]))
            if i != len(layer)-1:
                networks.append(nn.ReLU())
                networks.append(nn.Dropout(p=drop_prob))
        
        self.stack = nn.Sequential(*networks)

    def forward(self, x):
        x = self.flatten(x)
        logits = self.stack(x)
        return logits

connect_number = 128
model = NeuralNetwork([11*11, connect_number, 128, 128, 8])

learning_rate = 0.001
batch_size = 64

def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
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
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list
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
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
scheduler = ExponentialLR(optimizer, gamma=0.9)

epochs = 1000

def test(epochs, alert=1, mod = model, trd = train_dataloader, ted = test_dataloader, optim = optimizer, scheduler=scheduler):
        times = time.time()
        ale = False
        for t in range(epochs):
            if t % alert == 0:
                print(f"Epoch {t+1}\n")
                ale = True
            losses = train_loop(trd, mod, loss_fn, optim)
            scheduler.step()
            test_loop(ted, mod, loss_fn, ale)
            if ale == True:
                print(sum(losses)/len(losses))
            ale = False
            
        print(time.time()-times)
            
print("Done!")

flist = featurecall('distances')
flistd, remain_labels = feature_change(p, flist)
model_dist = NeuralNetwork([11*11, 128, 128, 128, 2])
ted = DataLoader(flistd[int(len(flist)//1.2):], batch_size=170)
trd = DataLoader(flistd[0:int(len(flist)//1.2)], batch_size=170)
optim_dist = torch.optim.Adam(model_dist.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
sched_dist = ExponentialLR(optim_dist, gamma=0.9)
test(30, 10, model_dist, trd, ted, optim_dist, sched_dist)

flist = featurecall('distances01')
flist01 = feature_change(p, flist)[0]
model_dist01 = NeuralNetwork([11*11, 128, 128, 128, 2])
ted01 = DataLoader(flist01[int(len(flist)//1.2):], batch_size=170)
trd01 = DataLoader(flist01[0:int(len(flist)//1.2)], batch_size=170)
optim_dist01 = torch.optim.Adam(model_dist01.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
sched_dist01 = ExponentialLR(optim_dist01, gamma=0.9)
test(30, 10, model_dist01, trd01, ted01, optim_dist01, sched_dist01)

flist = featurecall('distances02')
flist02 = feature_change(p, flist)[0]
model_dist02 = NeuralNetwork([11*11, 128, 128, 128, 2])
ted02 = DataLoader(flist02[int(len(flist)//1.2):], batch_size=170)
trd02 = DataLoader(flist02[0:int(len(flist)//1.2)], batch_size=170)
optim_dist02 = torch.optim.Adam(model_dist02.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
sched_dist02 = ExponentialLR(optim_dist02, gamma=0.9)
test(30, 10, model_dist02, trd02, ted02, optim_dist02, sched_dist02)

flist = featurecall('directions')
flist2 = feature_change(p, flist)[0]
model_dir = NeuralNetwork([11*11, 128, 128, 128, 4])
optim_dir = torch.optim.Adam(model_dir.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
ted1 = DataLoader(flist2[int(len(flist)//1.2):], batch_size=170)
trd1 = DataLoader(flist2[0:int(len(flist)//1.2)], batch_size=170)

sched_dir = ExponentialLR(optim_dir, gamma=0.0)
test(40, 10, model_dir, trd1, ted1, optim_dir, sched_dir)

li68=[]
for i in range(len(flistd)):
    li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flistd[i][0])[0], model_dir(flistd[i][0])[0]))))]), remain_labels[i]))

model_fin = NeuralNetwork([6, 8, 6])
optim_fin = torch.optim.Adam(model_fin.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)


train_fin = DataLoader(li68[0:int(len(p)//1.2)], batch_size=100)
test_fin = DataLoader(li68[int(len(p)//1.2):], batch_size=100)

sched_fin = ExponentialLR(optim_fin, gamma=0.9)
test(100, 30, model_fin, train_fin, test_fin, optim_fin, sched_fin)

code = {1:0, 2:2, 3:3, 4:1, 5:2, 6:0, 7:1, 8:3}

se1 = [[p[i*11+j][1].item() for j in range(11)] for i in range(10)]
se2 = [[code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()] \
        for j in range(11)] for i in range(10)]
     
def rangetest():
    erer = []
    for i in range(len(p)):
        erer.append((torch.argmax(model_dist(p[i][0])[0]).item(), torch.argmax(model_dir(p[i][0])[0]).item(), p[i][1].item()))

    seter = set(erer)
    count = {}
    for i in seter:
        count[i] = 0
    for i in erer:
        count[i] += 1
        
    return ((2*4*6)/len(set(erer)), count)

