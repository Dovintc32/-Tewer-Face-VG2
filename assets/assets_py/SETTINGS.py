import pygame
import sys
import os

pygame.init()

W, H = 1400, 800

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

background = pygame.image.load(resource_path("assets\Fons\Start_Fon\BackGround.png"))
background = pygame.transform.scale(background, (W, H))

# Настройки текста
font_size = 60
full_text = "Dovintc and Tooch1c"
full_text2 = "Tewer Face V2"
text_position = (50 + 300, H // 2)
text_color = (255, 255, 255)
text_color2 = (139, 0, 0)

scene = 0
fade_state = "in"
fade_state2 = "in"
alpha = 0
alpha2 = 0
fade_speed = 3
visible_time = 1000
show_start_time = None

font = pygame.font.Font(resource_path("assets\other\Bold.ttf"), font_size)
text_surface = font.render(full_text, True, text_color)
text_position = (W // 2 - text_surface.get_width() // 2, H // 2)

font2 = pygame.font.Font(resource_path("assets\other\Bold.ttf"), font_size)
text_surface2 = font2.render(full_text2, True, text_color2)
text_position2 = (W // 2 - text_surface2.get_width() // 2, H // 2)

background = pygame.image.load(resource_path("assets\Fons\Start_Fon\BackGround.png"))
background = pygame.transform.scale(background, (W, H))