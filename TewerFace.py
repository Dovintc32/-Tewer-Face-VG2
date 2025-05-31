import pygame
from assets.assets_py.SETTINGS import *

pygame.init()

# Настройки окна
screen = pygame.display.set_mode((W, H))
pygame.display.set_icon(pygame.image.load(resource_path("assets\other\Tewer_Face_icon.png")))
pygame.display.set_caption("Tewer Face V2 by Dovintc")

clock = pygame.time.Clock()


RUN = True
while RUN:
    clock.tick(60)  # Ограничиваем до 60 FPS
    screen.fill((0, 0, 0))  # Чистим экран

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    if scene == 0:
        if fade_state == "in":
            alpha += fade_speed
            if alpha >= 255:
                alpha = 255
                fade_state = "visible"
                show_start_time = pygame.time.get_ticks()

        elif fade_state == "visible":
            if pygame.time.get_ticks() - show_start_time > visible_time:
                fade_state = "out"

        elif fade_state == "out":
            alpha -= fade_speed
            if alpha <= 0:
                alpha = 0
                scene = 1

        # Применяем прозрачность
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_position)

    if scene == 1:
        if fade_state2 == "in":
            alpha2 += fade_speed
            if alpha2 >= 255:
                alpha2 = 255
                fade_state2 = "visible"
                show_start_time = pygame.time.get_ticks()

        elif fade_state2 == "visible":
            if pygame.time.get_ticks() - show_start_time > visible_time:
                fade_state2 = "out"

        elif fade_state2 == "out":
            alpha2 -= fade_speed
            if alpha2 <= 0:
                alpha2 = 0
                scene = 2

        text_surface2.set_alpha(alpha2)
        screen.blit(text_surface2, text_position2)
    if scene == 2:
        pass
    
    pygame.display.flip()

pygame.quit()