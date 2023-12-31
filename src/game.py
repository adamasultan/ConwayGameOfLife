from gamelogic import GameLogic
from gui import Gui
class Game():
    def __init__(self, width = 800, height = 600, cell_size = 40):
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        self.game_logic = GameLogic(self.grid_width, self.grid_height)
        self.display = Gui(self.game_logic,width, height, cell_size, self.grid_width, self.grid_height, self.on_exit_press, self.on_cell_press, self.on_next_gen_press, self.on_reset)
        self.running = False

    def start_game(self):
        self.running = True
        while self.running:
            self.display.handle_user_input()

            self.display.update()
        self.display.quit()
    def on_next_gen_press(self):
        self.game_logic.sequence()
        self.display.update_grid()

    def on_exit_press(self):
        self.running = False
    def on_cell_press(self, *args):
        row, col = args
        self.game_logic.change_state(row, col)
        self.display.update_cell(row,col)
        #print(self.game_logic.state[row][col])
    def on_reset(self):
        self.game_logic.state = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.display.reset_grid()
game = Game()
game.start_game()