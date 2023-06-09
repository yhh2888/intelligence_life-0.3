import pygame
import random
from time import perf_counter as pfc

pygame.init()

MAP_WIDTH = 800
MAP_HEIGHT = 800

BLOCK_SIZE = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
pygame.display.set_caption("Block Movement")

clock = pygame.time.Clock()

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        xmove = random.choice([-1, 0, 1])
        ymove = random.choice([-1, 0, 1])
        
        self.x += xmove
        self.y += ymove
        
        if self.x < 0:
            self.x += 1
        elif self.x > MAP_WIDTH/BLOCK_SIZE:
            self.x -= 1
        if self.y < 0:
            self.y += 1
        elif self.y > MAP_HEIGHT/BLOCK_SIZE:
            self.y -= 1

    def draw(self):
        block_rect = pygame.Rect(self.x*BLOCK_SIZE, self.y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, WHITE, block_rect)

blocks = []
for _ in range(20):
    block_x = random.randint(0, MAP_WIDTH/BLOCK_SIZE)
    block_y = random.randint(0, MAP_HEIGHT/BLOCK_SIZE)
    block = Block(block_x, block_y)
    blocks.append(block)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for block in blocks:
        block.move()

    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if pygame.Rect(blocks[i].x, blocks[i].y, BLOCK_SIZE, BLOCK_SIZE).colliderect(
                pygame.Rect(blocks[j].x, blocks[j].y, BLOCK_SIZE, BLOCK_SIZE)
                ):
                blocks[i].x -= 1

    screen.fill(BLACK)

    for block in blocks:
        block.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
