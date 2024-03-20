import pygame

from map import preparedMap
from agent import Agent
from house import House


class AutoGtGame():
    def __init__(self):
        self.SCREEN_SIZE = (512, 512)
        self.BACKGROUND_COLOR = pygame.Color('#ffffff')

        pygame.init()
        pygame.display.set_caption("autoGT")

        self.screen = pygame.display.set_mode(size=self.SCREEN_SIZE)
        self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))

        self.map = preparedMap(self.SCREEN_SIZE)
        self.screen.blit(self.map, (0, 0))
        
    def update_window(self):
        pygame.display.update()

    
    def draw_object(self, drawable_object, position: tuple[int, int]):
        # drawable object must have .image field inside class
        self.screen.blit(drawable_object.image, position)


    def reload_map(self):
        self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))
        self.screen.blit(self.map, (0, 0))


def main():
    game = AutoGtGame()
    game.update_window()

    house = House(20, 20)
    agent = Agent(16, 16, "resources\\textures\\garbagetruck\\trashmaster_blu.png")
    game.draw_object(agent, (0, 0))
    game.draw_object(house, (20, 20))
    

    game.update_window()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.reload_map()
                game.draw_object(agent, agent.move(event.key, 16))
                game.draw_object(house, (20, 20))
                game.update_window()

    pygame.quit()


if __name__ == "__main__":
    main()