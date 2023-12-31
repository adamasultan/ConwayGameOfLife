import pygame
import time
class Gui():
    def __init__(self, game_logic, width, height, cell_size, grid_width, grid_height, on_exit_press, on_cell_press, on_next_gen_press, on_reset):
        self.game_logic = game_logic
        self.width=  width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.on_exit_press = on_exit_press
        self.on_cell_press = on_cell_press
        self.on_next_gen_press = on_next_gen_press
        self.on_reset = on_reset
        self.RED = (255, 64, 64)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 100, 0)
        self.GREY = (169, 169, 169)
        self.screen = pygame.display.set_mode((self.width, self.height+self.height*0.25))
        pygame.init()
        self.start_text_font = pygame.font.SysFont("Arial", int(self.cell_size))
        self.reset_text_font = pygame.font.SysFont("Arial", int(0.75*self.cell_size))
        self.stop_and_next_text_font = pygame.font.SysFont("Arial", int(0.55*self.cell_size))
        pygame.display.set_caption("Conway's Game of Life")
        self.screen.fill(self.RED)
        self.__draw_grid(self.BLACK)
        pygame.draw.rect(self.screen, self.GREY, ((0,self.height),(self.width, self.height)))
        self.__draw_start()
        self.__draw_reset()
        self.__draw_next() 

    def __draw_rect(self,color, row, col):
        pygame.draw.rect(self.screen, color, (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size))
    def __draw_start(self):
        pygame.draw.rect(self.screen, self.GREEN, ((0.4*self.width, self.height+self.height*0.05), (4*self.cell_size, 2*self.cell_size)))
        self.draw_text("Start", self.start_text_font, (0,0,0), 0.46*self.width, self.height+self.height*0.08)
    def __draw_reset(self):
        pygame.draw.rect(self.screen, self.GREEN, ((0.15*self.width, self.height+self.height*0.075), (2.5*self.cell_size, 1.5*self.cell_size)))
        self.draw_text("Reset", self.reset_text_font, (0,0,0), 0.17*self.width, self.height+self.height*0.09)
    def __draw_stop(self):
        pygame.draw.rect(self.screen, self.RED, ((0.4*self.width, self.height+self.height*0.05), (4*self.cell_size, 2*self.cell_size)))
        self.draw_text("Stop", self.start_text_font, (0,0,0), 0.46*self.width, self.height+self.height*0.08)
    def __draw_next(self):
        pygame.draw.rect(self.screen, self.GREEN, ((0.75*self.width, self.height+self.height*0.075), (2.5*self.cell_size, 1.5*self.cell_size)))
        self.draw_text("Next", self.reset_text_font, (0,0,0), 0.78*self.width, self.height+self.height*0.09)
    def __draw_grid(self, color):
        for row in range(self.grid_height+1):
            pygame.draw.lines(self.screen, color, True, ((0, row*self.cell_size), (self.width, row*self.cell_size)),1)
        for col in range(self.grid_width+1):
            pygame.draw.lines(self.screen, color, True, ((col*self.cell_size, 0), (col*self.cell_size, self.height)),1)
    
    def __in_grid_range(self,x,y):
        return x <= self.width and y<= self.height  
    def __in_start_stop_button_range(self,x,y):
        return x>= 0.4*self.width and x <= 0.4*self.width+4*self.cell_size and y>= self.height+self.height*0.05 and y <= self.height+self.height*0.05+2*self.cell_size
    def __in_reset_button_range(self,x,y):
        return x>= 0.15*self.width and x<= 0.15*self.width+2.5*self.cell_size and y>= self.height+self.height*0.075 and y <= self.height+self.height*0.075+1.5*self.cell_size
    def __in_next_button_range(self,x,y):
        return x>=0.75*self.width and x<=0.75*self.width+2.5*self.cell_size and y>=self.height+self.height*0.075 and y <= self.height+self.height*0.1+ 1.5*self.cell_size
    def reset_grid(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                self.__draw_rect(self.RED, row, col)
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
                if self.__in_grid_range(x,y):
                        # find each row and column that has that specific mouse click
                        # finds specific squqare
                    row = y//self.cell_size
                    col = x//self.cell_size
                    self.on_cell_press(row, col)
                if self.__in_start_stop_button_range(x,y):
                    self.__draw_stop()
                    started = True
                    while started:
                        self.on_next_gen_press()
                        self.update()
                        time.sleep(0.5)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                z,z1 = pygame.mouse.get_pos()
                                if self.__in_start_stop_button_range(z,z1):
                                    self.__draw_start()
                                    started = False
                                if self.__in_reset_button_range(z,z1):
                                    started = False
                                    self.on_reset()
                                # if self.__in_next_button_range(z,z1):
                                #     self.on_next_gen_press()
                            if event.type == pygame.QUIT:
                                started = False
                                self.on_exit_press()
                    
                    #print('clicked start')
                if self.__in_reset_button_range(x,y):
                    self.on_reset()
                # if self.__in_stop_button_range(x,y):
                #     print('clicked stop')
                if self.__in_next_button_range(x,y):
                    self.on_next_gen_press()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.on_next_gen_press()
                
    def update(self):

        self.__draw_grid(self.BLACK)
        pygame.display.flip()
    
    def draw_text(self,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img, (x,y))

    def quit(self):
        pygame.quit()