import random, itertools, time

class randtree:
    def __init__(self, num_start_nodes):

        self.startnum = num_start_nodes
        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        
        
    def generate_random_tree(self, code = None, prob=0.3):
        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        self.ables = [i for i in self.nodes]
        self.branch = None
        
        if code == None:
            while len(self.ables) > 1:
                chosen = random.sample(self.ables, 2)
                new_nodes = self.nodes[-1]+1
                self.nodes.append(new_nodes)
                self.ables.append(new_nodes)
                del self.ables[self.ables.index(chosen[0])]
                del self.ables[self.ables.index(chosen[1])]
                self.steps.append([self.nodes.index(chosen[0]),
                                   self.nodes.index(chosen[1]),
                                   new_nodes])
                for i in self.nodes[:-1]:
                    if prob > random.random() and i not in self.steps[-1]:
                        self.steps[-1] = self.steps[-1][:-1] + [i] + [self.steps[-1][-1]]
        
        if code != None:
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
            self.edge = edge
        
        return self.steps

'''
code = [random.randint(0, 20) for i in range(24)]
a = randtree(24)
print(a.generate_random_tree(code))
'''
