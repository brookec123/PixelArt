import pygame
import pygame_menu
from pygame.locals import QUIT, K_s, K_o, KMOD_CTRL
pygame.init()
surface = pygame.display.set_mode((600, 400))
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
about_menu = pygame_menu.Menu('About', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
about_menu.add_label('Pygame is a python game development library')
about_menu.add_label('Pygame Menu assists in creating game menus')
about_menu.add_button('Return to main menu', pygame_menu.events.BACK)
menu.add_button('About', about_menu)
menu.mainloop(surface)
class TopMenu:
    def __init__(self):
        pass

    