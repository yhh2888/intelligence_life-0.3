from newmap import *
from cells import *
from multinet import *
from base.randtree import randtree
import numpy as np

model = MyNetwork()
dataset = MyDataset()
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
criterion = torch.nn.MSELoss()


'''
model(dataloader.dataset[0][0].unsqueeze(0))

1. 공간 기본정보와 그것을 모델로 해석한 결과값을 기억하기
2. cells 조합하는 클래스 만들기
2-1. 보상결정, 학습강도, 이동, 공격.
2-2. 에너지, 에너지기울기, 공간적정보, 랜덤포인트.
2-3. 전의특징기억(수치, 기억능력), 신호변환
3. 모델 해석 결과값을 cell조합 클래스에 넣기
4. 1에서 얻은 기억된 데이터를 때때로 학습시키기(보상결정시 학습강도만큼)
'''

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
        self.all = [i for i in range(len(self.netc)+16)]
        self.neuron_value = [self.received_param[i] for i in range(10)]+[None for i in range(21)]

        #Sender Neuron에 공간정보 전달하기
        for i in range(len(self.gene[0])):
            first_att = dir(self.netc[i])[dir(self.netc[i]).index('__weakref__')+1]
            if first_att in sender_typelist:
                self.netc[i].info = mapinfo[sender_typelist.index(first_att)]
            else :
                self.netc[i].info = None
                
            self.found.append(i+10)
            self.neuron_value[i+10] = self.netc[i].execute()
            
        #밝혀진 변수는 추가하고 연결망 계산하고
        while self.all != self.found:
            for i in range(len(self.gene[2])):
                if len(set(self.found)) == len(set(self.found+self.gene[2][i][:-1])) and i+10+len(self.gene[0]) not in self.found and type(self.netc[i]) != Sender_neuron:
                    self.found.append(i+10+len(self.gene[0]))
                    self.neuron_value[i+10+len(self.gene[0])] = self.netc[i].execute(sum([self.neuron_value[self.gene[2][i][cellsf]] for cellsf in range(len(self.gene[2][i][:-1]))]))
                    print(self.netc[i].execute(sum([self.neuron_value[self.gene[2][i][cellsf]] for cellsf in range(len(self.gene[2][i][:-1]))])))
                    
                        
def randgene(start=5, middle=10, prob=0.15):
    start_code = [random.randint(1, 10) for i in range(start)]
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

'''b.generate_random_tree(prob=0.1, cloud=14, start_unit=[10, 11, 12, 13, 14],
                          end_unit=[18,19,20,21,22,23], sequence_mode=True)'''

if __name__ == '__main__':
    a = Combiner(randgene())
    maps = Map(800, 800)
    maps.run()

'''a.execute(np.array([[maps.entitys[i].energy,
                     maps.entitys[i].energy_g,
                     maps.entitys[i].nst_food,
                     maps.entitys[i].nst_other,
                     maps.entitys[i].nst_food_angle,
                     maps.entitys[i].nst_other_angle,
                     maps.entitys[i].borderdistance,
                     maps.entitys[i].otherisin,
                     maps.entitys[i].foodisin,
                     random.uniform(-1, 1)] for i in range(len(maps.entitys))]).T.tolist())'''
