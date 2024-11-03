from whitecir import Whitecyrcle

class Ball:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def can_move(self, board, n, t_row, t_col, b=None):
            if t_row < 1 or t_row > n or t_col < 1 or t_col > n:
                return False
            if self.row == t_row and self.col == t_col:
                return False
            for element in board:
                if element == b:
                    continue
                if element.row == t_row and element.col == t_col:
                    if isinstance(element, (Purbleballs, Redballs, Metalballs)):
                            if element.can_move(board, n, element.row+(t_row-self.row), element.col+(t_col-self.col)):
                                element.row = 2*element.row-self.row
                                element.col = 2*element.col-self.col
            return True 
#_______________________________________________________________________________________________________________________
class Purbleballs(Ball):
    def __init__(self, row , col):
        Ball.__init__(self, row, col)
    
    def move(self, board):
        for element in board.b:
            if isinstance(element, (Purbleballs, Redballs, Metalballs)):
                if element.row > self.row and element.col == self.col:
                    if element.can_move(board.b, board.n, element.row+1, element.col, self):
                        element.row +=1
                elif element.row < self.row and element.col == self.col:
                    if element.can_move(board.b, board.n, element.row-1, element.col, self):
                        element.row -=1
                elif element.row == self.row and element.col > self.col:
                    if element.can_move(board.b, board.n, element.row, element.col+1, self):
                        element.col +=1
                elif element.row == self.row and element.col < self.col:
                    if element.can_move(board.b, board.n, element.row, element.col-1, self):
                        element.col -=1
#______________________________________________________________________________________________________________________
class Redballs(Ball):
    def __init__(self, row , col):
        Ball.__init__(self, row, col)

    def move(self, board):
        for element in board.b:
            if isinstance(element, (Purbleballs, Redballs, Metalballs)):
                if element.row > self.row+1 and element.col == self.col:
                    if element.can_move(board.b, board.n, element.row-1, element.col, self):
                        element.row = element.row-1      
                elif element.row < self.row-1 and element.col == self.col:
                    if element.can_move(board.b, board.n, element.row+1, element.col, self):
                        element.row = element.row+1
                elif element.row == self.row and element.col > self.col+1:
                    if element.can_move(board.b, board.n, element.row, element.col-1, self):
                        element.col = element.col-1
                elif element.row == self.row and element.col < self.col-1:
                    if element.can_move(board.b, board.n, element.row, element.col+1, self):
                        element.col = element.col+1
#_________________________________________________________________________________
class Metalballs(Ball):
    def __init__(self, row, col):
        Ball.__init__(self, row, col)