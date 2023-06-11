import pygame, random, math, torch
from time import perf_counter as pfc

class Entity:
    def __init__(self, screen, x, y, map_width, map_height, color, size):

        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        self.color = color
        self.BLOCK_SIZE = size
        self.screen = screen
        
        self.x = x
        self.y = y
        self.viewcode = [random.uniform(0, 2) for i in range(random.randint(3, 5))]

    def move(self):
        xmove = random.choice([-1, 0, 1])
        ymove = random.choice([-1, 0, 1])
        
        self.x += xmove
        self.y += ymove
        
        if self.x < 30:
            self.x += 1
        elif self.x > self.MAP_WIDTH/self.BLOCK_SIZE-30:
            self.x -= 1
        if self.y < 30:
            self.y += 1
        elif self.y > self.MAP_HEIGHT/self.BLOCK_SIZE-30:
            self.y -= 1

    def draw(self):
        entity_rect = pygame.Rect(self.x*self.BLOCK_SIZE, self.y*self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(self.screen, self.color, entity_rect)

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

    
class Map:
    def __init__(self, map_width, map_height, proto_num=50):
        
        pygame.init()

        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        
        self.entitys = []
        
        self.BLOCK_SIZE = 4

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.screen = pygame.display.set_mode((self.MAP_WIDTH, self.MAP_HEIGHT))
        pygame.display.set_caption("Entity Movement")
        
        for _ in range(proto_num):
            entity_x = random.randint(30, self.MAP_WIDTH/self.BLOCK_SIZE-30)
            entity_y = random.randint(30, self.MAP_HEIGHT/self.BLOCK_SIZE-30)
            entity = Entity(self.screen, entity_x, entity_y, self.MAP_WIDTH, self.MAP_HEIGHT, self.WHITE, self.BLOCK_SIZE)
            self.entitys.append(entity)
            
        self.mapm = torch.zeros(201, 201)

        self.clock = pygame.time.Clock()
        
    def run(self):
        running = True
        while running:
            a=0
            t = pfc()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            print(pfc()-t)
            t = pfc()
            
            for entity in self.entitys:
                entity.move()

            print(pfc()-t)
            t = pfc()
            
            for i in range(len(self.entitys)):
                for j in range(i + 1, len(self.entitys)):
                    if pygame.Rect(self.entitys[i].x, self.entitys[i].y, self.BLOCK_SIZE, self.BLOCK_SIZE).colliderect(
                        pygame.Rect(self.entitys[j].x, self.entitys[j].y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                        ):
                        self.entitys[i].x -= 1
                self.mapm[self.entitys[i].x, self.entitys[i].y] = 1

            print(pfc()-t)
            t = pfc()

            self.screen.fill(self.BLACK)

            print(pfc()-t)
            t = pfc()
            
            for entity in self.entitys:
                entity.view = maps.mapm[max(0, entity.x-28):min(200, entity.x+28), max(0, entity.y-28):min(200, entity.y+28)]
                        
                entity.draw()

            self.mapm = torch.zeros(201, 201)

            print(pfc()-t, 'done', a)

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    maps = Map(800, 800)
    maps.run()
