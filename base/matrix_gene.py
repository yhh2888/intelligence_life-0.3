import random
from randtree import randtree
from feature_analysis import matrix_generator

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
            self.ranges = self.code[48:80]
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
        else :
            self.orders = self.code[0]
            self.unite_method = self.code[1]

        def total_mutation(self, prob=0.01):
            for i in self.matricecodes:
                i.mutation()

            self.orders = [random.randint(0, 24) if random.random() < prob else i for i in self.orders]
            self.unite_method = [['o','a'][(['o','a'].index(i)+[-1, 1][random.randint(0, 1)])%2] \
                       if random.random() < prob else i for i in self.unite_method]
            
def combiner(dna):
    matrice_params = []
    for i in dna.matricecodes:

        point_fin = (5, 5)
        for j in i.points:
            add = [(1, 0), (0, 1), (-1, 0), (0, -1)][['r','d','l','u'].index(j)]
            point_fin = (point_fin[0]+add[0], point_fin[1]+add[1])

        scale_fin = 0.5
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
    for i in dna.code:
        pass
