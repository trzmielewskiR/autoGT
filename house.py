import pygame.image
import random
import os
from typing import Optional

class House(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, number_of_bins: int = 0, if_exits: bool = False):
        super().__init__()
        self.number_of_bins = number_of_bins
        self.x = x 
        self.y = y
        self.if_exists = if_exits
        self.bin_id = Optional[int]
        self.base_path = "\\resources\\textures\\building\\"

        # random sprite for house
        self.image = pygame.image.load(f"{os.getcwd()}{self.base_path}{self.get_random_house_texture()}")
        

    def get_random_house_texture(self) -> str:
        return random.choice(os.listdir(os.getcwd() + self.base_path))