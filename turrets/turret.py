turrets = [pygame.image.load('D:\Projects\.vscode\Pixel Warships\Turrets\Textur\Gun_1.png')]
class turret(pygame.sprite.Sprite):
    """Класс описывающий турели, принимает: размер, текстуры, время перезарядки, координаты мышки."""
    def __init__(self, tsize, timg_ID, r_time, *groups):
        super().__init__(*groups)
        self.tsize = tsize
        self.timg_ID = timg_ID
        self.r_time = r_time
    
    def fire(...):
        if pass:
            return True
        else:
            return False
    
    def pointed_at(mouse_x_y):
        pass
