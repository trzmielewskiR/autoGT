import pygame.image

class Trashbin(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img: str, type: str):
        super().__init__()

        self.width = 16
        self.height = 16

        # spawn coords
        self.x = x
        self.y = y

        # type of trashbin
        self.type = type
        match type:
            case "small":
                self.width = 4
                self.height = 4
            case "medium":
                self.width = 8
                self.height = 8
            case "large":
                self.width = 16
                self.height = 16

        # image
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()