class PixelWarships:
    '''Основной игровой объект.Является мозгом игры и ключевым звеном между всеми этапами игры.'''
    # основные импорты
    import pygame
    import pygame_menu
    import sys
    # Блок констант
    SIZE_SCREEN = (WIDTH_SCREEN, HEIGHT_SCREEN) = (704, 640)
    FONT = pygame_menu.font.FONT_8BIT

    # в конструкторе инициализация и определение окна 
    def __init__(self):
        self.pygame.init()
        # Создание окна
        self.screen = self.pygame.display.set_mode(self.SIZE_SCREEN)

    # Секция гетеров, хорошим тоном будет не таскать саму переменную, чтобы случайно не заменить в ней значение, а использовать геттер
    def getScreen(self):
        return self.screen
    
    # чтобы не дублировать везде выходы из игры, если игра расширится
    def getEvents(self):
        'Получение всех свободных событий'
        events = self.pygame.event.get()
        for event in events:
            if event.type == self.pygame.QUIT:
                quit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_ESCAPE:
                    quit()
        return events

    # Секция интерфейсов
    def start(self):
        'Объявление начала игры'
        self.openMenu()

    def openMenu(self):
        'Открытие меню игры'
        import menu.menu
        menu.menu.start(self)

    def startGame(self):
        'Запуск игровой сессии'
        import game
        game.init(self)

    def quit(self):
        'Закрытие игры'
        self.pygame.quit()
        self.sys.exit()


# Создание экземпляра игра и запуск
game_instance = PixelWarships()
game_instance.start()