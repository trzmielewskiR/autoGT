import pygame

TILE_SIZE: int = 16

def preparedMap(screenSize: tuple[int, int]) -> pygame.Surface:
    tile_image = pygame.image.load('tile1.png')
    surface = pygame.Surface(screenSize)
    
    for x in range(0, screenSize[0], TILE_SIZE):
        for y in range(0, screenSize[1], TILE_SIZE):
            surface.blit(tile_image, (x, y))
    return surface
