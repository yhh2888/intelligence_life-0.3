import random, json
from randtree import randtree
from feature_analysis import matrix_generator
import numpy as np
from pathlib import Path

class ununited_matrix_DNA:
    def __init__(self, code=None):
        self.code = code
        if self.code == None:
            self.points = [['r','d','l','u'][random.randint(0, 3)] for i in range(48)]
            self.scales = [['b', 's'][random.randint(0, 1)] for i in range(16)]
            self.ranges = [['i','n','a','x'][random.randint(0, 3)] for i in range(16)]
            self.reverse = [['0', '1'][random.randint(0, 1)] for i in range(2)]
        else :
            self.points = self.code[0:48]
            self.scales = self.code[48:64]
            self.ranges = self.code[64:80]
            self.reverse = self.code[80:]

    def mutation(self, prob=0.01):
        self.points = [['r','d','l','u'][(['r','d','l','u'].index(i)+[-1, 1][random.randint(0, 1)])%4] \
                       if random.random() < prob else i for i in self.points]
        self.scales = [['b', 's'][(['b','s'].index(i)+[-1, 1][random.randint(0, 1)])%2] \
                       if random.random() < prob else i for i in self.scales]
        self.ranges = [['i','n','a','x'][(['i','n','a','x'].index(i)+[-1, 1][random.randint(0, 1)])%4] \
                       if random.random() < prob else i for i in self.ranges]
        self.reverse = [['0','1'][(['0','1'].index(i)+[-1, 1][random.randint(0, 1)])%2] \
                       if random.random() < prob else i for i in self.reverse]


class united_matrix_DNA:
    def __init__(self, matricecodes, code = None):
        self.matricecodes = matricecodes
        self.code = code
        if self.code == None:
            self.orders = [random.randint(0, 24) for i in range(24)]
            self.unite_method = [['o','a'][random.randint(0, 1)] for i in range(23)]
            self.special = []
        else :
            self.orders = self.code[0]
            self.unite_method = self.code[1]
            self.special = self.code[2]

    def total_mutation(self, prob=0.01):
        for i in self.matricecodes:
            i.mutation(prob)

        self.orders = [random.randint(0, 24) if random.random() < prob else i for i in self.orders]
        self.unite_method = [['o','a'][(['o','a'].index(i)+[-1, 1][random.randint(0, 1)])%2] \
                            if random.random() < prob else i for i in self.unite_method]

    def special_mutation(self, mat, prob=0.2):
        addpoint = mutational(mat)
        addpoint = [min(10, max(0, i)) for i in addpoint]
        addpoint.reverse()
        if prob > random.random() and self.special != []:
            del self.special[random.randint(0, len(self.special)-1)]
        elif prob <= random.random() and len(self.special) < 20:
            while addpoint not in self.special:
                self.special.append(addpoint)
        
            
def combiner(dna):
    matrice_params = []
    for i in dna.matricecodes:

        point_fin = (5, 5)
        for j in i.points:
            add = [(1, 0), (0, 1), (-1, 0), (0, -1)][['r','d','l','u'].index(j)]
            point_fin = (point_fin[0]+add[0], point_fin[1]+add[1])

        scale_fin = 1
        for j in i.scales:
            mul = [0.9, 1.1][['b','s'].index(j)]
            scale_fin = scale_fin*mul

        ranges_fin = (0.2, 0.5)
        for j in i.ranges:
            mul = [(1.1, 1), (1, 1.1), (0.9, 1), (1, 0.9)][['i','n','a','x'].index(j)]
            ranges_fin = (ranges_fin[0]*mul[0], ranges_fin[1]*mul[1])

        if i.reverse[0] == '1' and i.reverse[1] == '1':
            rev_fin = True
        else :
            rev_fin = False

        matrice_params.append([point_fin, scale_fin, ranges_fin, rev_fin])
    return matrice_params

def matfin(dna = None, mutate = True):

    if dna == None:
        code = [random.randint(0, 24) for i in range(24)]
        mergecode = [['o','a'][random.randint(0, 1)] for i in range(23)]
        specode = []
    else :
        code = dna[0]
        mergecode = dna[1]
        specode = dna[2]
        
    randt = randtree(24)
    randt.generate_random_tree(code)
    
    if dna == None:
        b = united_matrix_DNA([ununited_matrix_DNA() for i in range(24)])
    else :
        b = united_matrix_DNA([ununited_matrix_DNA(dna[3+i]) for i in range(24)], code = [code, mergecode, specode])
        if mutate == True:
            for i in range(1):
                b.total_mutation()
    
    mat_sets = matrix_generator(combiner(b))
    edges = randt.edge
    mats = mat_sets.mats
    call = 0
    for i in randt.steps:
        edges.append(i[2])
        added = [mat_sets.plus_and(mat_sets.mats[edges.index(i[0])],
                                   mat_sets.mats[edges.index(i[1])]),
                 mat_sets.plus_or(mat_sets.mats[edges.index(i[0])],
                                  mat_sets.mats[edges.index(i[1])])] \
                                  [['a','o'].index(b.unite_method[call])]
        mats.append(added)
        
        del mats[edges.index(i[0])]
        del mats[edges.index(i[1])]
        del edges[edges.index(i[0])]
        del edges[edges.index(i[1])]
        call += 1
    
    for i in b.special:
        mats[0][i[0]][i[1]] = 1

    return mats, b

e = matfin()

with open(r'C:\Users\hyunhoyang\Desktop\IL'+'\\'+'field_data.json') as f:
        p = json.load(f)


for i in range(len(p)-1):
    p[0].extend(p[i+1])

p=p[0]

tot_points = []

for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = np.array([np.array(p[i][0]).reshape(11, 11)])
	p[i][1] = np.array(p[i][1])
	p[i] = list(p[i])

def genetest(matrix):
    tot_points = []
    crit = [i for i in range(len(matrix.flatten())) if matrix.flatten()[i] == 1]
    for k in range(len(p)):
        tot_points.append(sum([p[k][0][0].flatten()[i] for i in crit]))

    labels = [np.argmax(p[i][1]) if max(p[i][1]) != 0 else 5 for i in range(len(p))]
    labelpoints = [0,0,0,0,0]
    
    for i in range(len(labels)):
        if 0<=labels[i]<=4:
            labelpoints[labels[i]] += tot_points[i]

    return labelpoints

def fit(crit = 0.03, labelnum = None, reverse=False):
    
    er = []
    e = matfin()
    cut = 0
    
    while cut < 2:
        for i in range(1000):
            dna = [e[1].orders, e[1].unite_method, e[1].special,
                   *[e[1].matricecodes[i].points+e[1].matricecodes[i].scales+e[1].matricecodes[i].ranges+e[1].matricecodes[i].reverse for i in range(24)]]
            e = matfin(dna)
            if 7<len([0 for i in e[0][0].flatten() if i == 1])<85:
                er.append(i)
                break
        test = genetest(e[0][0])
        print(test)
        cut = 0
        if labelnum == None:
            labelnum = np.argmin(test[0:4])
        for i in test:
            if test[labelnum]/sum(test) < crit and reverse == False:
                cut += 1
            elif test[labelnum]/sum(test) > crit and reverse == True:
                cut += 1
        print(test[labelnum]/sum(test))

    return e


print("done!")

def mutational(mat, num=2.3):
    matL = []
    matx = 0
    maty = 0

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1.:
                matL.append((j, i))

    for i in matL:
        matx += i[0]
        maty += i[1]

    if matL != []:
        matx = matx/len(matL)
        maty = maty/len(matL)
    else:
        matx = 5
        maty = 5
    matmid = [matx, maty]

    pluscode = [np.random.normal()*num]*2
    mutatecode = [int(i+np.random.normal()*num) for i in matmid]

    return mutatecode

def special_mutation(dna, prob=0.1, least = 8):
    for codes in range(len(dna)):
        testmat = get_matrix(dna[codes])
        codelength = len(dna[codes])
        if prob > random.random() and len(dna[codes]) >= 8:
            del dna[codes][random.randint(0, len(dna[codes])-1)]
        else :
            while len(dna[codes]) == codelength:
                addpoint = mutational(testmat)
                if addpoint not in dna[codes]:
                    dna[codes].append(addpoint)
    return dna

def get_matrix(dna):
    mat = np.zeros(shape=(11, 11))
    for i in dna:
        x = min(10, max(0, i[0]))
        y = min(10, max(0, i[1]))
        mat[x][y] = 1
    return mat

epochs = 60

def evolution(dnamat, epochs, labelnum=None, step=1, reverse=False):
    dna = [[[i, j] for i in range(len(dnamat)) for j in range(len(dnamat[i]))  if dnamat[i][j] == 1] for i in range(30)]
    for i in range(epochs):
        print('\ngen'+str(i))
        if i > 0:
            dna = [[chosen[i][k] for k in range(len(chosen[i]))] for j in range(6) for i in range(5)]

        for j in range(step):
            dna[5:] = special_mutation(dna[5:])
        
        points = []
        for j in range(len(dna)):
            label = genetest(get_matrix(dna[j]))
            if labelnum == None:
                labelnum = np.argmin(label[0:4])
                
            if sum(label) != 0:
                points.append(label[labelnum]/sum(label))
                print(label[labelnum]/sum(label))
            else :
                points.append(50)
                
        sortpoint = list(set([i for i in points]))
        sortpoint.sort()
        
        chosen = [dna[points.index(sortpoint[i])] if reverse==False else dna[points.index(sortpoint[-i-1])] for i in range(5)]
    
    return chosen

'''
evolution(fit(crit, label)[0][0], epoch, label, step, reverse)
evolution(get_matrix(chosen[0]), epoch, label, step, reverse)
'''

def total_by_point(labelnum):
	totals = []
	for i in range(11):
		semitotal = []
		for j in range(11):
			labels = genetest(get_matrix([[i, j]]))
			semitotal.append(labels[labelnum]/sum(labels))
		totals.append(semitotal)
	return np.array(totals)

def matsort(stand, mat):
	matrix = []
	for i in mat:
		row = []
		for j in i:
			if j > stand:
                                row.append(0)
			else :
				row.append(1)
		matrix.append(row)
	return np.array(matrix)

for i in range(4):
    globals()['label'+str(i)] = total_by_point(i)


def save(chosen, type='awareness', label=None, direction = 'least'):
    if label == None:
        jsond = [[chosen[i], type, min(genetest(get_matrix(chosen[i]))[0:4])/sum(genetest(get_matrix(chosen[i]))),
                  genetest(get_matrix(chosen[i])).index(min(genetest(get_matrix(chosen[i])))[0:4]),
                  direction] for i in range(5)]
    else :
        jsond = [[chosen[i], type, genetest(get_matrix(chosen[i]))[label]/sum(genetest(get_matrix(chosen[i]))),
                  label, direction] for i in range(len(chosen))]
    if Path(r'featured_matrix\featurematrixes.json').exists():
        with open(r'featured_matrix\featurematrixes.json') as f:
            loaded = json.load(f)
            jsond = loaded+jsond
    with open(r'featured_matrix\featurematrixes.json', 'w') as f:
        json.dump(jsond, f)
