import pygame
import random
from time import perf_counter

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = random.choice([-1, 1])

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monster game")

player_sprite = Sprite(r"C:\Users\KDCA\Desktop\IL\resources\block.jpg", 50, 50, 1)
monster_group = pygame.sprite.Group()
for i in range(15):
    monster_group.add(Sprite(r"C:\Users\KDCA\Desktop\IL\resources\mobs.jpg", 300, 300, 1))



@jit(nopython=True)
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
        t = perf_counter()
        screen.fill((255, 255, 255))
        screen.blit(player_sprite.image, player_sprite.rect)
        for i in monster_group:
            screen.blit(i.image, i.rect)
        pygame.display.update()
        print(perf_counter()-t)
    pygame.quit()

run()
