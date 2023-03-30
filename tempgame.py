import pygame, os
import random
from time import perf_counter
import Characters

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__()
        self.size=30
        self.image = self.img = pygame.image.load(os.getcwd()+'\\'+'resources\\'+image_path).convert_alpha()
        self.image = pygame.transform.scale(self.img, (self.size*4, self.size*4))
        self.block = self.clip(self.image, self.size*0, self.size*1, self.size, self.size)
        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = random.choice([-1, 1])

    def clip(self, surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clipRect = pygame.Rect(x,y,x_size,y_size)
        handle_surface.set_clip(clipRect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monster game")
player = Characters.Player(screen, 10)

player_sprite = Sprite("squirtle.png", 50, 50, 1)
monster_group = pygame.sprite.Group()
for i in range(45):
    monster_group.add(Sprite("zilpuck.png", 300, 300, 1))

def run():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # 캐릭터 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_sprite.rect.x -= player_sprite.speed
        elif keys[pygame.K_RIGHT]:
            player_sprite.rect.x += player_sprite.speed
        elif keys[pygame.K_UP]:
            player_sprite.rect.y -= player_sprite.speed
        elif keys[pygame.K_DOWN]:
            player_sprite.rect.y += player_sprite.speed

        # 몬스터 이동
        for i in monster_group:
            i.rect.x += random.randint(-1, 1) * i.speed
            i.rect.y += random.randint(-1, 1) * i.speed

        # 스프라이트 그리기
        screen.fill((255, 255, 255))
        screen.blit(player_sprite.block, player_sprite.rect)
        for i in monster_group:
            screen.blit(i.block, i.rect)
        pygame.display.update()
    pygame.quit()

run()
