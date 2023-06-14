import random, itertools, time

class randtree:
    def __init__(self, num_start_nodes):

        self.startnum = num_start_nodes
        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        
    def generate_random_tree(self,
                             code = None,
                             prob=0.3,
                             cloud = 5,
                             start_unit=[],
                             end_unit=[],
                             delete_mode = False,
                             sequence_mode = False,
                             minimum_branch = 2):

        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        self.branch = None

        if sequence_mode == False:
            self.ables = [x for x in [i for i in range(self.startnum+cloud)] if x not in [i for i in end_unit]]
        else :
            self.ables = [i for i in self.nodes]
        
        if code == None:
            while cloud >= 1:
                new_nodes = self.nodes[-1]+1
                self.nodes.append(new_nodes)
                chosen = random.sample([x for x in self.ables if x != new_nodes], minimum_branch)
                if new_nodes not in end_unit and sequence_mode != False:
                    self.ables.append(new_nodes)  
                if delete_mode == True:
                    for m in range(minimum_branch):
                        del self.ables[self.ables.index(chosen[m])]
                if new_nodes not in start_unit:
                    self.steps.append([*[self.ables.index(chosen[m]) for m in range(minimum_branch)],
                                       new_nodes])
                    for i in [self.ables[:-1] if self.ables[:-1]==new_nodes else self.ables][0]:
                        if prob > random.random() and i not in self.steps[-1]:
                            self.steps[-1] = self.steps[-1][:-1] + [i] + [self.steps[-1][-1]]
                cloud -= 1
        
        '''elif code != None:
            self.nodes = [1, 2, 3]
            self.steps = [[2, 3, 1]]
            edge = [2, 3]
            codeinterp_ = 0
            while len(edge) != self.startnum:
                call_num = max(edge)
                dif_node = edge[code[codeinterp_]%len(edge)]
                del edge[int(code[codeinterp_])%len(edge)]
                dif_branch = [call_num+1, call_num+2]
                self.steps.append([dif_branch[0], dif_branch[1], dif_node])
                edge.extend(dif_branch)
                self.nodes.extend(dif_branch)
                codeinterp_ += 1
            self.steps = list(reversed(self.steps))
            self.edge = edge'''
        
        return self.steps

'''
code = [random.randint(0, 20) for i in range(24)]
a = randtree(24)
print(a.generate_random_tree(code))
'''
