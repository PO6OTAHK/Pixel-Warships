def init(game_instance):
    BACKGROUND_GAME = game_instance.pygame.image.load("image/background.png")
    transform_background_img = game_instance.pygame.transform.scale(BACKGROUND_GAME, game_instance.SIZE_SCREEN)
    # Подгружаем модуль объектов, персонажей
    import Tile.tile as tile_module
    tile_module.init(game_instance)
    import ship.ship as ship_module
    ship_module.init(game_instance)
    # Создаём общую группу спрайтов
    all_sprites = game_instance.pygame.sprite.Group()
    tile_group = game_instance.pygame.sprite.Group()
    walls_group = game_instance.pygame.sprite.Group()
    
    import levels.level
    game_level = levels.level.Level("levels/k.txt")
    player, level_x, level_y = game_level.generateLevel(tile_module, ship_module, all_sprites, tile_group, walls_group)
    camera_this_game = levels.level.Camera((level_x, level_y))
    STEP = 16
    game_run = True
    while game_run:
        for event in game_instance.getEvents():
            if event.type == game_instance.pygame.KEYDOWN:
                if event.key == game_instance.pygame.K_LEFT:
                    player.rect.x -= STEP
                    player.changeState('left')
                    if game_instance.pygame.sprite.spritecollide(player, walls_group, False):
                        player.rect.x += STEP
                    
                if event.key == game_instance.pygame.K_RIGHT:
                    player.rect.x += STEP
                    player.changeState('right')
                    if game_instance.pygame.sprite.spritecollide(player, walls_group, False):
                        player.rect.x -= STEP

                if event.key == game_instance.pygame.K_UP:
                    player.rect.y -= STEP
                    player.changeState('up')
                    if game_instance.pygame.sprite.spritecollide(player, walls_group, False):
                        player.rect.y += STEP

                if event.key == game_instance.pygame.K_DOWN:
                    player.rect.y += STEP
                    player.changeState('down')
                    if game_instance.pygame.sprite.spritecollide(player, walls_group, False):
                        player.rect.y -= STEP

        camera_this_game.update(player, game_instance.SIZE_SCREEN)
        for sprite in all_sprites:
            camera_this_game.apply(sprite)
         # Обновление спрайтов
        all_sprites.update()
        # Отрисовка всех спрайтов 
        game_instance.screen.blit(transform_background_img, (0, 0))
        all_sprites.draw(game_instance.getScreen())
        game_instance.pygame.display.flip()