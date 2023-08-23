import pygame
class Grid():
    def __init__(self, width=800, height=600, cell_size=40):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = self.width // self.cell_size
        self.grid_height = self.height // self.cell_size
        self.state = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.RED = (255, 64, 64)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 100, 0)

    def draw_rect(self,color, row, col):
        pygame.draw.rect(self.screen, color, (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size))

    def draw_grid(self, color):
        for row in range(self.grid_height):
            pygame.draw.lines(self.screen, color, True, ((0, row*self.cell_size), (self.width, row*self.cell_size)),1)
        for col in range(self.grid_width):
            pygame.draw.lines(self.screen, color, True, ((col*self.cell_size, 0), (col*self.cell_size, self.height)),1)
    def update_grid(self):
        #self.screen.fill(self.RED)
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.state[row][col]:
                    self.draw_rect(self.GREEN, row, col)
                else:
                    self.draw_rect(self.RED, row, col)
    def create_grid(self, game):
        # Initialize Pygame
        pygame.init()

        # Set up display
        #width, height = 800, 600
        #cell_size = 40
        pygame.display.set_caption("Conway's Game of Life")
        # Colors
        

        # Create a 2D array to represent the state of each cell
    
        # Main loop
        running = True
        self.screen.fill(self.RED)
        while running:
            #pygame.draw.rect(screen, (0,0,0), (col*cell_size, row*cell_size, cell_size, cell_size), 1)
            for event in pygame.event.get():
                # check if the curreznt event is quiting the window
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #self.update_grid()
                        #print(self.grid)
                        game.sequence()
                        #print(self.grid)
                        self.update_grid()
                        #self.draw_grid(self.BLACK)
                        #pygame.display.flip()
                # check of the current event is a click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # retrieve the coordinates of the current mouse click
                    x, y = pygame.mouse.get_pos()
                    # find each row and column that has that specific mouse click
                    # finds specific squqare
                    row = y//self.cell_size
                    col = x//self.cell_size
                    if self.state[row][col]:
                        self.state[row][col] = 0
                    else:
                        self.state[row][col] = 1

                    if self.state[row][col]:
                        self.draw_rect(self.GREEN, row, col)
                    else:
                        self.draw_rect(self.RED, row, col)
            self.draw_grid(self.BLACK)
            # pygame .display . flip updates the new grid
            pygame.display.flip()
        pygame.quit()