class Ship(pygame.sprite.Sprite):
    """Класс описывающий корабль в который подаются: позиция, здоровье, текстуры, жив ли он, скорость, туррели, ширина, длина."""
    def __init__(self, x, y, HP, ID_img, He_alive, speed, objectt, ssize, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.HP = HP
        self.ID_img = ID_img
        self.He_alive = He_alive
        self.speed = speed
        self.objectt = objectt
        self.ssize = ssize
    
    def hit(self, HP, ):
        pass

    def sink(self, HP):
        if HP < 0:
            return True
        else:
            return False
    
    def plase_turret():
       yes = ssize // tsize
       return yes