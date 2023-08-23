from grid import Grid
import copy

class Game():
    def __init__(self, grid = Grid()):
        self.grid = grid

    def sequence(self):
        def count_alives(row, col, alives = 0) -> int:
            if col == 0 and row == 0:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row+1][col+1]:
                    alives+=1
                

            elif col == 0 and row == self.grid.grid_height-1:
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row-1][col+1]:
                    alives+=1
                
                    
            elif col == self.grid.grid_width-1 and row == 0:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row+1][col-1]:
                    alives+=1
                

            elif col == self.grid.grid_width-1 and row == self.grid.grid_height-1:
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row-1][col-1]:
                    alives+=1
                
                        # note to future, this is chekcing for squares ar col 0
            elif col == 0:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row+1][col+1]:
                    alives+=1
                
                if self.grid.state[row-1][col+1]:
                    alives+=1
                
            elif col == self.grid.grid_width -1:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row+1][col-1]:
                    alives+=1
                
                if self.grid.state[row-1][col-1]:
                    alives+=1
                
            elif row == 0:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row+1][col-1]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row+1][col+1]:
                    alives+=1
                
            elif row == self.grid.grid_height -1:
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row-1][col-1]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row-1][col+1]:
                    alives+=1
                
            #start of general surrounding comparison
            else:
                if self.grid.state[row+1][col]:
                    alives+=1
                
                if self.grid.state[row-1][col]:
                    alives+=1
                
                if self.grid.state[row][col-1]:
                    alives+=1
                
                if self.grid.state[row+1][col-1]:
                    alives+=1
                
                if self.grid.state[row-1][col-1]:
                    alives+=1
                
                if self.grid.state[row][col+1]:
                    alives+=1
                
                if self.grid.state[row+1][col+1]:
                    alives+=1
                
                if self.grid.state[row-1][col+1]:
                    alives+=1
                
            return alives
        next = copy.deepcopy(self.grid.state)
        #print(self.grid.grid)
        for row in range(self.grid.grid_height):
            for col in range(self.grid.grid_width):
                # print(self.grid.state[0][0])
                alives = count_alives(row,col)
                #print(f"alive:{alives}  dead:{deads}")
                #print(self.grid.state[row][col])
                #print(self.grid.state[0][0])
                if self.grid.state[row][col]:
                    if alives < 2:
                        next[row][col] = 0
                    elif alives > 3:
                        next[row][col] = 0
                elif self.grid.state[row][col] == 0:
                    if alives == 3:
                        next[row][col] = 1
                #print(self.grid.state[row][col])
        self.grid.state = copy.deepcopy(next)
        #return self.grid.grid

        #print(next)

                
    
    


game = Game()
game.grid.create_grid(game)
#print(game.grid.grid)
#game.sequence()
#print(game.grid.grid)
#game.game()