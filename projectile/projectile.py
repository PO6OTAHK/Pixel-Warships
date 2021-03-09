import pygame
class Projectile(pygame.sprite.Sprite):
    """Класс описывающий снаряд, принимает скорость, урон, тип, координаты, размер, картинка, группы(групп неограниченное кол-во)"""
    def __init__(self, speed, damage, typke, position, size, img, *groups):
        super().__init__(*groups)
        self.speed = speed
        self.damage = damage
        self.typke = typke
        self.position = position
        self.size = size
        self.img = img
help(Projectile)