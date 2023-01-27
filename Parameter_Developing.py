import numpy as np
import time

from Hitting_Frame import *
from base.bp_temp import *

class Evolve:
    def __init__(self, amount=10, prev_scoresum = 0, nn=None):
        self.nn = nn
        self.prev_scoresum = prev_scoresum
        self.reevolve = False
        self.paramgens = [i for i in range(amount)]
        self.circumstances = Game(50, 50)

    def test(self, next_gen, view_lock = False):
        self.scorelist = []
        for i in range(len(self.paramgens)):
            score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
            self.scorelist.append(score)
            self.circumstances = Game(50, 50)
            
        scorelist_sum = 0
        
        for i in self.scorelist:
            scorelist_sum += i
        self.scoresum = scorelist_sum/len(self.scorelist)
        print(self.scorelist, scorelist_sum/len(self.scorelist))
        
        self.news = []
        for i in range(next_gen):
            self.news.append(self.paramgens[np.argmax(self.scorelist)])
            del self.paramgens[np.argmax(self.scorelist)]
            del self.scorelist[np.argmax(self.scorelist)]

    '''def next_generation(self, sons):
        new_gen = []
        for i in range(len(self.news)):
            new_gen.append(self.news[i].params)
        for j in range(sons):
            duple = []
            for i in range(len(self.news)):
                duple.append(self.news[i])
            for i in duple:
                i.m_params()
                some = i.params
                new_gen.append(some)
        return new_gen'''


def rep_test(rep, view_lock = False):
    
    try:
        with open('field_data.json') as f:
            received_data = json.load(f)
    except Exception as e:
        received_data = []
        
    nn = NeuralNetwork(layer=[11**2, 15, 15, 15, 5])
    nn.load('test')
    
    a = Evolve(nn=nn)
    
    for i in [i for i in range(rep)]:
        
        t = time.time()
        
        a.test(10, view_lock = view_lock)
        received_data.append(nn.received_data)
        nn.received_data = []
            
        print(time.time()-t)

        with open('field_data.json', 'w') as f:
            json.dump(received_data, f, indent=2)
        
        #b = a.next_generation(3)
        a = Evolve(prev_scoresum = a.scoresum, nn=nn)
        
    nn.save('test')
