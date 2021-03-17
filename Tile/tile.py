import pygame
def init(game_instance_local):
    global game_instance
    game_instance = game_instance_local

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, *groups):
        super().__init__(groups)
        tile_images = {
            'water': game_instance.pygame.image.load('image/water_tile.png'),
            'sand': game_instance.pygame.image.load('image/sand_tile.png')
            }
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(64 * pos_x, 64 * pos_y)
