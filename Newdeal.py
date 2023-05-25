import random
import pygame

# 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 블록 크기
BLOCK_SIZE = 20

# 생명체 클래스
class Organism:
    def __init__(self, x, y):
        self.blocks = []
        self.energy = 100
        self.evolved = False
        self.num_children = 0
        self.lifespan = random.randint(50, 100)
        self.x = x
        self.y = y
        self.rotation = 0

    def add_block(self, block):
        self.blocks.append(block)
    
    def remove_block(self, block):
        self.blocks.remove(block)
    
    def consume_energy(self, amount):
        self.energy -= amount
    
    def produce_energy(self, amount):
        self.energy += amount

    def move(self):
        if self.energy >= 20:
            self.energy -= 20
            # 이동 세포 실행
            if isinstance(self.blocks[0], MovableBlock):
                self.x += 1
                self.y += 1

    def attack(self, target):
        # 공격 블록 실행
        pass
    
    def defend(self):
        # 방어 블록 실행
        pass
    
    def evolve(self):
        # 진화 알고리즘 구현
        self.evolved = True
    
    def reproduce(self):
        if self.energy >= 100:
            self.energy -= 100
            self.num_children += 1
            return Organism(self.x, self.y)
        return None

    def update(self):
        self.move()

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, block.color, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    def is_alive(self):
        return self.lifespan > 0


# 블록 클래스
class Block:
    def __init__(self, block_type):
        self.block_type = block_type


# 이동 블록 클래스
class MovableBlock(Block):
    def __init__(self, block_type):
        super().__init__(block_type)
        self.color = GREEN


# 게임 엔진 클래스
class LifeEngine:
    def __init__(self, num_organisms):
        self.organisms = []
        self.num_organisms = num_organisms

    def create_organisms(self):
        for _ in range(self.num_organisms):
            x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE)
            y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE)
            organism = Organism(x, y)
            organism.add_block(MovableBlock("Move"))
            self.organisms.append(organism)            
    
    def simulate_round(self): 
        new_organisms = [] 
        for organism in self.organisms: 
            organism.update()
            target = random.choice(self.organisms)
            organism.attack(target)
            organism.defend() 

            # 생명체 진화 
            if organism.energy >= 200 and not organism.evolved:
                organism.evolve()

            # 생명체 자손 생성
            child = organism.reproduce()
            if child is not None: 
                new_organisms.append(child)

            organism.lifespan -= 1 
    
        self.organisms.extend(new_organisms)
        self.organisms = [organism for organism in self.organisms if organism.is_alive()]
    
    def run(self, num_rounds): 
        pygame.init() 
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Life Engine")
        clock = pygame.time.Clock()
        self.create_organisms()
        running = True
        round_count = 0
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                    
            screen.fill(BLACK)
            self.simulate_round()
                    
            for organism in self.organisms: 
                organism.draw(screen)
                
            pygame.display.flip()
            clock.tick(10)
            
            round_count += 1
            
            if round_count >= num_rounds:
                running = False
                
        pygame.quit() 
        
# 게임 실행 
engine = LifeEngine(num_organisms=5)
engine.run(num_rounds=100)
            
