from neural_network_test import *
from Genetic_Algorithm import *
import numpy as np

class Evolution:
    def __init__(self, amount=40, species = 'random', sight=11):
        if species == 'random':
            self.genlist = []
            for i in range(amount):
                layervalue=[np.random.randint(-1, 3) for i in range(2)]+[np.random.randint(-3, 3) for i in range(6)]+[np.random.randint(-3, 1) for i in range(2)]
                while len(layer_create(sight, layervalue, length=sight)) <= 3:
                    layervalue=[np.random.randint(-1, 3) for i in range(2)]+[np.random.randint(-3, 3) for i in range(6)]+[np.random.randint(-3, 1) for i in range(2)]
                genetics = [layervalue,
                            activation_code_create(4, lenlim=11), 11]
                params = param_renew(layer_create(genetics[2], genetics[0], length=genetics[2]))
                genetics.append(params[0])
                genetics.append(params[1])
                genetics.append([])
                self.genlist.append(genetics)
        elif type(species) == list:
            self.genlist = species

    def test(self, next_gen, freq):
        self.pointlist = []
        for i in self.genlist:
            self.pointlist.append(Gene(i[0], i[1], i[2], params = i[3], const = i[4], mrec=i[5]).genetest(freq))
        self.news = []
        pointlist_ = []
        genlist_ = []
        for i in range(len(self.pointlist)):
            pointlist_.append(self.pointlist[i])
            genlist_.append(self.genlist[i])
        for i in range(next_gen):
            app = genlist_[np.argmin(pointlist_)]
            if len(layer_create(app[2], app[0], length=app[2])) > 3:
                self.news.append(app)
                del genlist_[np.argmin(pointlist_)]
                del pointlist_[np.argmin(pointlist_)]
            else :
                i -= 1
        print(self.pointlist)

    def next_generation(self, sons):
        new_gen = []
        for i in range(len(self.news)):
            new_gen.append(self.news[i])
        for j in range(sons):
            duple = []
            for i in range(len(self.news)):
                duple.append(self.news[i])
            for i in duple:
                thing = Gene(i[0], i[1], i[2], params = i[3], const = i[4], mrec=i[5])
                thing.mutation_roulette()
                thing.length_adjust()
                some = [thing.curve, thing.code, thing.lenlim, thing.params, thing.const, thing.mutation_record]
                '''print(thing.params,  thing.const)'''
                new_gen.append(some)
        return new_gen


def ev_rep(b):
	a = Evolution(species=b)
	a.test(10, 30)
	c = a.next_generation(3)
	return c

def main():
    run = True
    fail = True
    b = []
    save = []
    kindsets = []
    while run == True:
        if len(save) > 40:
            b = save
            kindsets.append(save)
            save = []
            fail = False
        if len(kindsets) > 10:
            b = kindsets[random.randint(0, 9)]
            for i in range(3):
                del kindsets[random.randint(0, 6)]
        if fail == True or len(b) == 0:
            a = Evolution()
            a.test(5, 30)
            for i in range(len(a.pointlist)):
                if a.pointlist[i] < 200:
                    save.append(a.genlist[i])
                if a.pointlist[i] != 750.0:
                    fail = False
                    b = a.next_generation(10)
                    if len(b) == 0:
                        print('empty')
                if a.pointlist[i] < 50:
                    em = 0
                    for j in range(5):
                        if a.pointlist[j] > 150:
                            em += 1
                    if em > 1:
                        break
                    run = False
                    return a.genlist[i], i
                    break
        elif fail == False:
            a = Evolution(species=b)
            a.test(5, 30)
            fail = True
            for i in range(len(a.pointlist)):
                if a.pointlist[i] < 200:
                    save.append(a.genlist[i])
                if a.pointlist[i] != 750.0:
                    fail = False
                    b = a.next_generation(10)
                    if len(b) == 0:
                        print('empty')
                if a.pointlist[i] < 50:
                    em = 0
                    for j in range(5):
                        if a.pointlist[j] > 150:
                            em += 1
                    if em > 1:
                        break
                    run = False
                    return a.genlist[i], i
                    break
