class GameLogic():
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.state = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]

    def change_state(self, row, col):
        if self.state[row][col]:
            self.state[row][col] = 0
        else:
            self.state[row][col] = 1

    def is_alive(self, row, col):
        return self.state[row][col] == 1