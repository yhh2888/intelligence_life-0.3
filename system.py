from newmap import *
from cells import *
from multinet import *
from base.randtree import randtree
import numpy as np
from time import perf_counter as pfc
import sys

model = MyNetwork((60, 60))
dataset = MyDataset()
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
criterion = torch.nn.MSELoss()

class Combiner:
    def __init__(self, gene_data):
        self.received_param = [random.uniform(-1, 1) for i in range(10)]
        self.gene = gene_data
        self.netc = []
        for i in self.gene[0]:
            c=Sender_neuron(i)
            self.netc.append(c)

        for i in self.gene[1]:
            if i[0] == 0:
                    cell_ = Variate_neuron(*i[1:])
            elif i[0] == 1:
                    cell_ = Convert_neuron(*i[1:])
            self.netc.append(cell_)
    
        self.netc.append(Reinf_decide())
        self.netc.append(Movecell())

        self.branch = self.gene[2]
        self.branchpoint = self.gene[3]
        
    def execute(self, mapinfo):
        #밝혀진 변수들과 그 값, 그리고 전체 변수의 수
        self.found = [i for i in range(10)]
        self.all = [i for i in range(len(self.netc)+10+4)]
        self.neuron_value = [self.received_param[i] for i in range(10)]+[None for i in range(len(self.gene[0])+len(self.gene[1])+6)]
        self.doubled = 0
        
        #Sender Neuron에 공간정보 전달하기
        for i in range(len(self.gene[0])):
            first_att = dir(self.netc[i])[dir(self.netc[i]).index('__weakref__')+1]
            if first_att in sender_typelist:
                self.netc[i].val = mapinfo[sender_typelist.index(first_att)][0]
            else :
                self.netc[i].val = 0

            if self.gene[0][i] == 3 or self.gene[0][i] == 4:
                self.found.append(i+10+self.doubled)
                self.found.append(i+11+self.doubled)
                self.neuron_value[i+10+self.doubled], self.neuron_value[i+11+self.doubled] = self.netc[i].execute()
                self.doubled += 1
            else: 
                self.found.append(i+10+self.doubled)
                self.neuron_value[i+10+self.doubled] = self.netc[i].execute()
            
        #밝혀진 변수는 추가하고 연결망 계산하고
        for i in range(len(self.gene[2])-6):
            self.found.append(i+10+len(self.gene[0])+self.doubled)
            self.neuron_value[i+10+len(self.gene[0])+self.doubled] = self.netc[i+len(self.gene[0])].execute(sum([self.neuron_value[self.gene[2][i][cellsf]] \
                                                                                                          for cellsf in range(len(self.gene[2][i][:-1]))]))

        #reinf
        self.netc[-2].reinforce = bool(torch.round(torch.tensor(sum([self.neuron_value[k] for k in self.gene[2][-6][:-1]])%1)))
        self.neuron_value[-6] = self.netc[-2].reinforce
        self.netc[-2].strength = sum([self.neuron_value[k] for k in self.gene[2][-5][:-1]])
        self.neuron_value[-5] = self.netc[-2].strength
            
        #Movecell
        for i in range(4):
            self.neuron_value[-4+i] = sum([self.neuron_value[k] for k in self.gene[2][-6+i][:-1]])
            self.found.append(len(self.gene[2])+4+len(self.gene[0])+i)
            
        self.netc[-1].right = self.neuron_value[-4]
        self.netc[-1].down = self.neuron_value[-3]
        self.netc[-1].left = self.neuron_value[-2]
        self.netc[-1].up = self.neuron_value[-1]

        

class Evolution:
    def __init__(self, number):
        self.combs = []
        for i in range(number):
            self.combs.append(Combiner(self.randgene()))
        self.maps = Map(800, 800)

        self.maps.run()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
            self.maps.run(self.execute())
            try:
                for e in range(len(self.maps.entitys)):
                    self.combs[e].received_param = model(self.maps.entitys[e].view.unsqueeze(0)).tolist()[0][0]
            except Exception as l:
                print(self.maps.entitys[e].x, self.maps.entitys[e].y, self.maps.entitys[e].view.shape)
                
    def execute(self):
        self.forward_results = []
        for i in range(len(self.combs)):
            self.combs[i].execute(np.array([[self.maps.entitys[i].energy/300,
                     self.maps.entitys[i].energy_g/30,
                     self.maps.entitys[i].nst_food/15,
                     self.maps.entitys[i].nst_other/15,
                     self.maps.entitys[i].nst_food_angle/360,
                     self.maps.entitys[i].nst_other_angle/360,
                     self.maps.entitys[i].borderdistance/100,
                     self.maps.entitys[i].otherisin,
                     self.maps.entitys[i].foodisin,
                     random.uniform(-1, 1)]]).T.tolist())

            self.forward_results.append([self.combs[i].netc[-2].reinforce,
                                         self.combs[i].netc[-2].strength,
                                         torch.argmax(torch.tensor(self.combs[i].neuron_value[-4:])).item()])

        return self.forward_results

    def randgene(self, start=5, middle=10, prob=0.15):
        start_code = [random.randint(1, 10) for i in range(start)]
        for i in start_code:
            if i == 3 or i == 4:
                start += 1
                
        middle_code = [random.randint(0, 1) for i in range(middle)]
        branch = randtree(10).generate_random_tree(prob=prob,
                                                   cloud=start+middle+6,
                                                   start_unit=[10+i for i in range(start)],
                                                   end_unit=[10+start+middle+i for i in range(6)],
                                                   sequence_mode = True
                                                   )
        for i in range(len(middle_code)):
            if middle_code[i] == 0:
                middle_code[i] = [middle_code[i], random.uniform(-1, 1),
                                  [random.randint(0, 3) for j in range(random.randint(1, 8))],
                                   (0, 2)]
            elif middle_code[i] == 1:
                middle_code[i] = [middle_code[i], random.randint(0, 4),
                                  [random.uniform(0.3, 3), random.uniform(-3, -0.3)][random.randint(0, 1)],
                                  random.uniform(0.3, 3),
                                  random.uniform(-1, 1)]

        branchpoint = []
            
        for i in branch:
            roads = []
            for j in i:
                roads.append(random.uniform(-0.8, 0.8))
            branchpoint.append(roads)
                
        return (start_code, middle_code, branch, branchpoint)

if __name__ == '__main__':
    ev = Evolution(50)
    
