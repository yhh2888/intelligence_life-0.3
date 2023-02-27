import random
class randtree:
    def __init__(self, num_start_nodes):

        self.startnum = num_start_nodes
        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        
    def generate_random_tree(self, code = None):
        self.nodes = [i for i in range(self.startnum)]
        self.steps = []
        self.ables = [i for i in self.nodes]
        
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
        
        return self.steps
    
def datatest(num, leng):
    done = False
    had = 0
    while done == False and 2<=num<=7:
        data = [random.randint(1, 16) for i in range(leng)]
        data_dic = {}
        for i in range(len(data)-1):
            if str(data[i])+'+'+str(data[i+1]) in data_dic:
                data_dic[str(data[i])+'+'+str(data[i+1])] += 1
            else:
                data_dic[str(data[i])+'+'+str(data[i+1])] = 1
        for i in data_dic:
            if data_dic[i] >= num and len(set(data)) != 16:
                done = True
        had += 1
    return had
