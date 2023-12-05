import pygame
from input_box import InputBox
from pygame.locals import QUIT, K_s, KMOD_CTRL

# from top_menu import TopMenu
from canvas import Canvas

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
GRID_SIZE = 20
MAX_HISTORY_SIZE = 10
FPS = 60
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Art Drawing")

# Create a Canvas instance
canvas = Canvas(WIDTH, HEIGHT, GRID_SIZE, MAX_HISTORY_SIZE)

input_box1 = InputBox(10, 5, 50, 32, COLOR_INACTIVE, COLOR_ACTIVE, FONT)
input_box2 = InputBox(80, 5, 50, 32, COLOR_INACTIVE, COLOR_ACTIVE, FONT)
input_box3 = InputBox(150, 5, 50, 32, COLOR_INACTIVE, COLOR_ACTIVE, FONT)
input_boxes = [input_box1, input_box2, input_box3]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Pass events to the Canvas instance for handling
        canvas.handle_events(event)
        for box in input_boxes:
                box.handle_event(event)

    # Draw the pixels and the menu on the screen
    canvas.draw(screen)
    pygame.draw.rect(screen, (71, 71, 71), (0, 0, screen.get_width(), 40))
    

    for box in input_boxes:
        box.draw(screen)
    
    change_colour = True
    for box in input_boxes:
        if not box.valid_entry():
            change_colour = False
            break
    if change_colour:
        canvas.pen_colour = (int(input_box1.text), int(input_box2.text), int(input_box3.text))
        for box in input_boxes:
            box.clear_text()
            print("cleared")
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)
