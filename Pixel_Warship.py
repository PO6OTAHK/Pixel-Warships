# импорт всех библиотек. после чего будут доступны реализованные решения из них
import os
import sys
import pygame
# TODO: импорт клавиш

# инициализация
pygame.init()
pygame.font.init()
Starfont = pygame.font.Font('D:\Projects\.vscode\Fonts\SF Distant Galaxy Alternate.ttf', 38)

# устанавливаем характеристики повторения нажатия клавиш
# set_repeat (задержка, интервал)
pygame.key.set_repeat(200, 70)

# ширина экрана
WIDTH = 704
# высота экрана
HEIGHT = 640
# шаг героя
STEP = 16

# создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
damage_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()


#TODO загрузка уровня
def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = []
        for line in mapFile:
            level_map.append(line.strip())
        return level_map


#TODO генерация уровня
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
            # elif level_map[y][x] == "0":
            #     Damage_object("mine", x, y)
    
    return new_player, x, y

tile_images = {'water': pygame.image.load('data\image\water_tile.png')}
wall_images = {'sand': pygame.image.load('data\image\sand_tile.png')}
player_image = pygame.image.load('data\image\player\ShipV0.1right.png')
player_walk_image = [
    pygame.image.load('data\image\player\ShipV0.1down.png'),
    pygame.image.load('data\image\player\ShipV0.1up.png'),
    pygame.image.load('data\image\player\ShipV0.1right.png'),
    pygame.image.load('data\image\player\ShipV0.1left.png')
]
player_image_rotate = player_walk_image[2]
turret_images = pygame.image.load('data\image\Turrets\Gun_1.png')
# mine_image = {'mine': pygame.image.load('data\Mine1.png')}

tile_width = tile_height = wall_width = wall_height = damage_width = damage_height = 64
player_width = 128
player_height = 64
turret_width = 32
turret_height = 16

# TODO класс tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

# TODO класс wall
class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_type, pos_x, pos_y):
        super().__init__(walls_group, all_sprites)
        self.image = wall_images[wall_type]
        self.rect = self.image.get_rect().move(wall_width * pos_x, wall_height * pos_y)
        self.health = 100

# TODO класс player
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        global player_image_rotate
        self.images_walk = player_image_rotate
        self.index_walk = 0
        self.state = 'stop'
        self.image = player_image_rotate
        self.rect = self.image.get_rect().move(player_width * pos_x, player_height * pos_y)
    
    # def change_state(self):
    #     if self.state == 'stop':
    #         self.state = state
    #     else:
    #         self.state = state
    #     return self.state
    # 
    def update(self):
        if self.state == 'walk':
            self.index_walk += 1
            if self.index_walk >= len(self.images_walk):
                self.index_walk = 0
            self.image = self.image_walk[self.index_walk]
        else:
            self.index_walk = 0
            self.image = self.image_walk[self.index_walk]
    
class Turrets(pygame.sprite.Sprite):
    def gun_1(self, post_x, post_y):
        super().__init__(turret_group, all_sprites)
        self.image = turret_images
        self.rect = self.image.get_rect().move(turret_width * post_x, turret_height * post_y)


    # def getDamage(self, damage):
    #     if self.health > 0:
    #         self.health -= damage
    #     return self.health



# def load_menu():
#     # набор пунктов меню, список []
#     elements_menu = [   
#         #[x, y, название, цвет обычный, цвет при наведении, id]
#         [300, 200, 'Play', [255, 0, 0], [0, 255, 0], 0],
#         [300, 270, 'Quit', [255, 0, 0], [0, 255, 0], 1],
#         [300, 340, 'Options', [255, 0, 0], [0, 255, 0], 2]
#     ]
#     pygame.key.set_repeat(0, 0)
#     pygame.mouse.set_visible(True)
# 
#     fon = pygame.transform.scale(pygame.image.load("D:\Projects\.vscode\KEK\data\Fon.png"), (WIDTH, HEIGHT))
#     screen.blit(fon, (0, 0))
# 
#     element = -1
#     done = False
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame. QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if element == 0:
#                     pygame.key.set_repeat(200, 70)
#                     done = True
#                 elif element == 1:
#                     pygame.quit()
#                     sys.exit()
#             # Получение позиции курсора мыши
#             pointer = pygame.mouse.get_pos()
#              # Совпали ли координаты курсора и кнопки
#             for el in elements_menu:
#                 if pointer[0] > el[0] and pointer[0] < el[0] + 100 and pointer[1] < el[1] + 10 and pointer[1] > el[1] and pointer[2] < el[2] + 10 and pointer[2] > el[2]:
#                     element = el[5]
# 
#             
#             for el in elements_menu:
#                 if element == el[5]:
#                     screen.blit(Starfont.render(el[2], 1, el[4]), [el[0], el[1] - 40])
#                 else:
#                     # изменение цвета
#                     screen.blit(Starfont.render(el[2], 1, el[3]), [el[0], el[1] - 40])
# 
#             # window.blit(score, [0, 0])
#             # window.blit(screen, [0, 0])
#             pygame.display.flip()

#class Damage_object(pygame.sprite.Sprite):
#    super().__init__(damage_group, all_sprites)
#    self.image = mine_image
#    self.rect = self.image.get_rect().move(damage_width * pos_x, damage_height * pos_y)

class Camera:
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size
    
    def apply(self, obj):
        obj.rect.x += self.dx
         # вычислим координату клитки, если она уехала влево за границу экрана
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width
        # вычислим координату клитки, если она уехала вправо за границу экрана            
        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        # вычислим координату клитки, если она уехала вверх за границу экрана
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        # вычислим координату клитки, если она уехала вниз за границу экрана
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


player, level_x, level_y = generate_level(load_level("data\levels\k.txt"))
camera_this_game = Camera((level_x, level_y))



#load_menu()
running = True
# цикл игры
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #load_menu()
        elif event.type == pygame.KEYDOWN:
        #     player.change_state('walk')
            
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
                gun_1.rect.x -= STEP
                player_image_rotate = player_walk_image[3]
                if pygame.sprite.spritecollide(player, walls_group, False):
                    player.rect.x += STEP
                    gun_1.rect.x += STEP
                    
               
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
                gun_1.rect.x += STEP
                player_image_rotate = player_walk_image[1]
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.x -= STEP
                     gun_1.rect.x -= STEP

            if event.key == pygame.K_UP:
                player.rect.y -= STEP
                gun_1.rect.x -= STEP
                player_image_rotate = player_walk_image[2]
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.y += STEP
                     gun_1.rect.x += STEP

            if event.key == pygame.K_DOWN:
                player.rect.y += STEP
                gun_1.rect.x += STEP
                player_image_rotate = player_walk_image[0]
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.y -= STEP
                     gun_1.rect.x -= STEP
        
        # elif event.type == pygame.KEYUP:
        #     player.change_state('stop')
            
    # if pygame.sprite.spritecollide(player, damage_group, False):
    #     health -= 50

    camera_this_game.update(player)
    for sprite in all_sprites:
        camera_this_game.apply(sprite)
    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    walls_group.draw(screen)
    turret_group.draw(screen)
    player_group.draw(screen)
    player_group.update


    pygame.display.flip()

pygame.quit()