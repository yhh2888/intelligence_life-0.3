import pygame, os
import random, time
from time import perf_counter
from Characters import *
import numpy as np
from Entity import Entity

class Board:
    def __init__(self, boardsize=(30, 30), tilesize=30, start=[25, 25]):
        self.boardsize = boardsize
        self.tilesize = tilesize
        self.screen_width, self.screen_height = self.tilesize*self.boardsize[0], self.tilesize*self.boardsize[1]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)
        self.player = Player(self.screen, 30)
        self.player.x, self.player.y = start
        
    def settings(self,
            grass_group,
            nature_group,
            monster_group,
            movetype = 'keyboard',
            ):

        self.grass_group, self.nature_group, self.monster_group = grass_group, nature_group, monster_group
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.SHOWN)
        
        self.game_over = False
        self.paused = False
        self.middle = [25, 25]
        self.key_cooltime = 0
        self.space_clicked = 0
        self.movetype = movetype
        self.zoom_add = 0

    def run(self, automiddle = True, framedelay=0.03, view_lock = False):
        if not self.game_over:
            t = perf_counter()
            if self.paused == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            self.space_clicked = 0
                    elif event.type == pygame.MOUSEWHEEL:
                        if event.y >= 0 and self.zoom_add < 15:
                            self.zoom_add += 5
                        elif event.y < 0 and -15 < self.zoom_add:
                            self.zoom_add -= 5
                        else :
                            break
                        
                        for i in self.grass_group:
                            i.size = self.tilesize + self.zoom_add
                            i.cimage = pygame.transform.scale(i.image, (i.size*i.pos[2], i.size*i.pos[3]))
                            i.block = i.clip(i.cimage, i.size*i.pos[0], i.size*i.pos[1], i.size, i.size).convert_alpha()
                        for i in self.nature_group:
                            i.size = self.tilesize + self.zoom_add
                            i.cimage = pygame.transform.scale(i.image, (i.size*i.pos[2], i.size*i.pos[3]))
                            i.block = i.clip(i.cimage, i.size*i.pos[0], i.size*i.pos[1], i.size, i.size).convert_alpha()
                        for i in self.monster_group:
                            i.size = self.tilesize + self.zoom_add
                            i.cimage = pygame.transform.scale(i.image, (i.size*i.pos[2], i.size*i.pos[3]))
                            i.block = i.clip(i.cimage, i.size*i.pos[0], i.size*i.pos[1], i.size, i.size).convert_alpha()

                # 캐릭터 이동
                if self.movetype == 'keyboard':
                    self.key_cooltime = max(0, self.key_cooltime-1)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.player.move_left()
                        time.sleep(framedelay)
                        self.key_cooltime = 10
                    if keys[pygame.K_RIGHT]:
                        self.player.move_right()
                        time.sleep(framedelay)
                        self.key_cooltime = 10
                    if keys[pygame.K_UP]:
                        self.player.move_up()
                        time.sleep(framedelay)
                        self.key_cooltime = 10
                    if keys[pygame.K_DOWN]:
                        self.player.move_down()
                        time.sleep(framedelay)
                        self.key_cooltime = 10
                    if keys[pygame.K_SPACE]:
                        if self.space_clicked == 0:
                            self.paused = True
                            self.space_clicked = 1
                    #카메라 캐릭터로 이동
                    if keys[pygame.K_m] or automiddle:
                        self.middle = [self.player.x, self.player.y]
                
                #화면/맵 위치           
                mousepos = pygame.mouse.get_pos()
                x_unit = self.screen_width*0.04
                y_unit = self.screen_height*0.04
                if mousepos[0] > x_unit*23:
                    self.middle[0] += 0.5
                    if mousepos[0] > x_unit*24:
                        self.middle[0] +=0.5
                elif mousepos[0] < x_unit*2:
                    self.middle[0] -= 0.5
                    if mousepos[0] < x_unit*1:
                        self.middle[0] -= 0.5
                if mousepos[1] > y_unit*23:
                    self.middle[1] += 0.5
                    if mousepos[1] > y_unit*24:
                        self.middle[1] += 0.5
                elif mousepos[1] < y_unit*2:
                    self.middle[1] -= 0.5
                    if mousepos[1] < y_unit*1:
                        self.middle[1] -= 0.5 
                # 몬스터 이동과 지형 변화
                '''for i in monster_group:
                    i.rect.x += (random.randint(-1, 0)+random.randint(0, 1))
                    i.rect.y += (random.randint(-1, 0)+random.randint(0, 1))
                    change_grass = int(i.rect.x)*100+int(i.rect.y)'''
                '''if 0 <= change_grass <= 10000:
                        grass_code[change_grass] = [random.randint(0, 2), random.randint(0, 2)]
                        grass_group.sprites()[int(i.rect.x)*100+int(i.rect.y)] \
                        = Entity("grasses_refined.png", int(i.rect.x), int(i.rect.y), pos=[*grass_code[change_grass], 3, 3])'''
                    
                self.draw(view_lock)
                
            else :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.paused = False
    
    def draw(self, view_lock = False):
        # 스프라이트 그리기
        if view_lock == False:
            self.screen.fill((255, 255, 255))
            
            for i in self.grass_group:
                self.middle_to_hero = [i.rect.x-self.middle[0], i.rect.y-self.middle[1]]
                self.screen.blit(i.block, ((self.middle_to_hero[0]+self.boardsize[0]/2)*(self.tilesize)+(self.middle_to_hero[0])*self.zoom_add,
                                           (self.middle_to_hero[1]+self.boardsize[1]/2)*(self.tilesize)+(self.middle_to_hero[1])*self.zoom_add))
                    
            for i in self.nature_group:
                self.screen.blit(i.block, ((i.rect.x-self.middle[0]+self.boardsize[0]/2)*(self.tilesize)+(i.rect.x-self.middle[0])*self.zoom_add,
                                           (i.rect.y-self.middle[1]+self.boardsize[1]/2)*(self.tilesize)+(i.rect.y-self.middle[1])*self.zoom_add))
                
            self.screen.blit(self.player.block, ((self.player.x-self.middle[0]+self.boardsize[0]/2)*(self.tilesize),
                                              (self.player.y-self.middle[1]+self.boardsize[1]/2)*(self.tilesize)))
            for i in self.monster_group:
                self.screen.blit(i.block, ((i.rect.x-self.middle[0]+self.boardsize[0]/2)*(self.tilesize)+(i.rect.x-self.middle[0])*self.zoom_add,
                                           (i.rect.y-self.middle[1]+self.boardsize[1]/2)*(self.tilesize)+(i.rect.y-self.middle[1])*self.zoom_add))
            pygame.display.update()

if __name__ == '__main__':
    A = Board()
    size_out = 30

    player_sprite = Entity("squirtle.png", 25, 25)

    grass_group = pygame.sprite.Group()
    grass_code = [[random.randint(0, 2), random.randint(0, 2)] for i in range(10000)]
    for i in range(100):
        for j in range(100):
            grass_group.add(Entity("grasses_refined.png", i, j, pos=[*grass_code[i*100+j], 3, 3]))

    nature_group = pygame.sprite.Group()
    stone = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'stone.png'), (size_out, size_out))
    stone = player_sprite.clip(stone, size_out*0, size_out*0, size_out, size_out)

    stump = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'stump.png'), (size_out, size_out))
    stump = player_sprite.clip(stump, size_out*0, size_out*0, size_out, size_out)

    grass_2 = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'grass_2.png'), (size_out, size_out))
    grass_2 = player_sprite.clip(grass_2, size_out*0, size_out*0, size_out, size_out)

    grass_3 = pygame.transform.scale(pygame.image.load(os.getcwd()+'\\'+'resources\\'+'grass_3.png'), (size_out, size_out))
    grass_3 = player_sprite.clip(grass_2, size_out*0, size_out*0, size_out, size_out)

    for i in range(20):
        nature_group.add(Entity("stone.png", random.randint(0, 99), random.randint(0, 99), pos=[0, 0, 1, 1]))
        nature_group.add(Entity("stump.png", random.randint(0, 99), random.randint(0, 99), pos=[0, 0, 1, 1]))
        nature_group.add(Entity("grass_2.png", random.randint(0, 99), random.randint(0, 99), pos=[0, 0, 0.9, 0.9]))
        nature_group.add(Entity("grass_3.png", random.randint(0, 99), random.randint(0, 99), pos=[0, 0, 0.9, 0.9]))

    monster_group = Mob1(A.screen, A.player, A.tilesize)

    A.settings(grass_group, nature_group, monster_group)
    pygame.init()
    pygame.display.set_caption("Monster game")
    while not A.game_over:
        A.run()
    pygame.quit()
