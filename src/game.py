from gamelogic import GameLogic
from gui import Gui
from gamestate import GameState
class Game():
    def __init__(self, width, height, cell_size):
        grid_width = width // cell_size
        grid_height = height // cell_size
        gamestate = GameState(grid_width, grid_height)
        self.game_logic = GameLogic(gamestate)
        self.display = Gui(gamestate,width, height, cell_size, grid_width, grid_height, self.on_exit_press)
        self.running = False

    def start_game(self):
        self.running = True
        while self.running:
            self.display.handle_user_input()
            self.display.update()
        self.display.quit()

    def on_exit_press(self):
        self.running = False
game = Game(800, 600, 40)
game.start_game()