from ball import Purbleballs, Redballs, Metalballs
from whitecir import Whitecyrcle
from colorama import Fore


class Board :
    def __init__(self, n, board ):
        self.n = n
        self.b = board
#_________________________________________________________________________________
    def Printboard(self): 
        print(Fore.WHITE + " ", end=" ")
        for x in range(1,self.n+1):
            print (x, end=" ")
        print()
        for i in range(1,self.n+1): 
            print(i, end=" ")
            for j in range(1,self.n+1):
                printed = False 
                for element in self.b: 
                    if element.row == i and element.col == j: 
                        if isinstance(element, Purbleballs):
                            for e in self.b:
                                status = False
                                if isinstance(e, Whitecyrcle) and e.row == element.row and e.col == element.col:
                                    status = True
                                    print(Fore.MAGENTA + '@', end=" ")
                                    break
                            if  status is False:
                                print(Fore.MAGENTA + 'a', end=" ") 
                        elif isinstance(element, Redballs):
                            for e in self.b:
                                status = False
                                if isinstance(e, Whitecyrcle) and e.row == element.row and e.col == element.col:
                                    status = True
                                    print(Fore.RED + '@', end=" ")
                                    break
                            if  status is False:
                                print(Fore.RED + 'a', end=" ") 
                        elif isinstance(element, Metalballs):
                            for e in self.b:
                                status = False
                                if isinstance(e, Whitecyrcle) and e.row == element.row and e.col == element.col:
                                    status = True
                                    print(Fore.LIGHTBLACK_EX + '@', end=" ")
                                    break
                            if  status is False:
                                print(Fore.LIGHTBLACK_EX + 'a', end=" ") 
                        elif isinstance(element, Whitecyrcle):
                            print(Fore.LIGHTWHITE_EX + 'O', end=" ") 
                        printed = True
                        break
                if not printed: 
                    print(Fore.BLACK + '0', end=" ") 
                    print(Fore.WHITE + "", end="")
            print()
#____________________________________________________________________________________
    def solved (self):
        Whitecyrcles = []
        for element in self.b:
            if isinstance(element, Whitecyrcle):
                Whitecyrcles.append(element) 
        status = False
        for cyrcle in Whitecyrcles:
            status = False
            for e in self.b:
                if not isinstance(e, Whitecyrcle):
                    if cyrcle.row == e.row and cyrcle.col == e.col:
                        status = True
                        break
            if status == False:
                break
        return status
#_____________________________________________________________________________________
    def can_move(self, t_row, t_col, c_row, c_col):
        ball = None
        for element in self.b:
            if element.row == c_row and element.col == c_col :
                ball = element 
                break
        if ball is None:
            return None
        if (isinstance(ball, Redballs) or isinstance(ball, Purbleballs)):
            if t_row < 1 or t_row > self.n or t_col < 1 or t_col > self.n:
                return None
            if c_row == t_row and c_col == t_col:
                return None
            for element in self.b:
                if element.row == t_row and element.col == t_col:
                    if isinstance(element, Redballs) or isinstance(element, Purbleballs) or isinstance(element, Metalballs):
                        return None
            return ball 
        else:
            return None
#_______________________________________________________________________________________
    def move(self, row, col, t_row, t_col):
            ball = self.can_move(t_row, t_col, row, col)
            if ball is None:
                print("This is not a correct move")
                return False
            new_board = []
            for element in self.b:
                if isinstance(element, Purbleballs):
                    if element.row == ball.row and element.col == ball.col:
                        p1 = Purbleballs(t_row, t_col)
                        new_board.insert(0, p1)
                        rball = p1
                    else:
                        p = Purbleballs(element.row, element.col)
                        new_board.insert(0, p)
                elif isinstance(element, Redballs):
                    if element.row == ball.row and element.col == ball.col:
                        r1 = Redballs(t_row, t_col)
                        new_board.insert(0, r1)
                        rball = r1
                    else:
                        r = Redballs(element.row, element.col)
                        new_board.insert(0, r)
                elif isinstance(element, Metalballs):
                    m = Metalballs(element.row, element.col)
                    new_board.insert(0, m)
                elif isinstance(element, Whitecyrcle):
                    w = Whitecyrcle(element.row, element.col)
                    new_board.append(w)
            b1 = Board(self.n, new_board)
            rball.move(b1)
            return b1
#_________________________________________________________________________
    @staticmethod
    def is_equal(board1, board2):
        if board1.n == board2.n:
            for element in board1.b:
                status = False
                for e in board2.b:
                    if element.row == e.row and element.col == e.col:
                        if isinstance(element, Redballs) and isinstance(e, Redballs):
                            status = True
                            break
                        if isinstance(element, Purbleballs) and isinstance(e, Purbleballs):
                            status = True
                            break
                        if isinstance(element, Metalballs) and isinstance(e, Metalballs):
                            status = True
                            break
                        if isinstance(element, Whitecyrcle) and isinstance(e, Whitecyrcle):
                            status = True
                            break
                if status == False:
                    break
            return status
        else:
            return False
#____________________________________________________________________________________

    def av_status(self, ball):
        if isinstance(ball, (Purbleballs, Redballs)):
            status = []
            for i in range(1, self.n+1):
                for j in range(1, self.n+1):
                    board = self.move(ball.row, ball.col, i, j)
                    if board is not False:
                        status.insert(0, board)
            return status
