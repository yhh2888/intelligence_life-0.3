import torch, json, os
import numpy as np
from pathlib import Path
from time import perf_counter

paths = str(Path(os.getcwd()).parent)

try:
    with open(paths+'\\\\'+'field_data.json') as f:
        data = json.load(f)
except Exception:
    pass

#preprocessing data--------------------------

for i in range(len(data)-1):
    data[0].extend(data[i+1])

data = data[0]

for i in range(len(data)):
	data[i] = [[data[i][0][0]], data[i][0][1]]
	data[i][0] = torch.tensor([torch.Tensor.tolist((torch.tensor(data[i][0]).reshape(11, 11)))])
	data[i][1] = torch.tensor(data[i][1])
	data[i] = tuple(data[i])

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

def labeler(tensor, function, min_size=0.003, min_dist=3, middle=[5, 5], speed_print=False):
    if speed_print == True:
        timp = perf_counter()
        
    listA, listB, listC = [], [], []
    for i in range(len(tensor)):
        for j in range(len(tensor[i])):
            if tensor[i][j] > min_size:
                listA.append([j, i])
    for i in listA:
        listB.append([i[0]-middle[0], i[1]-middle[1]])
    for i in listB:
        listC.append((i[0]**2+i[1]**2)**0.5)
    if len(listB) != 0:
        main = listB[np.argmin(listC)]
        maindist = min(listC)
        
        func_params = []
        for i in function:
            if i in locals():
                func_params.append(locals()[i])
            elif i in globals():
                func_params.append(globals()[i])
            else:
                raise ValueError
            
        return func_params[0](*func_params[1:])
    
        #return [0 if maindist >= min_dist else 1][0]
        '''if abs(main[0])<=abs(main[1]) and main[1]>=0:
            return [4 if maindist >= min_dist else 5][0]
        elif abs(main[0])<=abs(main[1]) and main[1]<0:
            return [6 if maindist >= min_dist else 7][0]
        elif abs(main[0])>abs(main[1]) and main[0]>=0:
            return [0 if maindist >= min_dist else 1][0]
        elif abs(main[0])>abs(main[1]) and main[0]<0:
            return [2 if maindist >= min_dist else 3][0]'''

    if speed_print == True:
        print(perf_counter()-timp)

def directions(position):
    if abs(position[0])<=abs(position[1]) and position[1]>=0:
        return 2
    elif abs(position[0])<=abs(position[1]) and position[1]<0:
        return 3
    elif abs(position[0])>abs(position[1]) and position[0]>=0:
        return 0
    elif abs(position[0])>abs(position[1]) and position[0]<0:
        return 1

def distances(dist, crit_dist=3):
    return [0 if dist >= crit_dist else 1][0]

def labelchange(function):
    global data
    feature = []
    flist = []
    func_speed_test = 1
    for i in range(len(data)):
        if func_speed_test > 0:
            speed_test = True
            func_speed_test -= 1
        ton = labeler(data[i][0][0], function, min_size=0.01, speed_print=speed_test)
        if ton != None:
            flist.append([i, ton])
        speed_test = False
    return flist

def save(flist, name='features'):
    with open(paths+"\\\\"+"base"+'\\\\'+name+'_data.json', 'w') as f:
        json.dump(flist, f)


'''labelchange(['distances', 'maindist'])'''
