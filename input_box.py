import pygame

class InputBox:
    def __init__(self, x, y, w, h, inactive_colour, active_colour, font, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour
        self.font = font
        self.colour = self.inactive_colour
        self.text = text
        self.is_done = False
        self.txt_surface = self.font.render(text, True, self.colour)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current colour of the input box.
            self.colour = self.active_colour if self.active else self.inactive_colour
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.is_done = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.colour)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, 2)
    
    def valid_entry(self):
        if self.text != "":
            try:
                if  self.text != "" and int(self.text) <= 255 and int(self.text) >= 0:
                    return True
            except ValueError:
                return False
    def clear_text(self):
        self.text = ""
        self.is_done = False