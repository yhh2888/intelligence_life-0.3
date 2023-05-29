import random
import pygame
import numpy as np
from time import perf_counter as pfc
import time
from PIL import Image

# 색깔 정의
BLACK = ("#000000")
WHITE = ("#FFFFFF")
RED = ("#FF0000")
GREEN = ("#00FF00")
ORANGE = ("#FCAF00")
DCYAN = ("#0067A3")

# 화면 크기
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# 블록 크기
BLOCK_SIZE = 3

# 생명체 클래스
class Organism:
    def __init__(self):
        self.lifes = []
        self.energy = 100
        self.evolved = False
        self.num_children = 0
        
        self.lifespan = random.randint(50, 100)
        self.rotation = 0
        
        self.decoder = [0, Producer, Eater, Mover, Watcher]
        self.decoder_on = [0, Producer(), Eater(), Mover(), Watcher()]
        
        self.infield = np.zeros((int(SCREEN_WIDTH/BLOCK_SIZE), int(SCREEN_HEIGHT/BLOCK_SIZE)))
        self.real = np.zeros((int(SCREEN_WIDTH/BLOCK_SIZE), int(SCREEN_HEIGHT/BLOCK_SIZE)))
        self.foods = []

        self.eatrange = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
    def move(self):
        # 이동 세포 실행
        for i in range(len(self.lifes)):
            if 3.0 in self.lifes[i][0].reshape(1, 121):
                moveto = self.lifes[i][2]
                if self.collide_preventer(self.lifes[i], self.lifes[i][2]):
                    if moveto == 0:
                        self.lifes[i][1][0] += 1
                    elif moveto == 1:
                        self.lifes[i][1][1] += 1
                    elif moveto == 2:
                        self.lifes[i][1][0] -= 1
                    elif moveto == 3:
                        self.lifes[i][1][1] -= 1
                    self.lifes[i][1] = self.escape_preventer(self.lifes[i][1])
                
                if random.random() < 0.2:
                    self.lifes[i][2] = random.randint(0, 3)
                
        self.infield *= 0
        self.real *= 0
        
    def escape_preventer(self, loc):
        if 7 > loc[0]:
            loc[0] = 7
        elif loc[0] > SCREEN_WIDTH/BLOCK_SIZE-7:
            loc[0] = int(SCREEN_WIDTH/BLOCK_SIZE-7)
        if 7 > loc[1]:
            loc[1] = 7
        elif loc[1] > SCREEN_HEIGHT/BLOCK_SIZE-7:
            loc[1] = int(SCREEN_HEIGHT/BLOCK_SIZE-7)
        return loc

    def collide_preventer(self, life, dir_):
        if dir_ == 0:
            direc = [1, 0]
        elif dir_ == 1:
            direc = [0, 1]
        elif dir_ == 2:
            direc = [-1, 0]
        elif dir_ == 3:
            direc = [0, -1]
        self.infield[life[1][0]-5:life[1][0]+6, life[1][1]-5:life[1][1]+6] -= np.array((life[0]!=0)+np.zeros((11, 11)), dtype=int)
        map_ = self.infield[life[1][0]-5+direc[0]:life[1][0]+6+direc[0], life[1][1]-5+direc[1]:life[1][1]+6+direc[1]] + ((life[0]!=0)+0)
        self.infield[life[1][0]-5:life[1][0]+6, life[1][1]-5:life[1][1]+6] += np.array((life[0]!=0)+np.zeros((11, 11)), dtype=int)
        if len(set(map_.flatten())) != 2:
            return False
        else :
            return True

    def produce(self, prob=0.1):
        for lifes in self.lifes:
            if 1.0 in lifes[0]:
                for i in range(len(lifes[0])):
                    for j in range(len(lifes[0][i])):
                        if lifes[0][i, j] == 1.0 and prob > random.random():
                            location = [lifes[1][0]-5+i, lifes[1][1]-5+j]
                            location[random.randint(0, 1)] += random.randint(-1, 1)
                            
                            if self.real[location[0], location[1]] == 0:
                                self.foods.append(Food(location))

    def eat(self):
        for lifes in self.lifes:
            if 2.0 in lifes[0]:
                for i in range(len(lifes[0])):
                    for j in range(len(lifes[0][i])):
                        if lifes[0][i, j] == 2.0:
                            location = [[lifes[1][0]-5+i+loc[0], lifes[1][1]-5+j+loc[1]] for loc in self.eatrange]
                            
                            for k in location:
                                if self.real[k[0], k[1]] == 5:
                                    self.real[k[0], k[1]] -= 5
                                    delnum = 0
                                    for l in range(len(self.foods)):
                                        if self.foods[l-delnum].loc == k:
                                            del self.foods[l]
                                            lifes[3] += 7
                                            delnum += 1
                                            break
                        
    
    def biologic_change(self):
        delnum = 0
        for lifes in range(len(self.lifes)):
            if self.lifes[lifes-delnum][4] > 500:
                del self.lifes[lifes-delnum]
                delnum+=1
            if self.lifes[lifes-delnum][3] < 0:
                del self.lifes[lifes-delnum]
                delnum+=1
                
            lifes = self.lifes[lifes-delnum]
            
            if lifes[3] > 100:
                location = [lifes[1][0]+[random.randint(-6, -4), random.randint(4, 6)][random.randint(0, 1)],
                            lifes[1][1]+[random.randint(-6, -4), random.randint(4, 6)][random.randint(0, 1)]]
                rotation = random.randint(0, 3)
                if len(set((self.infield[location[0]-5:location[0]+6, location[1]-5:location[1]+6] + \
                        (lifes[0] != 0) + 0).flatten())) == 2:
                    newgen_code = lifes[0] + 0
                    for k in range(rotation):
                        newgen_code = np.rot90(newgen_code)
                    self.lifes.append([newgen_code, location, 0, 50, 0, imager(newgen_code)])
                    lifes[3] -= 50

            
        return None

    def update(self, screen):
        t = pfc()

        self.draw(screen)

        #print(pfc()-t)
        #t = pfc()
        
        self.produce()
        
        #print(pfc()-t)
        #t = pfc()
        
        self.eat()

        #print(pfc()-t)
        #t = pfc()
        
        self.biologic_change()

        #print(pfc()-t)
        #t = pfc()
        
        self.move()
        
        print(pfc()-t)

        #print('turn')
        
    def draw(self, screen):
        t = pfc()
        zeros = np.zeros((11, 11))
        for lifes in self.lifes:
            lifes[3]-=0.1
            lifes[4]+=1
            effobject_0 = lifes[1][0]
            effobject_1 = lifes[1][1]
            screen.blit(lifes[5], ((effobject_0-5) * BLOCK_SIZE, (effobject_1-5) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            self.infield[effobject_0-5:effobject_0+6, effobject_1-5:effobject_1+6] += (lifes[0]!=0)+zeros
            self.real[effobject_0-5:effobject_0+6, effobject_1-5:effobject_1+6] += lifes[0]
        #print(pfc()-t)
        #t = pfc()
        for foods in self.foods:
            pygame.draw.rect(screen, foods.color, (foods.loc[0] * BLOCK_SIZE, foods.loc[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            self.infield[foods.loc[0], foods.loc[1]] += 1
            self.real[foods.loc[0], foods.loc[1]] += 5
            
        #print(pfc()-t)
    def is_alive(self):
        return self.lifespan > 0

    


# 블록 클래스
class Block:
    def __init__(self, color, loc):
        self.color = color
        self.lifecode = np.zeros(11, 11)
        


class Producer:
    def __init__(self):
        self.color = GREEN

class Eater:
    def __init__(self):
        self.color = WHITE

class Mover:
    def __init__(self):
        self.color = RED

class Watcher:
    def __init__(self):
        self.color = ORANGE

class Food:
    def __init__(self, loc):
        self.color = DCYAN
        self.loc = loc

def transparent(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    cutOff = 0

    for item in datas:
        if item[0] <= cutOff and item[1] <= cutOff and item[2] <= cutOff:
            newData.append((255, 255, 255, 0))
            # RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿔줍니다.
        else:
            newData.append(item)
            # 나머지 요소는 변경하지 않습니다.

    img.putdata(newData)
    return img

def imager(matrix, size=(11, 11)):
    decoder = [(0, 255, 0), (255, 255, 255), (255, 0, 0), (int('FC', 16), int('AF', 16), 0)]
    x = np.zeros((*size, 3))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i, j] > 0:
                x[i,j] = decoder[int(matrix[i,j]-1)]
    ar_img = Image.fromarray(np.array(x, dtype=np.uint8))

    ar_img = transparent(ar_img)
    ar_img = pygame.image.fromstring(ar_img.tobytes(), ar_img.size, ar_img.mode)
    return pygame.transform.scale(ar_img, (11*BLOCK_SIZE, 11*BLOCK_SIZE))

# 게임 엔진 클래스
class LifeEngine:
    def __init__(self, num_organisms):
        self.num_organisms = num_organisms
        self.organism = Organism()

        
        '''for i in range(self.num_organisms):
            lifecode = np.zeros((11, 11))
            lifecode[5, 5] += 1
            for j in range(20):
                aa = random.randint(3, 8)
                bb = random.randint(3, 8)
                if len(set(lifecode[aa-1:aa+2, bb-1:bb+2].flatten())) != 1 and lifecode[aa, bb] < 1:
                    lifecode[aa, bb] += random.randint(1, 4)
            x = random.randint(7, SCREEN_WIDTH // BLOCK_SIZE -7)
            y = random.randint(7, SCREEN_HEIGHT // BLOCK_SIZE -7)
            self.organism.lifes.append([lifecode, [x, y], 0]) '''

        lifecode = np.zeros((11, 11))
        lifecode[5, 5] += 2
        lifecode[6, 6] += 1
        lifecode[4, 4] += 1

        self.organism.lifes.append([lifecode, [(SCREEN_WIDTH // BLOCK_SIZE) // 2, (SCREEN_HEIGHT // BLOCK_SIZE) // 2], 0, 50, 0, imager(lifecode)]) #[shape, location, direction, energy, age, imgdata]
        
    
    def run(self): 
        pygame.init() 
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Life Engine")
        clock = pygame.time.Clock()
        running = True
        round_count = 0
        
        while running:
            t = pfc()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

            
            screen.fill(BLACK)
            self.organism.update(screen)
            
            pygame.display.flip()

            round_count += 1
            
            #print(pfc()-t)
            
        pygame.quit() 
        
# 게임 실행 
engine = LifeEngine(num_organisms=100)
engine.run()
