import pygame, os
import random, time
from time import perf_counter
import Characters
import numpy as np

class Entity(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size=30, pos=[0, 0, 4, 4], from_path=True):
        super().__init__()
        self.size=size
        if from_path:
            self.image = pygame.image.load(os.getcwd()+'\\'+'resources\\'+image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size*pos[2], self.size*pos[3]))
            self.block = self.clip(self.image, self.size*pos[0], self.size*pos[1], self.size, self.size).convert_alpha()
        else:
            self.block = image_path.convert_alpha()
        
        self.rect = self.block.get_rect()
        self.rect.x = x*self.size
        self.rect.y = y*self.size

    def clip(self, surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clipRect = pygame.Rect(x,y,x_size,y_size)
        handle_surface.set_clip(clipRect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()

class Board:
    def __init__(self, boardsize=(30, 30), tilesize=30):
        self.boardsize = boardsize
        self.tilesize = tilesize
        self.screen_width, self.screen_height = self.tilesize*self.boardsize[0], self.tilesize*self.boardsize[1]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.init()
        pygame.display.set_caption("Monster game")
        
    def run(self, movetype = 'keyboard', framedelay=0.03, automiddle = True):
        game_over = False
        self.paused = False
        middle = [25, 25]
        self.player = Characters.Player(A.screen, 30)
        self.player.x, self.player.y = 40, 40
        key_cooltime = 0
        space_clicked = 0
        self.movetype = movetype
        
        while not game_over:
            if self.paused == False:
                time.sleep(framedelay)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            space_clicked = 0
                    elif event.type == MOUSEWHEEL:
                        
                # 캐릭터 이동
                if self.movetype == 'keyboard':
                    key_cooltime = max(0, key_cooltime-1)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.player.move_left()
                        key_cooltime = 10
                    if keys[pygame.K_RIGHT]:
                        self.player.move_right()
                        key_cooltime = 10
                    if keys[pygame.K_UP]:
                        self.player.move_up()
                        key_cooltime = 10
                    if keys[pygame.K_DOWN]:
                        self.player.move_down()
                        key_cooltime = 10
                    if keys[pygame.K_SPACE]:
                        if space_clicked == 0:
                            self.paused = True
                            space_clicked = 1
                    #카메라 캐릭터로 이동
                    if keys[pygame.K_m] or automiddle:
                        middle = [self.player.x, self.player.y]

                #화면/맵 위치           
                mousepos = pygame.mouse.get_pos()
                x_unit = self.screen_width*0.04
                y_unit = self.screen_height*0.04
                if mousepos[0] > x_unit*23:
                    middle[0] += 0.5
                    if mousepos[0] > x_unit*24:
                        middle[0] +=0.5
                elif mousepos[0] < x_unit*2:
                    middle[0] -= 0.5
                    if mousepos[0] < x_unit*1:
                        middle[0] -= 0.5
                if mousepos[1] > y_unit*23:
                    middle[1] += 0.5
                    if mousepos[1] > y_unit*24:
                        middle[1] += 0.5
                elif mousepos[1] < y_unit*2:
                    middle[1] -= 0.5
                    if mousepos[1] < y_unit*1:
                        middle[1] -= 0.5

                # 몬스터 이동과 지형 변화
                for i in monster_group:
                    i.rect.x += (random.randint(-1, 0)+random.randint(0, 1)) * self.tilesize
                    i.rect.y += (random.randint(-1, 0)+random.randint(0, 1)) * self.tilesize
                    
                    change_grass = int(i.rect.x/self.tilesize)*100+int(i.rect.y/self.tilesize)
                    if 0 <= change_grass <= 10000:
                        grass_code[change_grass] = [random.randint(0, 2), random.randint(0, 2)]
                        grass_group.sprites()[int(i.rect.x/self.tilesize)*100+int(i.rect.y/self.tilesize)] = \
                        Entity("grasses_refined.png", int(i.rect.x/self.tilesize), int(i.rect.y/self.tilesize), pos=[*grass_code[change_grass], 3, 3])

                self.draw(middle)
                
            else :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.paused = False
        pygame.quit()
    
    def draw(self, middle=[25, 25]):
        # 스프라이트 그리기
        self.screen.fill((255, 255, 255))
        for i in grass_group:
            self.screen.blit(i.block, (i.rect.x-(middle[0]-self.boardsize[0]/2)*self.tilesize,
                                       i.rect.y-(middle[1]-self.boardsize[1]/2)*self.tilesize))
        for i in nature_group:
            self.screen.blit(i.block, (i.rect.x-(middle[0]-self.boardsize[0]/2)*self.tilesize,
                                       i.rect.y-(middle[1]-self.boardsize[1]/2)*self.tilesize))
        A.screen.blit(self.player.block, ((self.player.x-(middle[0]-self.boardsize[0]/2))*self.tilesize,
                                          (self.player.y-(middle[1]-self.boardsize[1]/2))*self.tilesize))
        for i in monster_group:
            self.screen.blit(i.block, (i.rect.x-(middle[0]-self.boardsize[0]/2)*self.tilesize,
                                       i.rect.y-(middle[1]-self.boardsize[1]/2)*self.tilesize))
        pygame.display.update()

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
    nature_group.add(Entity(stone, random.randint(0, 99), random.randint(0, 99), from_path=False))
    nature_group.add(Entity(stump, random.randint(0, 99), random.randint(0, 99), from_path=False))
    nature_group.add(Entity(grass_2, random.randint(0, 99), random.randint(0, 99), from_path=False))
    nature_group.add(Entity(grass_3, random.randint(0, 99), random.randint(0, 99), from_path=False))

monster_group = pygame.sprite.Group()

for i in range(45):
    monster_group.add(Entity("zilpuck.png", 50, 50))
