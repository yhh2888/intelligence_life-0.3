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
        self.flist = []
        self.feature_label = []
        self.remain_labels = []
        self.f_on = False
        
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

    def featurecall(self, name):
        with open(os.getcwd()+'\\\\'+name+'_data.json') as f:
            self.flist = json.load(f)
        self.f_on = True
        
    def feature_change(self, data):
        goer = 0
        
        if self.f_on == True:
            self.feature_label = []
            self.remain_labels = []
            for i in range(len(data)):
                if self.flist[goer][0] == i:
                    self.feature_label.append((data[i][0], torch.tensor(self.flist[goer][1])))
                    goer += 1
                    self.remain_labels.append(data[i][1])

    def base_set(self, name, gamma = 0.99, call = True):
        try:
            if call == True:
                self.featurecall(name)
                self.feature_change(p)
            elif call == False:
                self.flist = name
                self.feature_label = name
                
            self.ted = DataLoader(self.feature_label[int(len(self.flist)//1.2):], batch_size=170)
            self.trd = DataLoader(self.feature_label[0:int(len(self.flist)//1.2)], batch_size=170)
            self.optim = torch.optim.Adam(self.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
            self.sched = ExponentialLR(self.optim, gamma=gamma)
            
        except Exception as e:
            pass

    def roll(self, epoch, alert=10):
        reinforce(epoch, alert, self, self.trd, self.ted, self.optim, self.sched)

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

def reinforce(epochs, alert=1, mod = model, trd = train_dataloader, ted = test_dataloader, optim = optimizer, scheduler=scheduler):
        times = time.time()
        ale = False
        for t in range(epochs):
            if t % alert == 0:
                print(f"Epoch {t+1}\n")
                ale = True
            losses = train_loop(trd, mod, loss_fn, optim)
            scheduler.step()
            test_loop(ted, mod, loss_fn, ale)
            if ale == True and len(losses) != 0:
                print(sum(losses)/len(losses))
            elif ale == True and len(losses) == 0:
                print(sum(losses))
            ale = False

        print(time.time()-times)
            
print("Done!")

'''
#other data uses
data =[(torch.tensor([[float(i//10), float(i%10)]]),
                      torch.tensor(random.randint(0, 1))) for i in range(50)]
                      
new = NeuralNetwork([len(data[0][0][0]), 2, 2])
new.base_set(data, call=False)
new.roll(15)
'''

model_dist = NeuralNetwork([11*11, 32, 32, 2])
model_dist.base_set('distances')
model_dist.roll(30, 10)

model_dist01 = NeuralNetwork([11*11, 32, 32, 2])
model_dist01.base_set('distances01')
model_dist01.roll(30, 10)

model_dist02 = NeuralNetwork([11*11, 32, 32, 2])
model_dist02.base_set('distances02')
model_dist02.roll(30, 10)

model_dir = NeuralNetwork([11*11, 32, 32, 4])
model_dir.base_set('directions')
model_dir.roll(50, 10)

li68=[]
for i in range(len(model_dist.feature_label)):
    li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(model_dist.feature_label[i][0])[0],
                                                               model_dir(model_dist.feature_label[i][0])[0],
                                                               torch.tensor([0 if model_dist.remain_labels[i].item() != 5 else 1])))))]),
                 model_dist.remain_labels[i]))

model_fin = NeuralNetwork([len(li68[0][0][0]), 15, 15, 6])
model_fin.base_set(li68, call = False)
model_fin.roll(100, 30)

code = {1:0, 2:2, 3:3, 4:1, 5:2, 6:0, 7:1, 8:3}

se1 = [[p[i*11+j][1].item() for j in range(11)] for i in range(10)]
se2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(10)]
     
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

