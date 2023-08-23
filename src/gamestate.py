class GameState():
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.state = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]