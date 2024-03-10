import pygame

class Agent(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, img:str):
        super().__init__()

        self.img = img
        self.width = x
        self.height = y

        self.x = 0
        self.y = 0

        self.image = pygame.image.load(img) 
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()


    def move(self, key: pygame.key, velocity: int):
        if key == pygame.K_LEFT:
            self.x -= velocity
        if key == pygame.K_RIGHT:
            self.x += velocity
        if key == pygame.K_UP:
            self.y -= velocity
        if key == pygame.K_DOWN:
            self.y += velocity
        
        return (self.x, self.y)