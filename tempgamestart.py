from tempgame import *

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
