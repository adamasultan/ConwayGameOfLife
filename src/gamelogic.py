import copy
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
    
    def sequence(self):
        def count_alives(row, col, alives = 0) -> int:
            if col == 0 and row == 0:
                if self.is_alive(row+1,col):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row+1,col+1):
                    alives+=1
                

            elif col == 0 and row == self.grid_height-1:
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row-1, col+1):
                    alives+=1
                
                    
            elif col == self.grid_width-1 and row == 0:
                if self.is_alive(row+1, col):
                    alives+=1
                
                if self.is_alive(row, col-1):
                    alives+=1
                
                if self.is_alive(row+1,col-1):
                    alives+=1
                

            elif col == self.grid_width-1 and row == self.grid_height-1:
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col-1):
                    alives+=1
                
                if self.is_alive(row-1,col-1):
                    alives+=1
                
                        # note to future, this is chekcing for squares ar col 0
            elif col == 0:
                if self.is_alive(row+1,col):
                    alives+=1
                
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row+1,col+1):
                    alives+=1
                
                if self.is_alive(row-1,col+1):
                    alives+=1
                
            elif col == self.grid_width -1:
                if self.is_alive(row+1,col):
                    alives+=1
                
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col-1):
                    alives+=1
                
                if self.is_alive(row+1,col-1):
                    alives+=1
                
                if self.is_alive(row-1,col-1):
                    alives+=1
                
            elif row == 0:
                if self.is_alive(row+1,col):
                    alives+=1
                
                if self.is_alive(row,col-1):
                    alives+=1
                
                if self.is_alive(row+1,col-1):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row+1,col+1):
                    alives+=1
                
            elif row == self.grid_height -1:
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col-1):
                    alives+=1
                
                if self.is_alive(row-1,col-1):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row-1,col+1):
                    alives+=1
                
            #start of general surrounding comparison
            else:
                if self.is_alive(row+1,col):
                    alives+=1
                
                if self.is_alive(row-1,col):
                    alives+=1
                
                if self.is_alive(row,col-1):
                    alives+=1
                
                if self.is_alive(row+1,col-1):
                    alives+=1
                
                if self.is_alive(row-1,col-1):
                    alives+=1
                
                if self.is_alive(row,col+1):
                    alives+=1
                
                if self.is_alive(row+1,col+1):
                    alives+=1
                
                if self.is_alive(row-1,col+1):
                    alives+=1
                
            return alives
        next = copy.deepcopy(self.state)
        #print(self.grid)
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                # print(self.state[0][0])
                alives = count_alives(row,col)
                #print(f"alive:{alives}  dead:{deads}")
                #print(self.state[row][col])
                #print(self.state[0][0])
                if self.state[row][col]:
                    if alives < 2:
                        next[row][col] = 0
                    elif alives > 3:
                        next[row][col] = 0
                elif self.state[row][col] == 0:
                    if alives == 3:
                        next[row][col] = 1
        #print(self.state[row][col])
        self.state = copy.deepcopy(next)