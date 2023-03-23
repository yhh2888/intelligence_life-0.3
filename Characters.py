import pygame
from pygame.locals import *
import random, os, sys

class Player:
    def __init__(self, surface, size):
        self.parent_screen = surface
        self.img = pygame.image.load(os.getcwd()+'\\'+'resources\\porygon.png')
        self.size = size
        self.img = pygame.transform.scale(self.img, (self.size*2*4, self.size*2*4))
        self.x = 10
        self.y = 10
        self.direc = 'left'
        self.att = []
        self.block = self.clip(self.img, self.size*2*0, self.size*2*0, self.size*2, self.size*2)
        self.attack_real = False
        self.move_score_x = 0
        self.move_score_y = 0
        self.pre_location = []
        self.view_lock == False
        self.tile_loc = [(i*7, j*7) for j in range(4) for i in range(4)]
        self.ground = pygame.image.load(os.getcwd()+'\\'+'resources\\grass.png')
        
    def move_left(self):
        self.move_score_x -= 1
        self.direc = 'left'
        if self.move_score_x <= -2:
            self.pre_location = [self.x, self.y]
            self.x -= 1
            self.block = self.clip(self.img, self.size*2*0, self.size*2*1, self.size*2, self.size*2)
            if self.view_lock == False:
                self.draw()
            self.move_score_x = 0
        
        
    def move_right(self):
        self.move_score_x += 1
        self.direc = 'right'
        if self.move_score_x >= 2:
            self.pre_location = [self.x, self.y]
            self.x += 1
            self.block = self.clip(self.img, self.size*2*0, self.size*2*2, self.size*2, self.size*2)
            if self.view_lock == False:
                self.draw()
            self.move_score_x = 0
        
        
    def move_up(self):
        self.move_score_y -= 1
        self.direc = 'up'
        if self.move_score_y <= -2:
            self.pre_location = [self.x, self.y]
            self.y -= 1
            self.block = self.clip(self.img, self.size*2*0, self.size*2*3, self.size*2, self.size*2)
            if self.view_lock == False:
                self.draw()
            self.move_score_y = 0
        
    def move_down(self):
        self.move_score_y += 1
        self.direc = 'down'
        if self.move_score_y >= 2:
            self.pre_location = [self.x, self.y]
            self.y += 1
            self.block = self.clip(self.img, self.size*2*0, self.size*2*0, self.size*2, self.size*2)
            if self.view_lock == False:
                self.draw()
            self.move_score_y = 0
            
    def view_lock(self):
        if self.view_lock == False:
            view_lock = True
        elif self.view_lock == True:
            view_lock = False
            
    def move_code(self, direction):
        if direction == 'left':
            self.move_left()
        if direction == 'right':
            self.move_right()
        if direction == 'up':
            self.move_up()
        if direction == 'down':
            self.move_down()
        if direction == 'stop':
            self.stopping()
            
    def stopping(self):
        self.eff_times()
        if self.view_lock == False:
            self.draw()

    def draw(self):
        if self.att != [] and self.att[-1] > 7:
            for co_ord in self.att[0:-1]:
                pygame.draw.rect(self.parent_screen, (240, 100, 100),
                                [co_ord[0]*self.size, co_ord[1]*self.size, self.size, self.size])
        else :
            for co_ord in self.att[0:-1]:
                self.parent_screen.blit(self.ground, ((co_ord[0])*self.size, (co_ord[1])*self.size),
                                        pygame.Rect(*self.tile_loc[[3, 5, 10, 11, 15][random.randint(0, 4)]], self.size, self.size))
            self.attack_real = False
        self.pre_loc_fill()
        self.parent_screen.blit(self.block, (self.x*self.size, self.y*self.size))
        pygame.display.flip()

    def pre_loc_fill(self):
        if len(self.pre_location) == 2:
            for i in range(2):
                for j in range(2):
                    self.parent_screen.blit(self.ground, ((self.pre_location[0]+i)*self.size, (self.pre_location[1]+j)*self.size),
                                            pygame.Rect(*self.tile_loc[[3, 5, 10, 11, 15][random.randint(0, 4)]], self.size, self.size))
            self.pre_location = []
        
    def eff_times(self):
        if self.att != []:
            if self.att[-1] > 0:
                self.att[-1] -= 1
            elif self.att[-1] == 0:
                self.att = []

    def attack(self):
        self.cool_time = 10
        if self.direc == 'left':
            self.att = [[(self.x-2+j), (self.y-1+i)] for i in range(3) for j in range(2)]
        if self.direc == 'right':
            self.att = [[(self.x+1+j), (self.y-1+i)] for i in range(3) for j in range(2)]
        if self.direc == 'up':
            self.att = [[(self.x-1+j), (self.y-2+i)] for i in range(2) for j in range(3)]
        if self.direc == 'down':
            self.att = [[(self.x-1+j), (self.y+1+i)] for i in range(2) for j in range(3)]
        self.attack_real = True
        self.att.append(self.cool_time)
        if self.view_lock == False:
            self.draw()
        pygame.display.flip()

    def clip(self, surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clipRect = pygame.Rect(x,y,x_size,y_size)
        handle_surface.set_clip(clipRect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()

class Mob1:
    def __init__(self, surface, follow, size):
        self.parent_screen = surface
        self.img = pygame.image.load("resources/mobs.jpg").convert()
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.size = size
        self.follow = follow
        self.moblist = []
        self.block = self.img
        self.color = (50, 200, 100)
        self.tile_loc = [(i*7, j*7) for j in range(4) for i in range(4)]
        self.ground = pygame.image.load(os.getcwd()+'\\'+'resources\\grass.png')
        
    def mobappend(self, x, y):
        self.moblist.append([x, y, 3])
    
    def distance_cal(self):
        moblist = [a[0:2] for a in self.moblist]
        self.pre_location = []
        for i in range(len(moblist)):
            self.pre_location.append([self.moblist[i][0], self.moblist[i][1]])
            self.amob_distance = [self.follow.x-self.moblist[i][0], self.follow.y-self.moblist[i][1]]

            if abs(self.amob_distance[0]) > abs(self.amob_distance[1]):
                nowmob = moblist[i]
                if self.amob_distance[0] > 0:
                    if [nowmob[0]+1, nowmob[1]] not in moblist:
                        self.moblist[i][0] += 1
                elif self.amob_distance[0] < 0:
                    if [nowmob[0]-1, nowmob[1]] not in moblist:
                        self.moblist[i][0] -= 1

            elif abs(self.amob_distance[1]) > abs(self.amob_distance[0]):
                nowmob = self.moblist[i]
                if self.amob_distance[1] > 0:
                    if [nowmob[0], nowmob[1]+1] not in moblist:
                        self.moblist[i][1] += 1
                elif self.amob_distance[1] < 0:
                    if [nowmob[0], nowmob[1]-1] not in moblist:
                        self.moblist[i][1] -= 1
                
            else:
                rand = random.randint(0, 1)
                if self.amob_distance[rand] > 0:
                    self.moblist[i][rand] += 1
                elif self.amob_distance[rand] < 0:
                    self.moblist[i][rand] -= 1

    def draw(self):
        for amob in range(len(self.moblist)):
            if self.moblist[amob][2] == 3:
                self.color = (50, 200, 100)
            if self.moblist[amob][2] == 2:
                self.color = (30, 140, 60)
            if self.moblist[amob][2] == 1:
                self.color = (10, 60, 20)
            if self.pre_location != [] and len(self.pre_location) >= amob+1:
                self.parent_screen.blit(self.ground, (self.pre_location[amob][0]*self.size, self.pre_location[amob][1]*self.size),
                                              pygame.Rect(*self.tile_loc[[3, 5, 10, 11, 15][random.randint(0, 4)]], self.size, self.size))
            pygame.draw.rect(self.parent_screen, self.color,
                                [self.moblist[amob][0]*self.size, self.moblist[amob][1]*self.size, self.size, self.size])      
        pygame.display.flip()
