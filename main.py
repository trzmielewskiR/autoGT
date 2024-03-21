from settings import WIDTH, HEIGHT

import pygame

from map import TiledMap
from agent import Agent
#from house import House
from sprites import Player, Obstacle


class AutoGtGame():
    def __init__(self):
        self.SCREEN_SIZE = (WIDTH, HEIGHT)
        #self.BACKGROUND_COLOR = pygame.Color('#ffffff')

        pygame.init()
        pygame.display.set_caption("autoGT")

        self.screen = pygame.display.set_mode(size=self.SCREEN_SIZE)
        #self.screen.fill(pygame.Color(self.BACKGROUND_COLOR))

        self.walls = pygame.sprite.Group()
        self.player_img = pygame.image.load("resources\\textures\\garbagetruck\\trashmaster_blu.png").convert_alpha()
        self.all_sprites = pygame.sprite.Group()
        self.map = TiledMap("resources\\textures\\map\\roads.tmx")
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.screen.blit(self.map_img, (0, 0))

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == "obstacle":
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

        
    def update_window(self):
        pygame.display.update()

    
    def draw_object(self, drawable_object, position: tuple[int, int]):
        # drawable object must have .image field inside class
        self.screen.blit(drawable_object.image, position)


    def reload_map(self):
        self.screen.blit(self.map_img, (0, 0))


def main():
    game = AutoGtGame()
    game.update_window()

    #house = House(20, 20)
    agent = Agent(16, 16, "resources\\textures\\garbagetruck\\trashmaster_blu.png")
    game.draw_object(agent, (0, 0))
    #game.draw_object(house, (20, 20))
    

    game.update_window()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.reload_map()
                game.draw_object(agent, agent.move(event.key, 16))
                game.update_window()

    pygame.quit()


if __name__ == "__main__":
    main()