import pygame

class Canvas:
    def __init__(self, width, height, grid_size, max_history_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.max_history_size = max_history_size
        self.white = (255, 255, 255)
        self.pen_colour = (0, 0, 0)
        self.grid_color = (200, 200, 200)

        self.screen = pygame.Surface((width, height))
        self.pixels = [[self.white for _ in range(width // grid_size)] for _ in range(height // grid_size)]
        self.history = []
        self.history_index = -1
        self.drawing = False

    def save_history(self):
        if self.history_index < len(self.history) - 1:
            self.history = self.history[: self.history_index + 1]

        self.history.append([row[:] for row in self.pixels])

        if len(self.history) > self.max_history_size:
            self.history.pop(0)

    def toggle_pixel_color(self, x, y, color):
        grid_x = x // self.grid_size
        grid_y = y // self.grid_size
        self.pixels[grid_y][grid_x] = color

    def draw(self, screen):
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                pygame.draw.rect(screen, color, (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))

        self.draw_grid(screen)

    def draw_grid(self, screen):
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(screen, self.grid_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(screen, self.grid_color, (0, y), (self.width, y))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.save_history()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.toggle_pixel_color(mouse_x, mouse_y, self.pen_colour if event.button == 1 else self.white)
            self.drawing = True

        elif event.type == pygame.MOUSEMOTION:
            if self.drawing:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.toggle_pixel_color(mouse_x, mouse_y, self.pen_colour if pygame.mouse.get_pressed()[0] else self.white)

        elif event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if self.history_index > 0:
                    self.history_index -= 1
                    self.pixels = [row[:] for row in self.history[self.history_index]]

            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if self.history_index < len(self.history) - 1:
                    self.history_index += 1
                    self.pixels = [row[:] for row in self.history[self.history_index]]

            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.save_canvas_image()

    def save_canvas_image(self):
        temp_surface = pygame.Surface((self.width, self.height))
        temp_surface.fill(self.white)

        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                pygame.draw.rect(temp_surface, color, (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))

        pygame.image.save(temp_surface, "pixel_art.png")
