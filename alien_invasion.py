import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # initial a game and window
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # start the game main loop
    while True:
        # listen the mouse and keyboard events
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)

run_game()