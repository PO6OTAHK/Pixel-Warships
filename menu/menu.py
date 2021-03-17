def createMenu(game_instance, screen):
    engine = game_instance.pygame_menu.sound.Sound()
    engine.set_sound(game_instance.pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE, 'menu/menu_click.ogg')
    background_image = game_instance.pygame_menu.baseimage.BaseImage(
            image_path='menu/kon1.jpg',
            drawing_mode=game_instance.pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0,0)
    )
    mytheme = game_instance.pygame_menu.themes.Theme(
            background_color=background_image,
            title_background_color=(255, 255, 255),
            title_font_color=(0, 0, 0),
            widget_font=game_instance.FONT,
            widget_background_color=(255, 255, 255),
            title_font=game_instance.FONT,
            widget_font_size=25,
            title_font_size=35,
            widget_font_color=(0, 0, 0),
            selection_color=(0, 0, 0),
            widget_margin=(0, 20),
            widget_padding=10,
            title_bar_style=game_instance.pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    )
    menu = game_instance.pygame_menu.Menu(
        game_instance.HEIGHT_SCREEN, 
        game_instance.WIDTH_SCREEN, 
        'Hello',
        theme=mytheme
    )
    menu.set_sound(engine, recursive=True)
    menu.add_button('Play', game_instance.startGame) # В None функция игры или любая др.
    menu.add_button('Options', None)
    menu.add_button('Quit', game_instance.pygame_menu.events.EXIT)
    
    menu.mainloop(screen)


def init(game_instance):
    createMenu(game_instance, game_instance.getScreen())
    