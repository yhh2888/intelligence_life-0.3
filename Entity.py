import pygame, os

class Entity(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, size=30, pos=[0, 0, 4, 4], from_path=True):
        super().__init__()
        self.size=size
        self.pos = pos
        if from_path:
            self.image = pygame.image.load(os.getcwd()+'\\'+'resources\\'+image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size*pos[2], self.size*pos[3]))
            self.block = self.clip(self.image, self.size*pos[0], self.size*pos[1], self.size, self.size).convert_alpha()
        else:
            self.image = image_path.convert_alpha()
            self.block = self.image
        
        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.y = y

    def clip(self, surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clipRect = pygame.Rect(x,y,x_size,y_size)
        handle_surface.set_clip(clipRect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()
