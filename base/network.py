import torch, json, random
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
from torch.optim.lr_scheduler import ExponentialLR
import numpy as np
import time, os, sys
from pathlib import Path
from randtree import randtree

sys.path.append(r'C:\Users\KDCA\Desktop\IL\base')
sys.path.append(r'C:\Users\hyunhoyang\Desktop\IL\base')

from feature_analysis import *

train_dataloader = []
test_dataloader = []

##
class NeuralNetwork(nn.Module):
    def __init__(self, input_len, gencode = [], cellout=5, node_num=5, neural_line_prob=0.2, drop_prob =0.1, rnn=False):

        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()

        networks = []
        self.flist = []
        self.feature_label = []
        self.remain_labels = []
        self.f_on = False
        self.rnntrue = [1 if rnn==True else 0][0]
        if gencode == []:
            self.gencode = randtree(node_num).generate_random_tree(prob = neural_line_prob)
        else :
            self.gencode = gencode

        self.cellout = cellout

        
        if input_len > 1:

            '''if rnn == True:
                self.rnn = nn.RNN(layer[0], layer[1])
                networks.append(nn.ReLU())
                networks.append(nn.Dropout(p=drop_prob))

            for i in range(self.rnntrue, len(layer)-1):
                networks.append(nn.Linear(layer[i], layer[i+1]))
                if i != len(layer)-1:
                    networks.append(nn.ReLU())
                    networks.append(nn.Dropout(p=drop_prob))'''
            self.start = nn.Linear(input_len, cellout*node_num)
            
            for i in self.gencode:
                networks.append(nn.Linear(cellout*len(i[:-1]), cellout))
            
            self.stack = nn.ModuleList(networks)

            '''self.halfed1 = nn.Linear(int(layer[-3]/2), int(layer[-2]/2))
            self.halfed1_1 = nn.Linear(int(layer[-2]/2), int(layer[-2]/2))
            self.halfed1_2 = nn.Linear(int(layer[-2]/2), int(layer[-2]/2))
            self.halfed1_3 = nn.Linear(int(layer[-2]/2), int(layer[-2]/2))

            self.halfed2 = nn.Linear(int(layer[-3]/2), int(layer[-2]/2))

            self.cated = nn.Linear(layer[-2], layer[-1])'''
            
            if rnn == True:
                self.rnn = nn.RNN(layer[-2], layer[-1])

            
            
    def forward(self, X):

        '''if self.rnntrue == 1:
            rnn_out, hidden = self.rnn(X)
            X = torch.squeeze(rnn_out, dim=1)
        else :
            X = self.flatten(X)
            
        processed = self.stack(X)'''

        X = self.flatten(X)
        
        processed = self.start(X)

        self.celldata = list(torch.split(processed, self.cellout, dim=-1))
        
        for i in range(len(self.gencode)):
            toinput = torch.cat(([self.celldata[j] for j in self.gencode[i][:-1]]), dim=-1)
            processed = self.stack[i](toinput)
            self.celldata.append(self.stack[i](toinput))
        
        if self.rnntrue == 1:
            rnn_out, hidden = self.rnn(processed.unsqueeze(1))
            processed = torch.squeeze(rnn_out, dim=1)

        '''halfed1, halfed2 = torch.split(processed, int(processed.shape[1]/2), dim=-1)
        halfed1 = self.halfed1(halfed1)
        halfed1 = self.halfed1_1(halfed1)
        halfed1 = self.halfed1_2(halfed1)
        halfed1 = self.halfed1_3(halfed1)
        halfed2 = self.halfed2(halfed2)

        cated = torch.cat((halfed1, halfed2), dim=-1)
        cated = self.cated(cated)'''
        
        
        return processed

    def featurecall(self, name):
        with open(os.getcwd()+'\\preprocessed\\'+name+'_data.json') as f:
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

    def roll(self, epoch, alert=10, first=0, last=18000):
        reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)

model = NeuralNetwork(11*11)

learning_rate = 0.001
batch_size = 64

def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
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

    test_loss /= max(1, num_batches)
    correct /= max(1, size)
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
            if t % alert == alert-1:
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

'''model_dist01 = NeuralNetwork([11*11, 32, 32, 2])
model_dist01.base_set('distances01')
model_dist01.roll(30, 10)
model_dist02 = NeuralNetwork([11*11, 32, 32, 2])
model_dist02.base_set('distances02')
model_dist02.roll(30, 10)'''

def structure_set(data, reshape=True):
        
    for i in range(len(data)):
        data[i] = [[data[i][0][0]], data[i][0][1]]
        if reshape==True:
            data[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(data[i][0]).reshape(11, 11)))])
        elif reshape == False:
            data[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(data[i][0])))])
        else :
            raise ValueError
        data[i][1] = torch.tensor(data[i][1])
        data[i] = list(data[i])

    for i in range(len(data)):
        if max(data[i][1])!=0:
            data[i] = (data[i][0], np.argmax(data[i][1]))
        else:
            data[i] = (data[i][0], torch.tensor(5))

    setter = 0

    for j in range(len(data)):
        disc = False
        j -= setter
        for i in data[j][0][0].tolist():
            if len(set(i)) != 1:
                disc = True
        if disc == False:
            del data[j]
            setter += 1
                
    return data

if __name__ == '__main__':
    paths = str(Path(os.getcwd()).parent)

    try:
        with open(paths+r'\base\preprocessed\mul_downmat.json') as f:
            mdm = json.load(f)
        with open(paths+'\\\\'+'field_data.json') as f:
            p = json.load(f)
            
        for i in range(len(p)-1):
            p[0].extend(p[i+1])

        p = p[0]
        
    except Exception:
        pass

    mdm = structure_set(mdm)
    p = structure_set(p)
    
    p_ = DataLoader(p[0:int(len(p)//1.2)], batch_size=100)

    torch.set_num_threads(2)



    train_dataloader = p_
    test_dataloader = DataLoader(p[int(len(p)//1.2):], batch_size=100)

    model_dist = NeuralNetwork(121)
    model_dist.base_set('distances')

    datakinds = ['distances', 'directions', 'distances0.6', 'directions0.6', 'interval0.3', 'interval0.6', 
                 'maf_3least', 'maf_1least', 'maf_2least', 'maf_0least',
                 'maf_1most', 'maf_3most',
                 'maf_0leastElite', 'maf_1leastElite', 'maf_2leastElite', 'maf_3leastElite',
                 'maf_0leastRequire', 'maf_1leastRequire', 'maf_2leastRequire', 'maf_3leastRequire',
                 'crossed_directions']
    
    datakinds = ['distances0.15', 'directions0.15', 'interval0.15', 'crossed_directions',
                 'boundary01,05', 'boundary01,15', 'boundary03,15', 
                 'maf_3least', 'maf_1least', 'maf_1most', 'maf_3most', 'maf_1leastRequire', 'maf_3leastRequire']

    longkinds = []
    
    for i in datakinds:
        globals()['models_'+i] = NeuralNetwork(1)
        globals()['models_'+i].base_set(i)

    for i in longkinds:
        globals()['models_'+i] = NeuralNetwork(1)
        globals()['models_'+i].base_set(i)

    li68=[] # 전~현 거리, 전~현 방향, 전~현 움직임 여부, 전~현 행렬 특징, 전 움직임, 전 행렬
    for i in range(len(model_dist.feature_label)):
        li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((*[torch.tensor([0 if model_dist.remain_labels[i-j].item() != 5 else 1]) for j in range(3)],
                                                                   *[torch.tensor([globals()['models_'+j].feature_label[i-k][1]]) for j in datakinds for k in range(3)],
                                                                   *[globals()['models_'+j].feature_label[i-k][1] if type(torch.Tensor.tolist(globals()['models_'+j].feature_label[i-k][1])) == list \
                                                                   else torch.tensor([0, 0]) for j in longkinds for k in range(3)],
                                                                   *[torch.tensor([0]) if i-1-j < 3 else torch.tensor([model_dist.remain_labels[i-1-j]]) for j in range(3)],
                                                                   *[model_dist.feature_label[i-j][0][0].flatten() for j in range(3)]
                                                                   ))
                                                        ))
                                   ]),
                     model_dist.remain_labels[i]
                     ))
        
    model_fin = NeuralNetwork(len(li68[0][0][0]), neural_line_prob=0.5)
    model_fin.base_set(li68, call = False)
    model_fin.roll(50, 10)

    code = {1:0, 2:2, 3:3, 4:1, 5:2, 6:0, 7:1, 8:3}

    set1 = [[model_fin.feature_label[i*11+j][1].item() for j in range(11)] for i in range(-1000, -2)]
    set2 = [[torch.argmax(model_fin(torch.tensor([torch.Tensor.tolist(li68[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]

    trues = 0
    for i in (np.array(set1)==np.array(set2)).flatten():
        if i == True:
            trues += 1

    print('real_test:', trues/(1000*11))

'''
params = []
for i in model_fin.parameters():
    params.append(i)
for i in range(len(params)):
    params[i]=torch.Tensor.tolist(params[i][0:])
             
with open('modelparam_data.json', 'w') as f:
    json.dump(params, f)
'''
