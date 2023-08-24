import pygame
class Gui():
    def __init__(self, game_logic, width, height, cell_size, grid_width, grid_height, on_exit_press, on_cell_press, on_next_gen_press):
        self.game_logic = game_logic
        self.width=  width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.on_exit_press = on_exit_press
        self.on_cell_press = on_cell_press
        self.on_next_gen_press = on_next_gen_press
        self.RED = (255, 64, 64)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 100, 0)
        self.screen = pygame.display.set_mode((self.width, self.height+self.height*0.25))
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")
        self.screen.fill(self.RED)
        self.__draw_grid(self.BLACK)
        pygame.draw.rect(self.screen, self.BLACK, ((0,self.height),(self.width, self.height)))

    def __draw_rect(self,color, row, col):
        pygame.draw.rect(self.screen, color, (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size))

    def __draw_grid(self, color):
        for row in range(self.grid_height+1):
            pygame.draw.lines(self.screen, color, True, ((0, row*self.cell_size), (self.width, row*self.cell_size)),1)
        for col in range(self.grid_width+1):
            pygame.draw.lines(self.screen, color, True, ((col*self.cell_size, 0), (col*self.cell_size, self.height)),1)
    

    def update_grid(self):
        #self.screen.fill(self.RED)
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.game_logic.is_alive(row,col):
                    self.__draw_rect(self.GREEN, row, col)
                else:
                    self.__draw_rect(self.RED, row, col)

    def update_cell(self, row, col):
        if self.game_logic.is_alive(row,col):
            self.__draw_rect(self.GREEN, row, col)
        else:
            self.__draw_rect(self.RED, row, col)

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_exit_press()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                    # find each row and column that has that specific mouse click
                    # finds specific squqare
                row = y//self.cell_size
                col = x//self.cell_size
                self.on_cell_press(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.on_next_gen_press()
                
    def update(self):

        self.__draw_grid(self.BLACK)
        pygame.display.flip()
    
    
    def quit(self):
        pygame.quit()