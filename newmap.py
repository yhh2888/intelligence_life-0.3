import pygame, random, math, torch, time
from time import perf_counter as pfc

class Entity:
    def __init__(self, screen, x, y, map_width, map_height, color, size, proto_energy=150):

        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        self.color = color
        self.BLOCK_SIZE = size
        self.screen = screen
        self.energy = proto_energy
        self.energy_g = 0
        self.score = 0
        self.scoretime = 0
        self.old = 0
        
        self.x = x
        self.y = y
        self.viewcode = [random.uniform(0, 2) for i in range(random.randint(3, 5))]

        self.energy_g, self.nst_foodx, self.nst_foody, self.nst_otherx, self.nst_othery, self.nst_food_angle, \
        self.nst_other_angle, self.borderdistance, self.otherisin, self.foodisin = \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    def move(self, movedir = None):
        if movedir == 0:
            self.x += 1
        elif movedir == 1:
            self.y += 1
        elif movedir == 2:
            self.x -= 1
        elif movedir == 3:
            self.y -= 1
        else :
            self.x += random.choice([-1, 0, 1])
            self.y += random.choice([-1, 0, 1])
        
        if self.x < 0:
            self.x += 1
        elif self.x > self.MAP_WIDTH/self.BLOCK_SIZE-1:
            self.x -= 1
        if self.y < 0:
            self.y += 1
        elif self.y > self.MAP_HEIGHT/self.BLOCK_SIZE-1:
            self.y -= 1

    def draw(self):
        entity_rect = pygame.Rect(self.x*self.BLOCK_SIZE, self.y*self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(self.screen, self.color, entity_rect)

    def energy_waste(self):
        self.energy -= 1

def anglecells(angle, scope=20):
	scopelist = []
	if 0<=angle<=2:
		if 0.25<angle<0.75 or 1.25<angle<1.75:
			for i in range(scope):
				scopelist.append([round((1/math.tan(angle*math.pi))*i), i])
		else :
			for i in range(scope):
				scopelist.append([i, round(math.tan(angle*math.pi)*i)])
	return scopelist

class Food_system:
    def __init__(self, screen, map_width, map_height, color, size, give_energy=50):
        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        self.color = color
        self.BLOCK_SIZE = size
        self.screen = screen
        self.give_energy = give_energy

        self.foods = []

    def generate(self, number):
        for i in range(number):
            self.foods.append([random.randint(1, self.MAP_WIDTH/self.BLOCK_SIZE-1), random.randint(1, self.MAP_HEIGHT/self.BLOCK_SIZE-1)])

    def draw(self):
        for food in self.foods:
            food_rect = pygame.Rect(food[0]*self.BLOCK_SIZE, food[1]*self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
            pygame.draw.rect(self.screen, self.color, food_rect)
    
class Map:
    def __init__(self, map_width, map_height, proto_num=50):
        
        pygame.init()

        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        
        self.entitys = []
        
        self.BLOCK_SIZE = 2

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (50, 255, 50)

        self.screen = pygame.display.set_mode((self.MAP_WIDTH, self.MAP_HEIGHT))
        pygame.display.set_caption("Entity Movement")

        self.timeset = time.time()%200
        
        self.food = Food_system(self.screen, self.MAP_WIDTH, self.MAP_HEIGHT, self.GREEN, self.BLOCK_SIZE)
        
        for _ in range(proto_num):
            entity_x = random.randint(0, self.MAP_WIDTH/self.BLOCK_SIZE)
            entity_y = random.randint(0, self.MAP_HEIGHT/self.BLOCK_SIZE)
            entity = Entity(self.screen, entity_x, entity_y, self.MAP_WIDTH, self.MAP_HEIGHT, self.WHITE, self.BLOCK_SIZE)
            self.entitys.append(entity)

        self.maptile_width = int(self.MAP_WIDTH/self.BLOCK_SIZE)
        self.maptile_height = int(self.MAP_HEIGHT/self.BLOCK_SIZE)
        
        self.mapm = torch.zeros(self.maptile_width+60, self.maptile_height+60)

        self.clock = pygame.time.Clock()

        self.clock.tick(60)
        
    def run(self, movedata=None):
        a=0
        
        #t = pfc()
        if movedata != None:
            for e in range(len(self.entitys)):
                self.entitys[e].move(movedata[e][2])
                self.entitys[e].energy_g = 0
                self.entitys[e].scoretime += 1
                self.entitys[e].old += 1
        else :
            for e in range(len(self.entitys)):
                self.entitys[e].move()
                self.entitys[e].energy_g = 0
                self.entitys[e].scoretime += 1
                self.entitys[e].old += 1
                
        while len(self.food.foods) < 1800-((time.time()-self.timeset)%50)*20:
            self.food.generate(1)

        #print(pfc()-t)
            #t = pfc()

        for food in self.food.foods:
            self.mapm[food[0]+30, food[1]+30] = 2

        for i in range(len(self.entitys)):
            for j in range(i + 1, len(self.entitys)):
                if self.entitys[i] != self.entitys[j] and \
                    pygame.Rect(self.entitys[i].x, self.entitys[i].y, self.BLOCK_SIZE, self.BLOCK_SIZE).colliderect(
                    pygame.Rect(self.entitys[j].x, self.entitys[j].y, self.BLOCK_SIZE, self.BLOCK_SIZE)):
                    self.entitys[i].x = abs(self.entitys[j].x-1)
                    
            self.mapm[self.entitys[i].x+30, self.entitys[i].y+30] = 1

            if [self.entitys[i].x, self.entitys[i].y] in self.food.foods:
                del self.food.foods[self.food.foods.index([self.entitys[i].x, self.entitys[i].y])]
                self.entitys[i].energy_g = 10000/(self.entitys[i].scoretime+1)
                self.entitys[i].energy += 10000/(self.entitys[i].scoretime+1)
                self.entitys[i].score += 1/self.entitys[i].scoretime*(self.entitys[i].old/10)
                self.entitys[i].scoretime = 0
                
                
        #print(pfc()-t)
        #t = pfc()

        self.screen.fill(self.BLACK)

        #print(pfc()-t)
        #t = pfc()
            
        for entity in self.entitys:
            entity.view = self.mapm[max(0, entity.x):min(self.maptile_width+60, entity.x+60),
                                    max(0, entity.y):min(self.maptile_height+60, entity.y+60)]
            entity.nst_otherx, entity.nst_othery, entity.nst_other_angle, entity.otherisin = \
                                nearest(entity.view, 1, torch.tensor([entity.x+30, entity.y+30]), inscope=10)
            entity.nst_foodx, entity.nst_foody, entity.nst_food_angle, entity.foodisin = \
                                nearest(entity.view, 2, torch.tensor([entity.x+30, entity.y+30]), inscope=10)
            entity.borderdistance = min(200-entity.x, 200-entity.y, entity.x, entity.y)
            entity.energy_waste()
            entity.draw()
                
        self.food.draw()

        self.mapm = torch.zeros(self.maptile_width+60, self.maptile_height+60)

        #print(pfc()-t, 'done')

        pygame.display.flip()


        
def nearest(map_, point, loc, negative = False, inscope=10):
    if negative == False:
        coord = torch.nonzero(map_== point)-loc
    elif negative == True:
        coord = torch.nonzero(map_!= point)-loc
    else :
        raise TypeError

    if len(coord) > 0:
        squared_sum = torch.square(coord[:, 0]) + torch.square(coord[:, 1])
        index = torch.argmin(squared_sum)
        isin = [1 if torch.min(squared_sum**0.5) < inscope else 0][0]
        index = torch.tensor([index//map_.shape[0], index%map_.shape[1]])
        angle = torch.round(torch.atan2(index[1], index[0])*(180/torch.pi))
    else :
        index = torch.tensor([0, 0])
        isin = 0
        angle = 0

    return index[0], index[1], angle, isin
