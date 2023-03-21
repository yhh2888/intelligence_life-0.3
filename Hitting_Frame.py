# Make it all object oriented by converting the code in various classes

import pygame, sys, os
import random, time
import numpy as np
import torch, json

from pygame.locals import *
from Characters import *
from geometry.calculation import *
from geometry.default_functions import *
from base.kde_temp import *
from base.bp_temp import *
from base.temp2 import NeuralNetwork
from base.feature_analysis import labeler, distances, directions, get_matrix, cross_dir

import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open(os.getcwd()+r'\base\featured_matrix\featurematrixes.json') as f:
    fm = json.load(f)

class Game:
    def __init__(self, start_x, start_y):
        pygame.init()
        self.display_width = [800, 800]
        self.surface = pygame.display.set_mode((self.display_width[0], self.display_width[1]))
        self.size = 8
        self.snake = Snake(self.surface, self.size)
        self.snake.draw()
        self.mobspawn = 0
        self.mobs = Mob1(self.surface, self.snake, self.size)
        self.turns = 0
        self.start_x = start_x
        self.start_y = start_y
        self.kills = 0

    def hit(self):
        score = 0
        for i in self.mobs.moblist:
            if i[0:2] in self.snake.att and self.snake.attack_real == True:
                if i[2] > 1:
                    self.mobs.moblist[self.mobs.moblist.index(i)][2] -= 1
                    score += 50*(2**self.kills)
                else:
                    self.mobs.moblist.remove(i)
                    score += 200*(3**self.kills)
                    self.kills += 1
        return score
                
    def regame(self):
        regame = True
        while regame:
            self.surface.fill((240, 240, 240))
            time.sleep(0.1)
                    
            keys = pygame.key.get_pressed()
            
            if (keys[pygame.K_r]):
                regame = False
            if (keys[pygame.K_ESCAPE]):
                regame = False

    '''def networkfeed(self, view):
        if 'nn' in dir(self):
            max_dir = np.argmax(self.nn.update(view))
            max_value = max(self.nn.update(view))
            if 0<=max_dir<=3 and max_value>0.13:
                return ['right', 'down', 'left', 'up'][max_dir]'''
                
                    
    def run(self):
        self.snake.x = self.start_x
        self.snake.y = self.start_y
        self.surface.fill((240, 240, 240))
        running = True
        self.eventer_time = 0
        self.killscore = 0
        self.movedata = []
        while running:
            #time_per1 = time.time()
            self.eventer_time += 1
            time.sleep(0.04)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if abs(self.snake.move_score_x) == 1:
                        self.snake.pre_location = [self.snake.x, self.snake.y]
                        self.snake.x += self.snake.move_score_x
                        self.snake.move_score_x = 0
                        self.snake.pre_loc_fill()
                    if abs(self.snake.move_score_y) == 1:
                        self.snake.pre_location = [self.snake.x, self.snake.y]
                        self.snake.y += self.snake.move_score_y
                        self.snake.move_score_y = 0
                        self.snake.pre_loc_fill()
                        
            keys = pygame.key.get_pressed()
            buttoned = False
            
            if (keys[pygame.K_LEFT]):
                self.snake.move_left()
                buttoned = True
                self.snake.pre_loc_fill()
                self.movedata.append('left')
                
            if (keys[pygame.K_RIGHT]):
                self.snake.move_right()
                buttoned = True
                self.snake.pre_loc_fill()
                self.movedata.append('right')
                
            if (keys[pygame.K_UP]):
                self.snake.move_up()
                buttoned = True
                self.snake.pre_loc_fill()
                self.movedata.append('up')

            if (keys[pygame.K_DOWN]):
                self.snake.move_down()
                buttoned = True
                self.snake.pre_loc_fill()
                self.movedata.append('down')
                            
            if (keys[pygame.K_SPACE]):
                if self.snake.att == []:
                    self.snake.attack()
                    self.killscore += self.hit()
                    self.movedata.append('space')
                                
            if (keys[pygame.K_s]):
                self.snake.stopping()
                self.movedata.append('stop')

            if (keys[pygame.K_ESCAPE]):
                running = False
                
            if self.eventer_time > 8:
                self.mobspawn += 1
                if self.mobspawn > 10:
                    if random.randint(0, 3) == 0:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size), 0)
                    elif random.randint(0, 3) == 1:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size),
                                            self.display_width[1]/self.snake.size)
                    elif random.randint(0, 3) == 2:
                        self.mobs.mobappend(0, random.randint(0, self.display_width[1]/self.snake.size))
                    elif random.randint(0, 3) == 3:
                        self.mobs.mobappend(self.display_width[0]/self.snake.size,
                                            random.randint(0,self.display_width[0]/self.snake.size))
                    self.mobspawn = 0
                self.turns += 1
                
                for j in range(6-int(self.display_width[1]/self.size-self.snake.y)):
                    vision[10-j][i] = 1
                vision_print_on = True
            if vision_print_on and buttoned:
                '''print(vision)'''
                vision_print_on = False
                
            #time_per1 = time.time()
            
            if self.mobs != None:
                self.snake.draw()
                self.mobs.draw()
                self.snake.eff_times()
                if self.eventer_time > 8 and self.turns%2 == 0:
                    self.mobs.distance_cal()
                    self.eventer_time = 0
            if [self.snake.x, self.snake.y] in [i[0:2] for i in self.mobs.moblist] or (not 0<=self.snake.x<=self.display_width[0]/self.size) or (not 0<=self.snake.y<=self.display_width[1]/self.size):
                running = False
                pygame.quit()
                return self.movedata
                    
                                
            #print(time_per1-time.time())       

    def run_by_AI(self, view_lock = False, net=None):
        
        sew = 0
        wait = 0
        
        self.snake.x = self.start_x
        self.snake.y = self.start_y
        self.surface.fill((240, 240, 240))
        running = True
        self.eventer_time = 0
        self.key_value = ['space', 'up', 'down', 'right', 'left', 'stop']
        vision = np.zeros((11, 11))
        self.killscore = 0
        self.snake.view_lock = view_lock
        Exceptor = None
        supervise = []

        #----initial----
        sightrange = 11
        sighthalf = int((sightrange-1)/2)
        mapkde = spreader(typ=[], mrec_disp=False)
        mapkde.test_data = [[100, 0], [0, 100], [0, 0], [100, 100]]
        mapkde.Xmg, mapkde.Ymg = np.mgrid[0:100:100j, 0:100:100j]
        kdeval = mapkde.kde_set(mapkde.test_data)
        mapkde.Z = mapkde.kde_distribution(*kdeval, 0.15, 1) + mapkde.kde_distribution(*kdeval, 0.15, 0.8)
        sightkde = [mapkde.Z[self.snake.x-sighthalf+i][self.snake.y-sighthalf+j]
                        for i in range(-sighthalf, sighthalf+1) for j in range(-sighthalf, sighthalf+1)]

        maf_dic = {}

        dist_3 = [torch.tensor([0]) for i in range(3)]
        dir_3 = [torch.tensor([0]) for i in range(3)]
        ismoving_3 = [torch.tensor([0]) for i in range(5)]
        #maf_3 = [torch.tensor([torch.tensor([0]) for m in range(14)]) for m in range(3)]
        cdir_3 = [torch.tensor([0]) for i in range(3)]
        mat_3 = [torch.tensor([0 for i in range(121)]) for m in range(3)]
        move_3 = [torch.tensor([0]) for i in range(3)]

        fnlist = ['dist_3', 'dir_3', 'ismoving_3', 'cdir_3', 'move_3', 'mat_3']

        dist_now, dir_now, ismoving_now,  cdir_now, mat_now, move_now = [[None]]*6
        
        '''maf_now,'''
        
        netmodel = net
        netresult = torch.tensor([0])
        
        while running:
            time_per1 = time.time()
            self.eventer_time += 1
            '''vision = np.zeros((11, 11))
            realmob = []'''

            # vision page --------------------------------------------------------------------------------------
            
            '''for i in self.mobs.moblist:
                if abs(self.snake.x-i[0]) <= 5 and abs(self.snake.y-i[1]) <= 5:
                    vision[5-(int(self.snake.y)-int(i[1]))][5-(int(self.snake.x)-int(i[0]))] += i[2]
                    self.killscore += 1
                    realmob.append(i[0:2])
                if self.snake.x-6 < 0:
                    for i in range(11):
                        for j in range(6-int(self.snake.x)-1):
                            vision[i][j] = 1
                if self.snake.x+6 > self.display_width[0]/self.size:
                    for i in range(11):
                        for j in range(6-int(self.display_width[0]/self.size-self.snake.x)):
                            vision[i][10-j] = 1
                if self.snake.y-6 < 0:
                    for i in range(11):
                        for j in range(6-int(self.snake.y)-1):
                            vision[j][i] = 1
                if self.snake.y+6 > self.display_width[1]/self.size:
                    for i in range(11):
                        for j in range(6-int(self.display_width[1]/self.size-self.snake.y)):
                            vision[10-j][i] = 1'''

            # moverule page --------------------------------------------------------------------------------------
        
            values = []
            mobxys = [i[0:2] for i in self.mobs.moblist]
            contemp = None
            avoidloc = movepoint([self.snake.x, self.snake.y], mobxys, self.display_width[0]/self.size, 3)

            
            movedir = [0,0,0,0]
            if avoidloc == None:
                pass
                #avoidloc = avoider(self.mobs.moblist, 20, 10, [self.snake.x, self.snake.y])
            elif avoidloc != None:
                nearest = distance_response(distance(mobxys, [self.snake.x, self.snake.y])).nearest_response(mobxys)[0]
                avoidaim = [self.snake.x+avoidloc[0], self.snake.y+avoidloc[1]]
                if abs(avoidaim[0]-nearest[0]) == 2 and abs(avoidaim[1]-nearest[1]) == 2:
                    randomxy = random.randint(0, 1)
                    avoidloc[randomxy] += nearest[randomxy]-avoidaim[randomxy]
                contemp = None
                if avoidloc[0] > 0:
                    xdir = 1
                elif avoidloc[0] < 0:
                    xdir = -1
                else :
                    xdir = 0
                if avoidloc[1] > 0:
                    ydir = 1
                elif avoidloc[1] < 0:
                    ydir = -1
                else :
                    ydir = 0
                    
                pluslist = [[xdir, 0], [0, ydir]][random.randint(0, 1)]
                avoidloc = [avoidloc[0]-pluslist[0], avoidloc[1]-pluslist[1]]
                
                if netresult == 0:
                    self.snake.move_code('right')
                    movedir = [1, 0, 0, 0]
                elif netresult == 2:
                    self.snake.move_code('left')
                    movedir = [0, 0, 1, 0]
                elif netresult == 1:
                    self.snake.move_code('down')
                    movedir = [0, 1, 0, 0]
                elif netresult == 3:
                    self.snake.move_code('up')
                    movedir = [0, 0, 0, 1]
                if avoidloc == [0, 0]:
                    avoidloc = None
            '''if 'data' in locals():
                feed = self.networkfeed(data[0][0])
                if feed != None:
                    self.snake.move_code(feed)'''
            

            # attack page --------------------------------------------------------------------------------------
            
            if self.snake.direc == 'left':
                sides = [[(self.snake.x-2+j), (self.snake.y-1+i)] for i in range(3) for j in range(2)]
            if self.snake.direc == 'right':
                sides = [[(self.snake.x+1+j), (self.snake.y-1+i)] for i in range(3) for j in range(2)]
            if self.snake.direc == 'up':
                sides = [[(self.snake.x-1+j), (self.snake.y-2+i)] for i in range(2) for j in range(3)]
            if self.snake.direc == 'down':
                sides = [[(self.snake.x-1+j), (self.snake.y+1+i)] for i in range(2) for j in range(3)]
            for i in self.mobs.moblist:
                if i[0:2] in sides and self.snake.att == []:
                    self.snake.attack()
                    self.killscore += self.hit()
                    break
            
            if contemp in self.key_value[1:6]:
                self.snake.move_code(contemp)
                
            if contemp == 'space':
                if self.snake.att == []:
                    self.snake.attack()
                    self.killscore += self.hit()
                    
            # time page --------------------------------------------------------------------------------------
            
            if self.eventer_time > 8:
                if avoidloc != None:
                    supervise.append([[self.snake.x, self.snake.y], mobxys, avoidloc])
                self.mobspawn += 1
                if self.mobspawn > random.randint(8, 15):
                    randnum = random.randint(0, 3)
                    if randnum == 0:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size), 0)
                    elif randnum == 1:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size),
                                            self.display_width[1]/self.snake.size)
                    elif randnum == 2:
                        self.mobs.mobappend(0, random.randint(0, self.display_width[1]/self.snake.size))
                    elif randnum == 3:
                        self.mobs.mobappend(self.display_width[0]/self.snake.size,
                                            random.randint(0,self.display_width[0]/self.snake.size))
                    self.mobspawn = 0
                self.turns += 3

            # last page --------------------------------------------------------------------------------------
                        
            #time_per1 = time.time()
            if self.mobs != None:
                self.snake.eff_times()
                if self.snake.view_lock == False:
                    self.snake.draw()
                    self.mobs.draw()
                if self.eventer_time > 8 and self.turns%2 == 0:
                    self.mobs.distance_cal()
                    self.eventer_time = 0
                    #plt.imshow(mapkde.Z, cmap=plt.cm.gist_earth_r, extent=[0, 100, 0, 100])
                    #plt.show()
                    
                    '''wait += 1
                    
                    if sew > 10 and wait > 30:
                        print(mobxys)
                        plt.imshow(np.array(sightkde).reshape(11, 11)[::-1], cmap=plt.cm.gist_earth_r, extent=[self.snake.x-5, self.snake.x+6, self.snake.y-5, self.snake.y+6])
                        plt.show()                        
                        plt.imshow(np.array([round(mapkde.Z[i][j], 4) for i in range(len(mapkde.Z)) for j in range(len(mapkde.Z[0]))]).reshape(len(mapkde.Z), len(mapkde.Z[0])),
                                   cmap=plt.cm.gist_earth_r, extent=[0, 100, 0, 100])
                        plt.scatter(self.snake.x, self.snake.y, marker='o')
                        plt.show()
                        
                        
                        sew = 0
                    sew += 1'''
            
            mapkde.test_data = mobxys+[[100, 0], [0, 100], [0, 0], [100, 100]]
            
            kdeval = mapkde.kde_set(mapkde.test_data)
            mapkde.Z = mapkde.kde_distribution(*kdeval, 0.03, 30) + mapkde.kde_distribution(*kdeval, 0.1, 0.5)
            self.snake.x, self.snake.y = 99-self.snake.y, self.snake.x
            try:
                sightkde = [round(mapkde.Z[i][j], 4) for i in range(self.snake.x-sighthalf, self.snake.x+sighthalf+1) for j in range(self.snake.y-sighthalf, self.snake.y+sighthalf+1)]
            except Exception:
                sigthkde = [0 for i in range(121)]
            data = [[sightkde, [movedir if contemp!='space' else [0,0,0,0]][0]+[1 if contemp=='space' else 0]]]
            #---------- feature setting page ----------#
            mat_sight = torch.tensor(sightkde).reshape(11, 11)
            
            dist_now = [labeler(mat_sight, ['distances', 'maindist'])]
            dir_now = [labeler(mat_sight, ['directions', 'main'])]
            if dist_now[0] != None:
                ismoving_now = [1 if netresult == 5 else 0]
                #maf_now = [torch.tensor(labeler(mat_sight,
                #           ['matrix_feature_', 'tensor', torch.tensor(get_matrix(fm[maf_dic[m]][0]))])) for m in list(maf_dic.keys())]
                cdir_now = [labeler(mat_sight, ['cross_dir', 'main'])]
                mat_now = torch.tensor(sightkde)
                move_now = torch.tensor([netresult])
            #---------- feature memory page ----------#

            if dist_now[0] != None:
                for n in fnlist:
                    del locals()[n][0]
                    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
            #---------- final feature ----------#
            if dist_now[0] != None:
                fin_feature = torch.tensor([torch.Tensor.tolist((torch.cat((*locals()[fnlist[0]], *locals()[fnlist[1]], *locals()[fnlist[2]],
                                                                        *locals()[fnlist[3]], *locals()[fnlist[4]], *locals()[fnlist[5]]
                                                                           ))
                                                                ))
                                           ])

                netresult = torch.argmax(netmodel(fin_feature))
                    
            self.snake.x, self.snake.y = self.snake.y, 99-self.snake.x
            
            
            
            if [self.snake.x, self.snake.y] in [i[0:2] for i in self.mobs.moblist] \
                or (not 6<=self.snake.x<=self.display_width[0]/self.size-6) \
                or (not 6<=self.snake.y<=self.display_width[1]/self.size-6):
                running = False
                
                pygame.init()
                #print(supervise)
                print(self.turns, self.killscore)
                return self.turns+self.killscore
            
            #print(time_per1-time.time())
            
            
if __name__ == '__main__':
    game = Game(20, 20)
    game.run()
    pygame.quit()
