import pygame

from map import preparedMap
from agent import Agent

#config
SCREEN_SIZE: tuple[int, int] = (512, 512)
BACKGROUND_COLOR: pygame.Color = pygame.Color('#ffffff')

if __name__ == '__main__':

    pygame.init()

    pygame.display.set_caption("autoGT")

    screen = pygame.display.set_mode(size=SCREEN_SIZE)
    screen.fill(pygame.Color(BACKGROUND_COLOR))

    map = preparedMap(SCREEN_SIZE)
    
    screen.blit(map, (0, 0))

    agent = Agent()
    agent_list = pygame.sprite.Group()
    agent_list.add(agent)
    agent_list.draw(screen)

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def AutoGtGame():
    def __init__(self):
        pass