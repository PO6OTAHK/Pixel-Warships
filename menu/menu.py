import pygame
import pygame_menu
from pygame_menu import sound

pygame.init()
WIDTH = 704
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'menu_click.mp3')
engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, 'menu.mp3')

mytheme = pygame_menu.themes.Theme(
    image_path='D:\Projects\.vscode\Pixel Warships\kon1.jpg',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)

    
menu = pygame_menu.Menu(640, 704, mytheme, title='Здраствуйте')

button = menu.add_button('Play', None) # В None функция игры или любая др.
button1 = menu.add_button('Options', None)
button2 = menu.add_button('Quit', None)

menu.mainloop(screen)
