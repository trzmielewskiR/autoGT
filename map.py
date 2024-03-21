import pygame
import pytmx
import settings

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class TiledMap:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm


    def render(self, surface: pygame.Surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
    

class Camera:
    def __init__(self, width: int, height: int):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    

    def update(self, target):
        x = -target.rect.x + int(settings.WIDTH / 2)
        y = -target.rect.y + int(settings.HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - settings.WIDTH), x)
        y = max(-(self.height - settings.HEIGHT), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)