from newmap import *
from cells import *
from multinet import *
from base.randtree import randtree
import numpy as np
from time import perf_counter as pfc
import sys, warnings, traceback, time, json

warnings.filterwarnings("ignore")

dataset = MyDataset()
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
criterion = torch.nn.MSELoss()

def execute(model, dataloader, num_epochs=1, learning_rate=0.005):
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    for epoch in range(num_epochs):
        for data, labels in dataloader:
            # 입력과 라벨을 GPU로 이동 (GPU 사용 시)
            # data = data.to(device)
            # labels = labels.to(device)
            outputs = model(data)
            
            optimizer.zero_grad()
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
class Combiner:
    def __init__(self, gene_data):
        self.received_param = [random.uniform(-1, 1) for i in range(10)]
        self.gene = gene_data
        self.netc = []
        self.model = MyNetwork(20)
        self.view = None

        self.memoryv = [[[0.0 for i in range(20)] for j in range(20)]]
        self.memoryp = [[0.0 for i in range(10)]]

        self.gene = list(self.gene)
        
        #진화 기록
        if len(self.gene) < 5:
            self.gene.append([])
        
        #유전자형 오류 수리(세포와 브랜치의 차이가 6이 아닌 경우)
        if len(self.gene[2])-len(self.gene[1]) != 6:
            if len(self.gene[2])-len(self.gene[1]) < 6:
                for i in range(len(self.gene[1])-len(self.gene[2])+6):
                    if random.random() > 0.9:
                        self.gene[2] = self.gene[2][:-6] + [[0, self.gene[2][-6][-1]]] + [k[:-1]+[k[-1]+1] for k in self.gene[2][-6:]]
                        self.gene[3] = self.gene[3][:-6] + [[random.random()]] + self.gene[3][-6:]
                    else:
                        del self.gene[1][-1]
            elif len(self.gene[2])-len(self.gene[1]) > 6:
                for i in range(len(self.gene[2])-len(self.gene[1])-6):
                    del self.gene[2][-1]
                    del self.gene[3][-1]

        #유전자형 오류 수리(브랜치가 하나 이상의 세포를 건너뛰는 경우)
        deleted_instant = 0
        i = 0
        pre_i = int(i)
        while i < len(self.gene[2])-2:
            i = pre_i
            i += 1
            pre_i = int(i)
            i -= deleted_instant
            if self.gene[2][i][-1]+1 != self.gene[2][i+1][-1]:
                if self.gene[2][i][-1]+1 > self.gene[2][i+1][-1]:
                    remain_branch = self.gene[2][i+1][:-1]
                    del self.gene[2][i+1]
                    del self.gene[3][i+1]
                    self.gene[2] = self.gene[2][:i+1] + [[*remain_branch, self.gene[2][i][-1]+1]] + self.gene[2][i+1:]
                    self.gene[3] = self.gene[3][:i+1] + [[random.random() for i in remain_branch]] + self.gene[3][i+1:]
                    deleted_instant += 1

                elif self.gene[2][i][-1]+1 < self.gene[2][i+1][-1]:
                    _prebranch = self.gene[2][i][:-1]
                    self.gene[2] = self.gene[2][:i+1] + [[*[_prebranch if len(_prebranch) > 1 else [0]][0], self.gene[2][i][-1]+1]] + self.gene[2][i+1:]
                    del self.gene[2][-1]
                    self.gene[3] = self.gene[3][:i+1] + [[random.random()]] + self.gene[3][i+1:]
                    del self.gene[3][-1]
                    deleted_instant += 1
            

        #유전자형 오류 수리(브랜치와 브랜치수치가 서로 일정하지 않은 경우)
        for i in range(len(self.gene[2])):
            if len(self.gene[2][i])-len(self.gene[3][i]) != 1:
                if len(self.gene[2][i])-len(self.gene[3][i]) < 1:
                    for i in range(min(0, len(self.gene[3][i])-len(self.gene[2][i])+1)):
                        try:
                            del self.gene[3][i][-1]
                        except Exception as e:
                            print(e)
                elif len(self.gene[2][i])-len(self.gene[3][i]) > 1:
                    for i in range(min(0, len(self.gene[2][i])-len(self.gene[3][i])-1)):
                        self.gene[3][i].append(random.random())

        self.gene = tuple(self.gene)

        self.gene[4].append(self.gene[2])
                    
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

        #fix system 제작:
        
        #밝혀진 변수들과 그 값, 그리고 전체 변수의 수
        self.found = [i for i in range(10)]
        self.all = [i for i in range(len(self.netc)+10+4)]
        self.neuron_value = [self.received_param[i] for i in range(10)]+[None for i in range(len(self.gene[0])+len(self.gene[1])+6)]
        
        #Sender Neuron에 공간정보 전달하기
        for i in range(len(self.gene[0])):
            first_att = dir(self.netc[i])[dir(self.netc[i]).index('__weakref__')+1]
            if first_att in sender_typelist:
                self.netc[i].val = mapinfo[sender_typelist.index(first_att)][0]
            else :
                self.netc[i].val = 0
            self.found.append(i+10)
            self.neuron_value[i+10] = self.netc[i].execute()
            
        #밝혀진 변수는 추가하고 연결망 계산하고
        for i in range(len(self.gene[2])-6):
            self.found.append(i+10+len(self.gene[0]))
            #None오류가 뜨면 그 변수는 총합에서 제거
            self.neuron_value[i+10+len(self.gene[0])] = self.netc[i+len(self.gene[0])].execute( \
                sum([self.neuron_value[self.gene[2][i][cellsf]] for cellsf in range(len(self.gene[2][i][:-1])) if self.neuron_value[self.gene[2][i][cellsf]] != None]))

        #reinf
        #None오류가 뜨면 그 변수는 총합에서 제거
        self.netc[-2].reinforce = bool(torch.round(torch.tensor(sum([self.neuron_value[k] for k in self.gene[2][-6][:-1] if self.neuron_value[k] != None])%1)))
        self.neuron_value[-6] = self.netc[-2].reinforce
        #None오류가 뜨면 그 변수는 총합에서 제거
        self.netc[-2].strength = sum([self.neuron_value[k] for k in self.gene[2][-5][:-1] if self.neuron_value[k] != None])
        self.neuron_value[-5] = self.netc[-2].strength

        if self.view != None:
            if self.netc[-2].strength > 0.7:
                self.memoryv.append(self.view)
                self.memoryp.append(self.received_param)
        if self.netc[-2].reinforce > 0.99999:
            dataset_ = MyDataset(torch.tensor([i for i in self.memoryv]), torch.tensor([i for i in self.memoryp]))
            self.memoryv = [[[0.0 for i in range(20)] for j in range(20)]]
            self.memoryp = [[0.0 for i in range(10)]]
            execute(self.model, DataLoader(dataset_))
            
            
        #Movecell
        for i in range(4):
            #None오류가 뜨면 그 변수는 총합에서 제거
            self.neuron_value[-4+i] = sum([self.neuron_value[k] for k in self.gene[2][-6+i][:-1] if self.neuron_value[k] != None])
            self.found.append(len(self.gene[2])+4+len(self.gene[0])+i)
            
        self.netc[-1].right = self.neuron_value[-4]
        self.netc[-1].down = self.neuron_value[-3]
        self.netc[-1].left = self.neuron_value[-2]
        self.netc[-1].up = self.neuron_value[-1]

        return (self.netc[-1].right, self.netc[-1].down, self.netc[-1].left, self.netc[-1].up)

class Evolution:
    def __init__(self, number, specify=False):
        self.combs = []
        for i in range(number):
            if specify==False:
                self.combs.append(Combiner(self.randgene()))
            else:
                self.combs.append(Combiner(specify[random.randint(0, len(specify)-1)]))
        self.specify = specify
        self.maps = Map(1000, 1000)

        self.maps.run()

    def play(self):
        global ev
        
        best_genes = []
        if self.specify != False:
            with open(r'C:\Users\KDCA\Desktop\IL\best_obj.json') as f:
                best_genes = json.load(f)
            
        running = True
        t = time.time()
        while running:
            #t =pfc()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False

            try:
                self.maps.run(self.execute())
            except Exception as e:
                print(e, traceback.format_exc())
                ev = Evolution(50, best_genes[-10:])
                ev.play()

            #print(pfc()-t)
            #t =pfc()
            deleted_instant = 0
            try:
                for e in range(len(self.maps.entitys)):
                    self.combs[e-deleted_instant].received_param = self.combs[e-deleted_instant].model(self.maps.entitys[e-deleted_instant].view.unsqueeze(0)).tolist()[0][0]
                    self.combs[e-deleted_instant].view = self.maps.entitys[e-deleted_instant].view
                    if not (3<self.maps.entitys[e-deleted_instant].x<self.maps.maptile_width-3 and 3<self.maps.entitys[e-deleted_instant].y<self.maps.maptile_height-3):
                        del self.combs[e-deleted_instant]
                        del self.maps.entitys[e-deleted_instant]
                        deleted_instant += 1
                    
            except Exception as l:
                print(self.maps.entitys[e-deleted_instant].x, self.maps.entitys[e-deleted_instant].y, self.maps.entitys[e-deleted_instant].view.shape, l)

            

            deleted_num = 0

            #print(pfc()-t)
            #t =pfc()
            
            for i in range(len(self.maps.entitys)):

                
                
                if self.maps.entitys[i-deleted_num].energy > 1000:
                    self.maps.entitys[i-deleted_num].energy -= 800
                    self.maps.entitys.append(Entity(self.maps.screen,
                                                    self.maps.entitys[i-deleted_num].x, self.maps.entitys[i-deleted_num].y,
                                                    self.maps.MAP_WIDTH, self.maps.MAP_HEIGHT,
                                                    self.maps.WHITE, self.maps.BLOCK_SIZE))
                    self.combs.append(Combiner(self.mutated_child(i-deleted_num)))
                    ab = [self.combs[-1].gene[1], self.combs[-1].gene[2]]

                elif self.maps.entitys[i-deleted_num].energy < 0:
                    del self.maps.entitys[i-deleted_num]
                    del self.combs[i-deleted_num]
                    deleted_num += 1

            #print(pfc()-t)
            #pt =pfc()
            
            if time.time() - t > 30:
                best_gene = None
                best_objscore = 0
                for i in range(len(self.maps.entitys)):
                    if self.maps.entitys[i].score > best_objscore:
                        best_objscore = self.maps.entitys[i].score
                        best_gene = self.combs[i].gene[0:4]
                if best_gene != None:
                    best_genes.append(best_gene)
                    with open(r'C:\Users\KDCA\Desktop\IL\best_obj.json', 'w') as f:
                        json.dump(best_genes, f, indent=1)
                t = time.time()

            if len(self.combs) == 0:
                ev = Evolution(50, best_genes[-10:])
                ev.play()

            #print(pfc()-pt, 'here')
                
    def execute(self):
        self.forward_results = []
        for i in range(len(self.combs)):
            try:
                self.combs[i].execute(np.array([[self.maps.entitys[i].energy/300,
                         self.maps.entitys[i].energy_g/30,
                         self.maps.entitys[i].nst_foodx/15,
                         self.maps.entitys[i].nst_foody/15,
                         self.maps.entitys[i].nst_otherx/15,
                         self.maps.entitys[i].nst_othery/15,
                         self.maps.entitys[i].nst_food_angle/360,
                         self.maps.entitys[i].nst_other_angle/360,
                         self.maps.entitys[i].borderdistance/100,
                         self.maps.entitys[i].otherisin,
                         self.maps.entitys[i].foodisin,
                         random.uniform(-1, 1)]]).T.tolist())
            except Exception as e:
                print(e, i, traceback.format_exc())
                ev = Evolution(50, best_genes[-10:])
                ev.play()
            try:
                self.forward_results.append([self.combs[i].netc[-2].reinforce,
                                         self.combs[i].netc[-2].strength,
                                         torch.argmax(torch.tensor(self.combs[i].neuron_value[-4:])).item()])
            except Exception as e:
                print(e, self.combs[i].neuron_value[-4:])
                
        return self.forward_results

    def randgene(self, start=5, middle=100, prob=0.15):
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
            for j in i[:-1]:
                roads.append(random.uniform(-0.8, 0.8))
            branchpoint.append(roads)
                
        return (start_code, middle_code, branch, branchpoint, [])

    def mutated_child(self, num, probability=0.05):
        new_gene = list(self.combs[num].gene)
        prepare_gene = self.combs[num].gene

        #센더 뉴런 돌연변이
        for i in range(len(new_gene[0])):
            if random.random() < probability:
                new_gene[0][i] = random.randint(1, 10)

        new_gene = self.variate_change(new_gene, probability)
        new_gene = self.branch_change(new_gene, probability)
        new_gene = self.variate_add_remove(new_gene, probability)

        return new_gene

    def variate_change(self, new_gene, probability):
        potential0 = [0, random.uniform(-1, 1),
                                  [random.randint(0, 3) for j in range(random.randint(1, 8))],
                                   (0, 2)]
        potential1 = [1, random.randint(0, 4),
                                  [random.uniform(0.3, 3), random.uniform(-3, -0.3)][random.randint(0, 1)],
                                  random.uniform(0.3, 3),
                                  random.uniform(-1, 1)]
        #변화 뉴런 돌연변이
        for i in range(len(new_gene[1])):
            if random.random() < probability/2:
                if new_gene[1][i][0] == 0:
                    new_gene[1][i] = [1, random.randint(0, 4),
                                      [random.uniform(0.3, 3), random.uniform(-3, -0.3)][random.randint(0, 1)],
                                      random.uniform(0.3, 3),
                                      random.uniform(-1, 1)]
                elif new_gene[1][i][1] == 1:
                    new_gene[1][i] = [0, random.uniform(-1, 1),
                                      [random.randint(0, 3) for j in range(random.randint(1, 8))],
                                       (0, 2)]

            for j in range(len(new_gene[1][i])):
                if random.random() < probability:
                    if new_gene[1][i][0] == 0:
                        new_gene[1][i][j] = potential0[j]
                        potential0 = [0, random.uniform(-1, 1),
                                  [random.randint(0, 3) for j in range(random.randint(1, 8))],
                                   (0, 2)]
                    elif new_gene[1][i][0] == 1:
                        new_gene[1][i][j] = potential1[j]
                        potential1 = [1, random.randint(0, 4),
                                  [random.uniform(0.3, 3), random.uniform(-3, -0.3)][random.randint(0, 1)],
                                  random.uniform(0.3, 3),
                                  random.uniform(-1, 1)]

        return tuple(new_gene)
            

    def branch_change(self, new_gene, probability):
        new_gene = list(new_gene)
        prepare_gene = tuple(new_gene)
        #가지 추가/변화/삭제
        try:
            for i in range(len(new_gene[2])):
                if random.random() < probability:
                    _3div_prob = random.random()
                    ea = random.choice([k+1 for k in range(3) for j in range((3-k)**2)])
                    if _3div_prob < 0.33 and len(new_gene[2][i]) <= new_gene[2][i][-1]-ea-1:
                        try:
                            new_gene[2][i] = new_gene[2][i][:-1] + random.sample([k for k in range(new_gene[2][i][-1]) if (k not in new_gene[2][i] and k < new_gene[2][-1][-1]-5)], ea) \
                                         + [new_gene[2][i][-1]]
                        except Exception as e:
                            print(traceback.format_exc(), [k for k in range(new_gene[2][i][-1]) if (k not in new_gene[2][i] and k < new_gene[2][-1][-1]-5)])
                        new_gene[3][i] = new_gene[3][i][:-1] + [random.random() for k in range(ea)] + [new_gene[3][i][-1]]

                    elif 0.33 <= _3div_prob < 0.67 and len(new_gene[2][i]) < new_gene[2][i][-1]:
                        for j in range(ea):
                            try:
                                new_gene[2][i][random.randint(0, len(new_gene[2][i])-2)] = random.choice([k for k in range(new_gene[2][i][-1]) if (k not in new_gene[2][i] and k < new_gene[2][-1][-1]-5)])
                            except Exception as e:
                                print(new_gene[2][i], new_gene[3][i], traceback.format_exc())

                    elif 0.67 <= _3div_prob and len(new_gene[2][i]) >= 2+ea:
                        for j in range(ea):
                            try:
                                pos = random.randint(0, len(new_gene[2][i])-2)
                            except Exception as e:
                                print(new_gene[2][i], new_gene[3][i], traceback.format_exc())
                            del new_gene[2][i][pos]
                            del new_gene[3][i][pos]
                            
        except Exception as e:
            return prepare_gene

        return tuple(new_gene)
                        
    def variate_add_remove(self, new_gene, probability):
        new_gene = list(new_gene)
        prepare_gene = tuple(new_gene)
        #변화뉴런 추가/삭제
        if random.random() < probability*3:
            _2div_prob = random.random()
            if _2div_prob < 0.7 and len(new_gene[2]) < 1500:
                _middle_code0 = random.randint(0, 1)
                if _middle_code0 == 0:
                    new_gene[1].append([0, random.uniform(-1, 1),
                                  [random.randint(0, 3) for j in range(random.randint(1, 8))],
                                   (0, 2)])
                elif _middle_code0 == 1:
                    new_gene[1].append([1, random.randint(0, 4),
                                  [random.uniform(0.3, 3), random.uniform(-3, -0.3)][random.randint(0, 1)],
                                  random.uniform(0.3, 3),
                                  random.uniform(-1, 1)])
                
                new_gene[2] = new_gene[2][:-6] + [[0, new_gene[2][-6][-1]]] + [k[:-1]+[k[-1]+1] for k in new_gene[2][-6:]]
                new_gene[3] = new_gene[3][:-6] + [[random.random()]] + new_gene[3][-6:]
                
                
            if _2div_prob >= 0.7 and len(new_gene[2]) > 10:
                del_neuron = random.randint(0, len(new_gene[2])-8)
                crit_num = new_gene[2][del_neuron][-1]
                try:
                    del new_gene[1][del_neuron]
                    del new_gene[2][del_neuron]
                    del new_gene[3][del_neuron]
                except Exception as e:
                    print(traceback.format_exc())
                for k in range(len(new_gene[2])):
                    deleted_instant = 0
                    for l in range(len(new_gene[2][k])):
                        if new_gene[2][k][l-deleted_instant] > crit_num:
                            new_gene[2][k][l-deleted_instant] -= 1
                        elif new_gene[2][k][l-deleted_instant] == crit_num:
                            try:
                                del new_gene[2][k][l-deleted_instant]
                                del new_gene[3][k][l-deleted_instant]
                            except Exception as e:
                                print(traceback.format_exc())
                                return prepare_gene
                            deleted_instant += 1
            
        print(len(new_gene[1]), len(new_gene[2]), 'after')
    
        return tuple(new_gene)
            
            
if __name__ == '__main__':
    with open(r'C:\Users\KDCA\Desktop\IL\best_obj.json') as f:
        best_genes = json.load(f)
    ev = Evolution(50, best_genes[-5:])
    ev.play()
    
