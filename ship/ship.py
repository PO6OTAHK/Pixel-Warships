import pygame
def init(game_instance_local):
    global game_instance
    game_instance = game_instance_local

class Ship(pygame.sprite.Sprite):
    """Класс описывающий корабль в который подаются: позиция, здоровье, текстуры, жив ли он, скорость, туррели, ширина, длина."""
    def __init__(self, x, y, *groups, HP=100, speed=5, objectt=None, size=(128, 64)):
        super().__init__(groups)
        self.ship_image = {
                    'right': game_instance.pygame.image.load('ship/Textur/ShipV01right.png'), 
                    'left': game_instance.pygame.image.load('ship/Textur/ShipV01left.png'),
                    'up': game_instance.pygame.image.load('ship/Textur/ShipV01up.png'),
                    'down': game_instance.pygame.image.load('ship/Textur/ShipV01down.png'),
        }
        self.HP = HP
        self.image = self.ship_image['right']
        self.is_alive = True
        self.speed = speed
        self.objectt = objectt
        self.size = size
        self.x, self.y = x, y
        self.rect = self.image.get_rect().move(64 * self.x, 34 * self.y)
    
    def changeState(self, state):
        self.image = self.ship_image[state]
        # if state == 'up' or state == 'down':
        #     self.image = game_instance.pygame.transform.scale(self.ship_image[state], (34, 64))
        # else:
        #     self.image = game_instance.pygame.transform.scale(self.ship_image[state], (64, 34))

    def hit(self, damage):
        pass

    def sink(self):
        if self.HP < 0:
            return True
        else:
            return False
    
    def plase_turret(self):
       yes = self.ssize // self.tsize
       return yes


      
        