import numpy as np
import time, random, traceback

from turnset import *
from base.network import NeuralNetwork as Nets

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

class Evolve:
    def __init__(self, amount=20, prev_scoresum = 0, net=None):
        self.nn = net
        self.prev_scoresum = prev_scoresum
        self.reevolve = False
        self.circumstances = Game(50, 50)
        self.amountsleft = amount
        self.amounts = amount
        self.received_data = []
        
        '''ext = netdata_extract(self.nn)'''

        self.paramgens = [self.nn for i in range(amount)]

        '''for i in range(len(self.paramgens)):
            netdata_substitute(self.paramgens[i], ext)'''
        
    def test(self, next_gen, view_lock = False, time_=False):
        global term_data
        self.scorelist = []
        
        '''for i in range(len(self.paramgens[next_gen:])):
            net_mutate(self.paramgens[next_gen+i])'''
            
        for i in range(self.amounts):
            print(id(self.paramgens[i]))
            score = self.circumstances.run_by_AI(view_lock = view_lock, net=self.paramgens[i], time_=time_)
            for i in self.paramgens[i].received_data:
                self.received_data.append(i)
            self.scorelist.append(score[0])
            self.circumstances = Game(50, 50)
            term_data = score[1]
            
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

        self.paramgens = []
        count = 0
        while self.amountsleft>1:
            self.paramgens.append(self.news[i])
            count += 1
            count = count%next_gen
            self.amountsleft -= 1
        self.amountsleft = self.amounts

def rep_test(rep, view_lock = False, time_=False):
    
    try:
        with open('mobs_data.json') as f:
            received_data = json.load(f)
    except Exception as e:
        print(e)
        received_data = []

    '''try:
        with open(os.getcwd()+r'\base\modelparam_data.json') as f:
            mp = json.load(f)
            
    except Exception as e:
        print(e)

    ns = Nets(380)
    netparams = []
        
    for n in range(len(mp)):
        netparams.append(torch.tensor(mp[n]))'''
        
    '''for n in range(3):
            ns.stack[n*3].weight = torch.nn.parameter.Parameter(netparams[n*2])
            ns.stack[n*3].bias = torch.nn.parameter.Parameter(netparams[n*2+1])'''
    
    try:
        a = Evolve(net=Nets(380))
    
        
        for i in [i for i in range(rep)]:
            
            t = time.time()
            
            a.test(5, view_lock = view_lock, time_=time_)
            
            print(time.time()-t)
            received_data = received_data + a.received_data
            with open('mobs_data.json', 'w') as f:
                json.dump(received_data, f)
            
            #b = a.next_generation(3)
            a = Evolve(prev_scoresum = a.scoresum, net=ns)
            
    except Exception as e:
        print(e, traceback.format_exc())
    if a.circumstances.quit == True:
        pygame.quit()

def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)

def netdata_extract(net, length=4):
    extracted_weights = []
    extracted_biases = []
    for n in range(length-1):
        extracted_weights.append(torch.tensor(net.stack[n*(length-1)].weight))
        extracted_biases.append(torch.tensor(net.stack[n*(length-1)].bias))
    return extracted_weights, extracted_biases

def netdata_substitute(net, extracted, length=4):
    with torch.no_grad():
        for i in range(length-1):
            net.stack[i*(length-1)].weight = torch.nn.parameter.Parameter(extracted[0][i])
            net.stack[i*(length-1)].biases = torch.nn.parameter.Parameter(extracted[1][i])
