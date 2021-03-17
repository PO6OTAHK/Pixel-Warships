class Level:
    '''Определяет вид уровня, его состояние.'''
    def __init__(self, filename):
        self.filename = filename
        self.loadLevel()

    def loadLevel(self):
        with open(self.filename, 'r') as mapFile:
            self.level_map = []
            for line in mapFile:
                self.level_map.append(line.strip())
        return self.level_map
    
    def generateLevel(self, tile_module, ship_module, all_sprites, tile_group, wall_group):
        for y in range(len(self.level_map)):
            for x in range(len(self.level_map[y])):
                # if self.level_map[y][x] == ".":
                #     tile_module.Tile("water", x, y, tile_group, all_sprites)
                if self.level_map[y][x] == "#":
                    tile_module.Tile("sand", x, y, wall_group, all_sprites)
                elif self.level_map[y][x] == "@":
                    # tile_module.Tile("water", x, y, tile_group, all_sprites)
                    new_player = ship_module.Ship(x, y, all_sprites)
<<<<<<< HEAD
                    
=======
        return new_player, x, y

class Camera:
    # зададим начальный сдвиг камеры и размер поля для возможности реализации циклического сдвига
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size
>>>>>>> 8421f07c1f3349d84d8c6ea3b2e0b1e50d2bc16b

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        # вычислим координату клетки, если она уехала влево за границу экрана
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * 64
        # вычислим координату клетки, если она уехала вправо за границу экрана            
        if obj.rect.x >= (self.field_size[0]) * 64:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        # вычислим координату клетки, если она уехала вверх за границу экрана
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * 64
        # вычислим координату клетки, если она уехала вниз за границу экрана
        if obj.rect.y >= (self.field_size[1]) * 64:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

<<<<<<< HEAD
class Camera:
    # зададим начальный сдвиг камеры и размер поля для возможности реализации циклического сдвига
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        # вычислим координату клетки, если она уехала влево за границу экрана
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * 64
        # вычислим координату клетки, если она уехала вправо за границу экрана            
        if obj.rect.x >= (self.field_size[0]) * 64:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        # вычислим координату клетки, если она уехала вверх за границу экрана
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * 64
        # вычислим координату клетки, если она уехала вниз за границу экрана
        if obj.rect.y >= (self.field_size[1]) * 64:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

=======
>>>>>>> 8421f07c1f3349d84d8c6ea3b2e0b1e50d2bc16b
    # позиционировать камеру на объекте target
    def update(self, target, size_screen):
        self.dx = -(target.rect.x + target.rect.w // 4 - size_screen[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 4 - size_screen[1] // 2)