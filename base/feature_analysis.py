import torch, json, os, sys
import numpy as np
from pathlib import Path
from time import perf_counter
from scipy.stats import norm

sys.path.append(r'C:\Users\KDCA\Desktop\IL\geometry')
sys.path.append(r'C:\Users\hyunhoyang\Desktop\IL\geometry')
from default_functions import movepoint

if __name__ == '__main__':
    paths = str(Path(os.getcwd()).parent)

    try:
        with open(paths+'\\\\'+'field_data.json') as f:
            data = json.load(f)
        with open(r'featured_matrix\featurematrixes.json') as f:
            fm = json.load(f)
        with open(r'C:\Users\KDCA\Desktop\IL\base\featured_matrix\downmat.json') as f:
            fd = json.load(f)
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

def labeler(tensor, function, min_size=0.003, max_size=1.0, min_dist=3, middle=[5, 5], speed_print=False):
    if speed_print == True:
        timp = perf_counter()
        
    listA, listB, listC = [], [], []
    for i in range(len(tensor)):
        for j in range(len(tensor[i])):
            if max_size > tensor[i][j] > min_size:
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
            if type(i) == list or type(i) == torch.Tensor or type(i) == int:
                func_params.append(i)
            elif i in locals():
                func_params.append(locals()[i])
            elif i in globals():
                func_params.append(globals()[i])
            
            else:
                raise ValueError
            
        return func_params[0](*func_params[1:])

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

def cross_dir(position):
    if position[0]>=0 and position[1]>=0:
        return 0
    elif position[0]<0 and position[1]>=0:
        return 1
    elif position[0]<0 and position[1]<0:
        return 2
    elif position[0]>=0 and position[1]<0:
        return 3

def pure_interval(position):
    return ((position[0])**2+(position[1])**2)**0.5

def distances(dist, crit_dist=3):
    return [0 if dist >= crit_dist else 1][0]

def get_matrix(dna):
    mat = np.zeros(shape=(11, 11))
    for i in dna:
        x = min(10, max(0, i[0]))
        y = min(10, max(0, i[1]))
        if len(i) >= 3:
            toadd = i[2]
        else :
            toadd = 1
        mat[x][y] = toadd
    return mat

def matrices_change(data):
    new_data = []
    mold = get_matrix(fd)
    for i in data:
        new_data.append(i[0][0]*mold)
    return new_data

def labelchange(function, min_size=0.003, max_size=1.0, middle=[5, 5]):
    global data
    feature = []
    flist = []
    func_speed_test = 1
    for i in range(len(data)):
        if func_speed_test > 0:
            speed_test = True
            func_speed_test -= 1
        ton = labeler(data[i][0][0], function, min_size=min_size, max_size=max_size, speed_print=speed_test, middle=middle)
        if ton != None:
            flist.append([i, ton])
        speed_test = False
    return flist

def matrix_feature_(matrix, crit):
    return float(sum((matrix*crit).flatten()))
    

class matrix_generator:
    def __init__(self, mat_var : list, size=11):
        self.mat_var = mat_var
        self.mats = []
        self.unified = []
        
        for i in mat_var:
            self.mats.append(self.get_matrix(size=(size, size),
                                        point=i[0],
                                        scale=i[1],
                                        scope_value=i[2],
                                        reverse=i[3]))
    def unify(self, unify_var : list):
        self.unify_var = unify_var
        
        for i in self.unify_var:
            if i[0][0:7] == 'unified':
                first_mat = self.unified[int(i[0][7])]
            else :
                first_mat = self.mats[i[0]]

            if i[1][0:7] == 'unified':
                second_mat = self.unified[int(i[1][7])]
            else :
                second_mat = self.mats[i[1]]

            if i[2] == 'and':
                self.unified.append(self.plus_and(first_mat, second_mat))
            elif i[2] == 'or':
                self.unified.append(self.plus_or(first_mat, second_mat))
        
    def get_matrix(self,
                   size=(11, 11),
                   point=(5, 5),
                   scale=0.7,
                   scope_value=(0, 0.5),
                   reverse = False):

        matrix = np.zeros(shape=size)
        max_value = round(((size[0]**2)+(size[1]**2))**0.5, 3)
        x = np.arange(-max_value, max_value, 0.001)
        dists = norm.pdf(x, loc=0, scale=scale)

        for i in range(11):
            for j in range(11):
                distance = ((point[0]-i)**2+(point[1]-j)**2)**0.5
                if dists[int(-1+max_value*1000+round(distance*500))]>np.random.uniform(0.3, 0.3):
                    matrix[i][j] = 1

        if reverse == True:
            matrix = ((matrix-1)*-1)+0
        return matrix

    def plus_and(self, matrix1, matrix2):
        matrix = matrix1+matrix2
        for i in range(11):
            for j in range(11):
                if matrix[i][j] <= 1:
                    matrix[i][j] = 0
                elif matrix[i][j] > 1:
                    matrix[i][j] = 1
        return matrix

    def plus_or(self, matrix1, matrix2):
        matrix = matrix1+matrix2
        for i in range(11):
            for j in range(11):
                if matrix[i][j] > 1:
                    matrix[i][j] = 1
        return matrix

def aligner(standard, aligned, default=0):
    result = []
    align_num = 0
    for i in standard:
        if aligned[align_num][0] == i[0]:
            result.append([i[0], aligned[align_num][1]])
            align_num+=1

        else :
            result.append([i[0], default])

    print(len(standard), len(aligned), align_num)
    return result

def save(flist, name='features'):
    with open(paths+"\\\\"+"base\\preprocessed"+'\\\\'+name+'_data.json', 'w') as f:
        json.dump(flist, f)


'''
labelchange(['distances', 'maindist'])
labelchange(['directions', 'main'])
flist= labelchange(['matrix_feature_', 'tensor', torch.tensor(get_matrix(fm[0][0]))])

new_data = matrices_change(data)
for i in range(len(new_data)):
    new_data[i] = [[torch.Tensor.tolist(new_data[i].flatten()), data[i][0][1]]]
'''
