import matplotlib.pyplot as plt
import random, time
import numpy as np

from time import perf_counter
from scipy.stats import gaussian_kde
from collections import deque
from more_itertools import distinct_permutations
from itertools import combinations as comb

#같은 것이 있는 순열 - 중복 제외한 것(중복 판단 자체를 하지 않아 빠름)
def unique_perms(series):
    return {"".join(p) for p in distinct_permutations(series)}

#거리에 따른 움직임 개수 구하기
def dist_code(start, fin):
	disco = []
	dist = [fin[0]-start[0], fin[1]-start[1]]
	dir_ = ['r', 'd', 'l', 'u']
	for i in range(2):
		step = [dir_[i] if dist[i]>=0 else dir_[i+2]][0]
		for j in range(abs(dist[i])):
			disco.append(step)
	return disco

#방향 코드에 따른 포인트 수치 변화
def direction(point, direct):
    if direct == 'r':
        point[0] += 1
    if direct == 'd':
        point[1] += 1
    if direct == 'l':
        point[0] -= 1
    if direct == 'u':
        point[1] -= 1
    return point

#------------------------------------------------------------------------



#@jitclass(spec)
class spreader:
    def __init__(self, typ=0, moves=5, quant_coeff=10, mrec_disp=True, unable_disp=False):
        
        self.moves = moves
        self.route=[]
        self.nearpoint = []
        self.nearlist = []
        self.connected = []
        self.destinate = []

        #랜덤 포인트 지정
        self.list_ = [[random.randint(-50, 50), random.randint(-50, 50)] for i in range(50)]

        #랜덤 포인트 표시
        plt.scatter([self.list_[i][0] for i in range(50)],
            [self.list_[i][1] for i in range(50)],
            marker='o', s=10, c='lightgreen', edgecolors='black')

        #랜덤 주인공 포인트 설정(0 - 완전 랜덤, 1 - 격자점, 2 - 군집) 
        if typ==0:
            self.test_data = [[random.randint(-50, 50) for i in range(2)] for i in range(quant_coeff**2)]
            print('test_data type : total random')
        elif typ==1:
            self.test_data = [[i*(100/quant_coeff)-50, j*(100/quant_coeff)-50] for i in range(quant_coeff) for j in range(quant_coeff)]
            print('test_data type : lattice point')
        elif typ==2:
            self.test_data = [[np.random.normal(scale=5), np.random.normal(scale=5)] for i in range(quant_coeff**2)]
            print('test_data type : dense cluster')

        #리스트일 경우
        elif type(typ)==list:
            self.test_data = typ

        #self.testall(self.test_data, mrec_disp, unable_disp)
        
    def testall(self, test_data, mrec_disp, unable_disp):
        #시간 기록
        t = time.time()
        #움직임 목적지 계산
        for a in test_data:
            self.spread1(a)
            self.nearpoint.append(10**10)

        self.Xmg, self.Ymg = np.mgrid[-50:50:100j, -50:50:100j]
        kdes = self.kde_set(self.list_)
        self.Z = self.kde_distribution(*kdes, 0.15, 1) + self.kde_distribution(*kdes, 0.15, 0.8)

        #움직임 경로 계산
        self.test_move1(test_data, mrec_disp=mrec_disp)
        
        if unable_disp == True:
            self.unable_land_display(density=2)
        
        print(time.time()-t)
    
    def spread1(self, point):
        edge=[]
        edge.append(point)
        edge = edge[0]
        
        for j in range(self.moves):
            
            self.nearlist = self.nears(edge, mobs=self.list_)
            
            if len(self.nearlist) != 0:
                center = [sum([i[0] for i in self.nearlist])/len(self.nearlist),
                          sum([i[1] for i in self.nearlist])/len(self.nearlist)]
            else :
                break
            
            self.route.append(edge)
            temp_edge1 = [2*edge[0]-center[0], 2*edge[1]-center[1]]
            temp_edge3 = temp_edge1
            if self.nearest(temp_edge1, self.nearlist) > 5:
                edge = temp_edge1
            else :
                while True:
                    
                    temp_edge2 = [temp_edge3[0]+np.random.normal(scale=5), temp_edge3[1]+np.random.normal(scale=5)]
                    
                    templines = [[temp_edge1[0]+i*0.1*(temp_edge2[0]-temp_edge1[0]),
                                  temp_edge1[1]+i*0.1*(temp_edge2[1]-temp_edge1[1])]
                                 for i in range(11)]
                    
                    self.nearlist = self.nears(temp_edge1, mobs=self.list_)
                    
                    if self.nearest(temp_edge1, self.nearlist) < 5:
                        break
                    
                    line_analyze = [True if j < min(5, self.nearest(point, self.list_)) else False
                                    for j in [self.nearest(templines[i], mobs=self.nears(templines[i], mobs=self.list_)) for i in range(11)]]
                    if True not in line_analyze:
                        break
                    temp_edge3 = temp_edge2

                edge = temp_edge2
        self.route.append(edge)
        self.nearpoint.append(self.nearest(edge, self.nearlist))

        edge = [int(edge[0]), int(edge[1])]
        point = [int(point[0]), int(point[1])]
        self.destinate.append([point, edge])
        
        
        '''if self.route != []:
            plt.plot([point[0]]+[self.route[i][0] for i in range(len(self.route))],
                     [point[1]]+[self.route[i][1] for i in range(len(self.route))],
                     linewidth=0.05, linestyle='solid', color='black')'''

        #plt.scatter(*point, marker='o', s=10, c='red')

        #plt.scatter(*edge, marker='o', s=10, c='blue')

    
    def kde_set(self, points):
        '''if points == [] or 1<=len(points)<=3 :
            points = [[random.randint(-50, 50), random.randint(-50, 50)] for i in range(4)]'''
        
        m1 = np.array([i[0] for i in points])
        m2 = np.array([i[1] for i in points])
        '''while len(set(list(np.cov(m1, m2).reshape(1,4)[0]))) <= 1:
            m1 = np.array([i[0]+0.1**6*random.random() for i in points])
            m2 = np.array([i[1]+0.1**6*random.random() for i in points])'''

        positions = np.vstack([self.Xmg.ravel(), self.Ymg.ravel()])
        values = np.vstack([m1, m2])
        return values, positions

    def kde_distribution(self, values, positions, adjust=0.15, strength=1, speed=False):
        self.kernel = gaussian_kde(values)
        self.kernel.set_bandwidth(self.kernel.factor * adjust)
        Z = np.reshape(self.kernel(positions).T, self.Xmg.shape)
        return np.rot90(Z*strength)
    
    def test_move1(self, test_data, mrec_disp=False):

        self.routes = [[True if self.Z[i][j] < 0.00008 else False for i in range(100)] for j in range(100)]
        
        for i in self.destinate:
            if abs(i[0][0]-i[1][0])+abs(i[0][1]-i[1][1]) < 15:
                r = self.code_analysis(unique_perms(dist_code(*i)), self.routes, i[0])
                if r != None:
                    point = [int(i[0][0]), int(i[0][1])]
                    if mrec_disp == True:
                        self.disp_route(r, i[0], end=i[1])
                        
                else :
                    point = [int(i[0][0]), int(i[0][1])]
                    routelist = dist_code(*i)
                    while r == None:
                        if len(routelist) >= 3:
                            r = self.code_analysis(list(comb(routelist, 3)), self.routes, i[0], dir_only=True)
                        else :
                            r = list(routelist)
                    if mrec_disp == True:
                        self.disp_route(r, i[0], end=None)
            else :
                routelist = dist_code(*i)
                r = self.code_analysis(list(comb(routelist, 3)), self.routes, i[0], dir_only=True)
                if mrec_disp == True and len(r) > 0:
                    self.disp_route(r, i[0], end=None)
                        
        plt.imshow(self.Z, cmap=plt.cm.gist_earth_r, extent=[-50, 50, -50, 50])
    
    def unable_land_display(density=1):
        for i in range(0,100,density):
            for j in range(0,100,density):
                if self.routes[i][j] == False:
                    plt.scatter(i-50, 50-j, s= 5, c='red')
                    
    def nears(self, point, mobs=[], dist=10):
        near = []
            
        for i in mobs:
            if point[0]+dist>i[0]>point[0]-dist and point[1]+dist>i[1]>point[1]-dist:
                near.append(i)
        return near

    def nearest(self, point, mobs):
        if mobs != []:
            return min([((point[0]-i[0])**2+(point[1]-i[1])**2)**0.5 for i in mobs])
        else :
            return 10

    def code_analysis(self, codelist, map_, point, dir_only=False):
        try:
            if dir_only == False:
                for code in codelist:
                    a = [int(point[0]), int(point[1])]
                    
                    for j in range(len(code)):
                        a = direction(a, code[j])
                        if map_[a[0]][a[1]] == False:
                            break
                        if j == len(code)-1:
                            return code
            elif dir_only == True:
                
                mass_list = []
                
                for code in codelist:
                    a = [int(point[0]), int(point[1])]
                    
                    for j in range(len(code)):
                        a = direction(a, code[j])
                        if map_[a[0]][a[1]] == False:
                                mass_list.append(1)
                                break
                        if j == len(code)-1:
                            mass_list.append(self.Z[a[0]][a[1]])
                            
                return codelist[np.argmin(mass_list)]
                    
            else :
                print('dir_only type error')
                    
            return None
        
        except Exception as e:
            print(e)

    def disp_route(self, routes, start, end=None):
        point = [int(start[0]), int(start[1])]
        for j in routes:
            point = direction(point, j)
            plt.scatter(*point, marker='o', s=2, c='black')

        plt.scatter(*start, marker='o', s=10, c='red')
        if end==None:
            plt.scatter(*point, marker='o', s=10, c='blue')
        else:
            plt.scatter(*end, marker='o', s=10, c='blue')
