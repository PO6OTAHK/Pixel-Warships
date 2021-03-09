import pygame
import pygame_menu

pygame.init()
WIDTH = 704
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# mytheme = pygame_menu.themes.Theme(
#     image_path='D:\Projects\.vscode\Pixel Warships\Gun_1.png',
#     drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
    
menu = pygame_menu.Menu(640, 704, theme=pygame_menu.themes.THEME_DARK, title='Здраствуйте')

menu.background_color = ('D:\Projects\.vscode\Pixel Warships\Gun_1.png')
button = menu.add_button('Play', None) # В None функция игры или любая др.
button1 = menu.add_button('Options', None)
button2 = menu.add_button('Quit', None)

menu.mainloop(screen)
