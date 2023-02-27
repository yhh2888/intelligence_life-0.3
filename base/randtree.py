import random, itertools, time

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
    
def datatest(num, leng, data = None):
    done = False
    had = 0
    datanone = True
    alter_data = []
    letters = "0123456789abcdef"
    perms = itertools.permutations(letters)
    
    if data != None:
        for i in data:
            alter_data.append(int(i, 16))
        data = alter_data
        datanone = False
    while done == False and 2<=num<=7:
        if datanone == True:
            data = [random.randint(1, 16) for i in range(leng)]
        else :
            alter_data = []
            nth_perm = next(itertools.islice(perms, had, None))
            for i in data:
                alter_data.append(int(nth_perm[i], 16))
                data = alter_data
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

hexacodes = []

for i in range(16):
    dic = {}
    for j in range(16):
        dic[hex(j)[2:]] = hex((j+i)%16)[2:]
    hexacodes.append(dic)

thenumb = ''.join([hex(random.randint(0, 15))[2:] for i in range(500)])

def timetest(num):
    t = time.time()
    for i in range(num):
        for j in range(4096):
            e = datatest(1, 50, thenumb[0:50])
    print(time.time()-t)
    
letters = "abcde"
n = 42  # 출력할 순열 번호 - 이 경우 42번째 순열을 출력합니다.

perms = itertools.permutations(letters)
nth_perm = next(itertools.islice(perms, n-1, None))
