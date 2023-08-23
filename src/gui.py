import pygame
class Gui():
    def __init__(self, gamestate, width, height, cell_size, grid_width, grid_height, on_exit_press):
        self.gamestate = gamestate
        self.width=  width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.on_exit_press = on_exit_press
        self.RED = (255, 64, 64)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 100, 0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")
        self.screen.fill(self.RED)

    def draw_rect(self,color, row, col):
        pygame.draw.rect(self.screen, color, (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size))

    def draw_grid(self, color):
        for row in range(self.grid_height):
            pygame.draw.lines(self.screen, color, True, ((0, row*self.cell_size), (self.width, row*self.cell_size)),1)
        for col in range(self.grid_width):
            pygame.draw.lines(self.screen, color, True, ((col*self.cell_size, 0), (col*self.cell_size, self.height)),1)

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_exit_press()
    def update(self):

        self.draw_grid(self.BLACK)
        pygame.display.flip()
    
    def quit(self):
        pygame.quit()