import pygame.image

class Dump(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.glass = []
        self.paper = []
        self.bio = []
        self.other = []