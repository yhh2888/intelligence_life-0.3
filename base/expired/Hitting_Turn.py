# Make it all object oriented by converting the code in various classes

import pygame
from pygame.locals import *
from Mobs import *
import random, time

class Snake:
    def __init__(self, surface, size):
        self.parent_screen = surface
        self.img = pygame.image.load("resources/block.jpg").convert()
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.x = 10
        self.y = 10
        self.size = size
        self.direc = 'left'
        self.att = []
        self.block = self.img
        self.attack_real = False
        
    def move_left(self):
        self.x -= 1
        self.block = pygame.transform.rotate(self.img, 0)
        self.direc = 'left'
        self.eff_times()

        self.draw()
        
        
    def move_right(self):
        self.x += 1
        self.block = pygame.transform.rotate(self.img, 180)
        self.direc = 'right'
        self.eff_times()
        
        self.draw()
        
    def move_up(self):
        self.y -= 1
        self.block = pygame.transform.rotate(self.img, 270)
        self.direc = 'up'
        self.eff_times()

        self.draw()
        
    def move_down(self):
        self.y += 1
        self.block = pygame.transform.rotate(self.img, 90)
        self.direc = 'down'
        self.eff_times()

        self.draw()
        
    def stopping(self):
        self.eff_times()
        self.draw()

    def draw(self):
        self.parent_screen.fill((240, 240, 240))
        if self.att != [] and self.att[-1] > 2:
            for co_ord in self.att[0:-1]:
                pygame.draw.rect(self.parent_screen, (240, 100, 100),
                                [co_ord[0]*self.size, co_ord[1]*self.size, self.size, self.size])
        else :
            self.attack_real = False
        
        self.parent_screen.blit(self.block, (self.x*self.size, self.y*self.size))
        pygame.display.flip()
        
    def eff_times(self):
        if self.att != []:
            if self.att[-1] > 0:
                self.att[-1] -= 1
            elif self.att[-1] == 0:
                self.att = []

    def attack(self):
        cool_time = 3
        if self.direc == 'left':
            self.att = [[(self.x-2+j), (self.y-1+i)] for i in range(3) for j in range(2)]
        if self.direc == 'right':
            self.att = [[(self.x+1+j), (self.y-1+i)] for i in range(3) for j in range(2)]
        if self.direc == 'up':
            self.att = [[(self.x-1+j), (self.y-2+i)] for i in range(2) for j in range(3)]
        if self.direc == 'down':
            self.att = [[(self.x-1+j), (self.y+1+i)] for i in range(2) for j in range(3)]
        self.attack_real = True
        self.att.append(cool_time)
        self.draw()
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.display_width = [800, 800]
        self.surface = pygame.display.set_mode((self.display_width[0], self.display_width[1]))
        self.size = 20
        self.snake = Snake(self.surface, self.size)
        self.snake.draw()
        self.mobspawn = 0
        self.mobs = Mob1(self.surface, self.snake, self.size)
        self.turns = 0

    def hit(self):
        for i in self.mobs.moblist:
            if i[0:2] in self.snake.att and self.snake.attack_real == True:
                if i[2] > 1:
                    self.mobs.moblist[self.mobs.moblist.index(i)][2] -= 1
                else:
                    self.mobs.moblist.remove(i)
                
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                evented = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        evented = True
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        evented = True
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        evented = True

                    if event.key == K_UP:
                        self.snake.move_up()
                        evented = True

                    if event.key == K_DOWN:
                        self.snake.move_down()
                        evented = True
                        
                    if event.key == K_SPACE:
                        if self.snake.att == []:
                            self.snake.attack()
                            evented = True
                            self.hit()
                            
                    if event.key == K_s:
                        self.snake.stopping()
                        evented = True
                elif event.type == QUIT:
                    running = False
                
                if evented == True:
                    self.mobspawn += 1
                    if self.mobspawn > 10:
                        if random.randint(0, 3) == 0:
                            self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size), 0)
                        elif random.randint(0, 3) == 1:
                            self.mobs.mobappend(random.randint(0, self.display_width[0]/self.snake.size), self.display_width[1]/self.snake.size)
                        elif random.randint(0, 3) == 2:                            
                            self.mobs.mobappend(0, random.randint(0, self.display_width[1]/self.snake.size))
                        elif random.randint(0, 3) == 3:
                            self.mobs.mobappend(self.display_width[0]/self.snake.size, random.randint(0, self.display_width[0]/self.snake.size))
                        self.mobspawn -= 10
                    self.turns += 1
                if evented == True and self.mobs != None:
                    self.mobs.draw()
                    if self.turns%2 == 0:
                        self.mobs.distance_cal()
                
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
