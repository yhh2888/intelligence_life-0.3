# Make it all object oriented by converting the code in various classes

import pygame, sys, os
import random, time
import numpy as np
import torch, json, traceback
from numba import jit

from torch import nn
from torch.optim.lr_scheduler import ExponentialLR
from torch.utils.data import DataLoader
from time import perf_counter

from pygame.locals import *
from Characters import *
from geometry.calculation import *
from geometry.default_functions import *
from base.kde_temp import *
from base.bp_temp import *
from base.network import NeuralNetwork, structure_set
from base.feature_analysis import labeler, distances, directions, get_matrix, cross_dir
from tempgame import Entity, Board

import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open(os.getcwd()+r'\base\featured_matrix\featurematrixes.json') as f:
    fm = json.load(f)

class Game:
    def __init__(self, start_x, start_y):
        pygame.init()
        self.mapwidth = [30, 30]
        self.size = 30
        self.start_x = start_x
        self.start_y = start_y
        self.display_width = [self.mapwidth[0]*self.size, self.mapwidth[1]*self.size]
        self.board = Board(self.mapwidth, self.size, [self.start_x, self.start_y])
        self.player = self.board.player
        self.mobspawn = 0
        self.mobs = Mob1(self.board.screen, self.player, self.size)
        self.turns = 0
        self.kills = 0
        
        self.term_data = []
        self.quit = False

    def hit(self):
        score = 0
        for i in self.mobs.moblist:
            if i[0:2] in self.player.att and self.player.attack_real == True:
                if i[2] > 1:
                    self.mobs.moblist[self.mobs.moblist.index(i)][2] -= 1
                    self.player.lifes += 1
                else:
                    self.mobs.moblist.remove(i)
                    score += 100
                    self.kills += 1
                    self.player.lifes += 2
        return score
                
    def regame(self):
        regame = True
        while regame:
            self.board.screen.fill((240, 240, 240))
            time.sleep(0.1)
                    
            keys = pygame.key.get_pressed()
            
            if (keys[pygame.K_r]):
                regame = False
            if (keys[pygame.K_ESCAPE]):
                regame = False
    
    def clip(self, surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clipRect = pygame.Rect(x,y,x_size,y_size)
        handle_surface.set_clip(clipRect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()   

    def run_by_AI(self, view_lock = False, net=None, time_=False):
        sew = 0
        wait = 0
        self.board.screen.fill((240, 240, 240))
        running = True
        self.eventer_time = 0
        self.key_value = ['space', 'up', 'down', 'right', 'left', 'stop']
        vision = np.zeros((11, 11))
        self.killscore = 0
        Exceptor = None
        supervise = []
        
        self.player.lifes = 10
        self.player.view_lock = view_lock

        #----initial----
        sightrange = 11
        sighthalf = int((sightrange-1)/2)
        mapkde = spreader(typ=[], mrec_disp=False)
        mapkde.test_data = [[100, 0], [0, 100], [0, 0], [100, 100]]
        mapkde.Xmg, mapkde.Ymg = np.mgrid[0:100:100j, 0:100:100j]
        kdeval = mapkde.kde_set(mapkde.test_data)
        mapkde.Z = mapkde.kde_distribution(*kdeval, 0.15, 1) + mapkde.kde_distribution(*kdeval, 0.15, 0.8)
        sightkde = [mapkde.Z[self.player.x-sighthalf+i][self.player.y-sighthalf+j]
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
        
        self.netmodel = net
        self.netmodel.optim = torch.optim.Adam(self.netmodel.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
        self.netmodel.sched = ExponentialLR(self.netmodel.optim, gamma=0.9)
        loss_fn = nn.CrossEntropyLoss()
    
        netresult = torch.tensor([0])
        oscillater = 0
        
        tile_loc = [(i*7, j*7) for j in range(4) for i in range(4)]
        
        netresult_time = 0

        self.healthbarimg = pygame.image.load(os.getcwd()+'\\'+'resources\\healthbar.png').convert()
        self.healthbarimg = pygame.transform.scale(self.healthbarimg, (988/8, 3392/8))

        grass_group = pygame.sprite.Group()
        grass_code = [[random.randint(0, 2), random.randint(0, 2)] for i in range(10000)]
        for i in range(100):
            for j in range(100):
                grass_group.add(Entity("grasses_refined.png", i, j, pos=[*grass_code[i*100+j], 3, 3]))

        player_sprite = Entity("squirtle.png", 25, 25)
        size_out = 30
        
        nature_group = pygame.sprite.Group()
        '''stone = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'stone.png'), (size_out, size_out))
        stone = player_sprite.clip(stone, size_out*0, size_out*0, size_out, size_out)

        stump = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'stump.png'), (size_out, size_out))
        stump = player_sprite.clip(stump, size_out*0, size_out*0, size_out, size_out)

        grass_2 = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'grass_2.png'), (size_out, size_out))
        grass_2 = player_sprite.clip(grass_2, size_out*0, size_out*0, size_out, size_out)

        grass_3 = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'grass_3.png'), (size_out, size_out))
        grass_3 = player_sprite.clip(grass_2, size_out*0, size_out*0, size_out, size_out)'''
        
        monster_group = self.mobs
        
        self.board.settings(grass_group, nature_group, monster_group)

        self.chunks = {}

        self.netmodel.received_data = []
        
        while running:
            if time_==True and dist_now[0] != None:
                t = perf_counter()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                    self.quit = True
                    
            self.eventer_time += 1
            '''vision = np.zeros((11, 11))
            realmob = []'''

            # vision page --------------------------------------------------------------------------------------

            if self.player.view_lock == False:
                x_lbound, x_lchunk = int(self.board.middle[0]-self.board.boardsize[0]/2), int(self.board.middle[0]-self.board.boardsize[0]/2)//16
                y_ubound, y_uchunk = int(self.board.middle[1]-self.board.boardsize[1]/2), int(self.board.middle[1]-self.board.boardsize[1]/2)//16
                x_rbound, x_rchunk = int(self.board.middle[0]+self.board.boardsize[0]/2), int(self.board.middle[0]+self.board.boardsize[0]/2)//16
                y_dbound, y_dchunk = int(self.board.middle[1]+self.board.boardsize[1]/2), int(self.board.middle[1]+self.board.boardsize[1]/2)//16
                print(x_lbound, x_lchunk, y_ubound, y_uchunk, x_rbound, x_rchunk, y_dbound, y_dchunk)

                chunk_now = [[i, j] for i in range(x_lchunk, x_rchunk+1) for j in range(y_uchunk, y_dchunk+1)]
                tiles_now = {}
                
                for i in chunk_now:
                    if str(i) in self.chunks.keys():
                        tiles_now[str(i)] = self.chunks[str(i)]
                    else :
                        self.chunks[str(i)] = np.array([[[random.randint(0, 2), random.randint(0, 2)] for i in range(16)] for j in range(16)])

                
                complete_tile = np.concatenate(([np.concatenate(([self.chunks[str([i, j])] for j in range(y_uchunk, y_dchunk+1)]), axis=0) for i in range(x_lchunk, x_rchunk+1)]), axis=1)

                self.board.grass_group = pygame.sprite.Group()
                for i in range(len(complete_tile)):
                    for j in range(len(complete_tile[i])):
                        self.board.grass_group.add(Entity("grasses_refined.png", x_lchunk*16+j, y_uchunk*16+i, pos=[*complete_tile[i][j], 3, 3]))
                    
            '''for i in self.mobs.moblist:
                if abs(self.player.x-i[0]) <= 5 and abs(self.player.y-i[1]) <= 5:
                    vision[5-(int(self.player.y)-int(i[1]))][5-(int(self.player.x)-int(i[0]))] += i[2]
                    self.killscore += 1
                    realmob.append(i[0:2])
                if self.player.x-6 < 0:
                    for i in range(11):
                        for j in range(6-int(self.player.x)-1):
                            vision[i][j] = 1
                if self.player.x+6 > self.display_width[0]/self.size:
                    for i in range(11):
                        for j in range(6-int(self.display_width[0]/self.size-self.player.x)):
                            vision[i][10-j] = 1
                if self.player.y-6 < 0:
                    for i in range(11):
                        for j in range(6-int(self.player.y)-1):
                            vision[j][i] = 1
                if self.player.y+6 > self.display_width[1]/self.size:
                    for i in range(11):
                        for j in range(6-int(self.display_width[1]/self.size-self.player.y)):
                            vision[10-j][i] = 1'''

            # moverule page --------------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
            values = []
            mobxys = [i[0:2] for i in self.mobs.moblist]
            contemp = None
            avoidloc = movepoint([self.player.x, self.player.y], mobxys, self.display_width[0]/self.size, 3)

            
            movedir = [0,0,0,0]
            virtual_movedir = [0,0,0,0]
            if avoidloc == None:
                avoidloc = avoider(self.mobs.moblist, 20, 10, [self.player.x, self.player.y])
            elif avoidloc != None:
                nearest = distance_response(distance(mobxys, [self.player.x, self.player.y])).nearest_response(mobxys)[0]
                avoidaim = [self.player.x+avoidloc[0], self.player.y+avoidloc[1]]
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
                    
                pluslist = [[xdir, 0], [0, ydir]][oscillater]
                avoidloc = [avoidloc[0]-pluslist[0], avoidloc[1]-pluslist[1]]

                if random.random()>0.5:
                    if oscillater == 0:
                        oscillater = 1
                    elif oscillater == 1:
                        oscillater = 0

                if pluslist == [1, 0]:
                    self.player.move_code('right')
                    virtual_movedir = [1, 0, 0, 0]
                elif pluslist == [-1, 0]:
                    self.player.move_code('left')
                    virtual_movedir = [0, 0, 1, 0]
                elif pluslist == [0, 1]:
                    self.player.move_code('down')
                    virtual_movedir = [0, 1, 0, 0]
                elif pluslist == [0, -1]:
                    self.player.move_code('up')
                    virtual_movedir = [0, 0, 0, 1]
                if avoidloc == []:
                    avoidloc = None
                    
            if netresult == 0:
                #self.player.move_code('right')
                movedir = [1, 0, 0, 0]
            elif netresult == 2:
                #self.player.move_code('left')
                movedir = [0, 0, 1, 0]
            elif netresult == 1:
                #self.player.move_code('down')
                movedir = [0, 1, 0, 0]
            elif netresult == 3:
                #self.player.move_code('up')
                movedir = [0, 0, 0, 1]
            '''if 'data' in locals():
                feed = self.networkfeed(data[0][0])
                if feed != None:
                    self.player.move_code(feed)'''
            
            if time_==True and dist_now[0] != None:
                print('moverule page :', perf_counter()-t)
            
            # attack page --------------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
            if self.player.direc == 'left':
                sides = [[(self.player.x-2+j), (self.player.y-1+i)] for i in range(3) for j in range(2)]
            if self.player.direc == 'right':
                sides = [[(self.player.x+1+j), (self.player.y-1+i)] for i in range(3) for j in range(2)]
            if self.player.direc == 'up':
                sides = [[(self.player.x-1+j), (self.player.y-2+i)] for i in range(2) for j in range(3)]
            if self.player.direc == 'down':
                sides = [[(self.player.x-1+j), (self.player.y+1+i)] for i in range(2) for j in range(3)]
            for i in self.mobs.moblist:
                if i[0:2] in sides and self.player.att == []:
                    self.player.attack()
                    self.killscore += self.hit()
                    break
            
            if contemp in self.key_value[1:6]:
                self.player.move_code(contemp)
                
            if contemp == 'space':
                if self.player.att == []:
                    self.player.attack()
                    self.killscore += self.hit()

            if time_==True and dist_now[0] != None:
                print('attack page :', perf_counter()-t)
                    
            # mob page --------------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
            decision_num = random.randint(25, 100)
            if self.eventer_time > 8:
                if avoidloc != None:
                    supervise.append([[self.player.x, self.player.y], mobxys, avoidloc])
                self.mobspawn += 1
                if self.mobspawn > random.randint(10+decision_num, 20+decision_num):
                    randnum = random.randint(0, 3)
                    if randnum == 0:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.player.size), 0)
                    elif randnum == 1:
                        self.mobs.mobappend(random.randint(0, self.display_width[0]/self.player.size),
                                            self.display_width[1]/self.player.size)
                    elif randnum == 2:
                        self.mobs.mobappend(0, random.randint(0, self.display_width[1]/self.player.size))
                    elif randnum == 3:
                        self.mobs.mobappend(self.display_width[0]/self.player.size,
                                            random.randint(0,self.display_width[0]/self.player.size))
                    self.mobspawn = 0
                self.turns += 3

            if time_==True and dist_now[0] != None:
                print('mob page :', perf_counter()-t)

            # kde generating page ---------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
            mapkde.test_data = mobxys+[[100, 0], [0, 100], [0, 0], [100, 100]]
            
            kdeval = mapkde.kde_set(mapkde.test_data)
            mapkde.Z = mapkde.kde_distribution(*kdeval, 0.03, 30) + mapkde.kde_distribution(*kdeval, 0.1, 0.5)
            self.player.x, self.player.y = 99-self.player.y, self.player.x
            try:
                sightkde = np.round(mapkde.Z[self.player.x-sighthalf:self.player.x+sighthalf+1,
                                            self.player.y-sighthalf:self.player.y+sighthalf+1], 4).reshape(1, sightrange**2)[0].tolist()
            except Exception as e:
                print(e, traceback.format_exc())
                sigthkde = [0]*(sightrange**2)
            data = [[sightkde, [virtual_movedir if contemp!='space' else [0,0,0,0]][0]+[1 if contemp=='space' else 0]]]

            data = [i[0:2] for i in self.mobs.moblist]
            self.player.x, self.player.y = self.player.y, 99-self.player.x
            data = data+[[self.player.x, self.player.y]]

            if time_==True and dist_now[0] != None:
                print('kde generating page :', perf_counter()-t)
            
            #---------- feature setting page ----------#
            '''t = None
            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
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

                netresult = torch.argmax(self.netmodel(fin_feature))
                netresult_time = 30

            netresult_time -= 1
            if netresult_time <= 0:
                netresult = 5
            
            if dist_now[0] != None:
                self.term_data.append((fin_feature, torch.tensor(torch.argmax(torch.tensor(data[0][1])))))

            if time_==True and dist_now[0] != None and t != None:
                print('features page :', perf_counter()-t)'''

            # map boundary deal page ---------------------------------------------------------------------

            '''if time_==True and dist_now[0] != None:
                t = perf_counter()

            if (not 7<=self.player.x<=self.display_width[0]/self.size-7):
                self.player.pre_location = [self.player.x, self.player.y]
                self.player.x = int((abs(self.player.x-(self.display_width[0]/self.size))*14+50)//15)
                if self.player.view_lock == False:
                    self.player.draw()
            elif (not 7<=self.player.y<=self.display_width[1]/self.size-7):
                self.player.pre_location = [self.player.x, self.player.y]
                self.player.y = int((abs(self.player.y-self.display_width[1]/self.size)*14+50)//15)
                if self.player.view_lock == False:
                    self.player.draw()

            if time_==True and dist_now[0] != None:
                print('map boundary deal page :', perf_counter()-t)'''
                    
            # lifes page ---------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter()
            
            if [self.player.x, self.player.y] in [i[0:2] for i in self.mobs.moblist]:
                self.player.lifes -= 3
                
            if self.player.lifes < 0:
                running = False
                
                self.netmodel.feature_label = self.term_data
                print(len(self.term_data))
                self.netmodel.ted = DataLoader(self.netmodel.feature_label[int(len(self.netmodel.feature_label)//1.2):],
                                               batch_size=max(1, (len(self.netmodel.feature_label)-int(len(self.netmodel.feature_label)//1.2))//100))
                self.netmodel.trd = DataLoader(self.netmodel.feature_label[0:int(len(self.netmodel.feature_label)//1.2)],
                                               batch_size=max(1, ((int(len(self.netmodel.feature_label)//1.2)))//100))

                #self.netmodel.roll(7, 3, last = max(100, len(self.term_data)))
                pygame.init()
                print(self.turns, self.killscore)
                return self.turns+self.killscore, self.term_data
            elif self.player.lifes > 10:
                self.player.lifes = 10

            if time_==True and dist_now[0] != None:
                print('lifes page :', perf_counter()-t)

            # draw page ----------------------------------------------------------------------------------

            if time_==True and dist_now[0] != None:
                t = perf_counter(automiddle = False)
            self.board.run(view_lock = self.player.view_lock)
            if self.mobs != None:
                self.player.eff_times()
                if self.player.view_lock == False and not (self.eventer_time > 8 and self.turns%2 == 0):
                    self.player.draw()
                    self.mobs.draw(grassorigin=self.maptiles)
                    self.healthbar = self.clip(self.healthbarimg, 0, (228+288*abs(min(10, max(0, self.player.lifes))-10))/8, 988/8, 269/8)
                    self.board.screen.blit(self.healthbar, (2*self.size, 2*self.size))
                if self.eventer_time > 8 and self.turns%2 == 0:
                    if self.player.view_lock == False:
                        self.player.draw(grass=True)
                        self.mobs.draw(grass=True, grassorigin=self.maptiles)
                        self.healthbar = self.clip(self.healthbarimg, 0, (228+288*abs(min(10, max(0, self.player.lifes))-10))/8, 988/8, 269/8)
                        self.board.screen.blit(self.healthbar, (2*self.size, 2*self.size))
                    
                    if data != []:
                        self.netmodel.received_data.append(data)
                    self.mobs.distance_cal()
                    self.eventer_time = 0
                    
                    '''
                    plt.imshow(mapkde.Z, cmap=plt.cm.gist_earth_r, extent=[0, 100, 0, 100])
                    plt.show()
                    
                    wait += 1
                    
                    if sew > 10 and wait > 30:
                        print(mobxys)
                        plt.imshow(np.array(sightkde).reshape(11, 11)[::-1], cmap=plt.cm.gist_earth_r, extent=[self.player.x-5, self.player.x+6, self.player.y-5, self.player.y+6])
                        plt.show()                        
                        plt.imshow(np.array([round(mapkde.Z[i][j], 4) for i in range(len(mapkde.Z)) for j in range(len(mapkde.Z[0]))]).reshape(len(mapkde.Z), len(mapkde.Z[0])),
                                   cmap=plt.cm.gist_earth_r, extent=[0, 100, 0, 100])
                        plt.scatter(self.player.x, self.player.y, marker='o')
                        plt.show()
                        
                        
                        sew = 0
                    sew += 1
            '''
            if time_==True and dist_now[0] != None:
                print('draw page :', perf_counter()-t)
            
            
if __name__ == '__main__':
    game = Game(20, 20)
    game.run()
    pygame.quit()
