import pygame.image

class Trash(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img: str, type: str):
        super().__init__()

        self.width = 16
        self.height = 16

        # spawn coords
        self.x = x
        self.y = y

        # type of trash
        self.type = type

        # image
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()