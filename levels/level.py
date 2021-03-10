
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class level():
    def load_level(filename):
        with open(filename, 'r') as mapFile:
            level_map = []
            for line in mapFile:
                level_map.append(line.strip())
            return level_map

    def generate_level(level_map):
        new_player, x ,y = None, None, None
        for y in range(len(level_map)):
            for x in range(len(level_map[y])):
                if level_map[y][x] == ".":
                    Tile ("water", x, y)
                elif level_map[y][x] == "#":
                    Wall("sand", x, y)
                elif level_map[y][x] == "@":
                    Tile("water", x, y)
                    new_player = Player(x, y)

        return new_player, x, y

tile_images = {'water': pygame.image.load('data\image\water_tile.png')}
wall_images = {'sand': pygame.image.load('data\image\sand_tile.png')}
player_image = pygame.image.load('data\image\player\ShipV0.1right.png')