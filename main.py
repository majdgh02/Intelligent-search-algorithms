from board import *
from ball import *
from whitecir import *


b1 = Board(4, [Purbleballs(3,1),Metalballs(2,3), Whitecyrcle(2,2), Whitecyrcle(2,4)])
b2 = Board(5, [Purbleballs(5,1), Metalballs(2,3), Metalballs(3,2), Metalballs(3,4),Metalballs(4,3), Whitecyrcle(1,3), Whitecyrcle(3,1), Whitecyrcle(3,3), Whitecyrcle(3,5), Whitecyrcle(5,3)])
b3 = Board(4, [Purbleballs(3,1), Metalballs(2,3), Whitecyrcle(1,4), Whitecyrcle(3,4)])
b4 = Board(5, [Purbleballs(3,2), Metalballs(2,3), Metalballs(4,3), Whitecyrcle(1,2), Whitecyrcle(1,4), Whitecyrcle(5,3)])
b5 = Board(4, [Purbleballs(4,2), Metalballs(2,1), Metalballs(3,1), Metalballs(2,3), Metalballs(3,3), Whitecyrcle(1,1), Whitecyrcle(1,3), Whitecyrcle(2,1), Whitecyrcle(2,3), Whitecyrcle(4,1)])
b6 = Board(5, [Purbleballs(4,1), Metalballs(3,2), Metalballs(3,4), Whitecyrcle(2,4), Whitecyrcle(3,3), Whitecyrcle(3,4)])
b7 = Board(5, [Purbleballs(3,2), Metalballs(2,1), Metalballs(3,1), Metalballs(4,2), Metalballs(4,3), Whitecyrcle(1,1), Whitecyrcle(2,1), Whitecyrcle(3,4), Whitecyrcle(4,3), Whitecyrcle(5,4)])
b8 = Board(5, [Purbleballs(3,1), Metalballs(2,2), Metalballs(2,3), Whitecyrcle(1,1), Whitecyrcle(1,3), Whitecyrcle(3,3)])
b9 = Board(7, [Purbleballs(4,1), Metalballs(4,4), Metalballs(4,6), Whitecyrcle(4,2), Whitecyrcle(4,4), Whitecyrcle(4,7)])
b10 = Board(4, [Purbleballs(1,1), Metalballs(3,3), Metalballs(3,4), Metalballs(4,2), Whitecyrcle(2,2), Whitecyrcle(2,4), Whitecyrcle(4,1), Whitecyrcle(4,4)])
b11 = Board(5, [Redballs(2,3), Metalballs(1,1), Metalballs(1,5), Whitecyrcle(1,2), Whitecyrcle(1,3), Whitecyrcle(1,4)])
b12 = Board(5, [Redballs(4,2), Metalballs(1,1), Metalballs(2,1), Metalballs(5,4), Whitecyrcle(2,1), Whitecyrcle(3,1), Whitecyrcle(5,1), Whitecyrcle(5,3)])
b13 = Board(6, [Redballs(3,4), Metalballs(1,1), Metalballs(1,5), Metalballs(1,6), Whitecyrcle(1,4), Whitecyrcle(1,5), Whitecyrcle(2,2), Whitecyrcle(3,2)])
b14 = Board(4, [Redballs(4,4), Metalballs(1,4), Metalballs(3,1), Metalballs(4,1), Whitecyrcle(2,1), Whitecyrcle(2,3), Whitecyrcle(3,2), Whitecyrcle(3,3)])
b15 = Board(5, [Purbleballs(2,3), Redballs(3,3), Metalballs(1,2), Metalballs(1,4), Whitecyrcle(1,1), Whitecyrcle(1,2), Whitecyrcle(2,5), Whitecyrcle(3,5)])
b16 = Board(5, [Purbleballs(3,5), Redballs(3,1), Metalballs(2,3), Metalballs(4,3), Whitecyrcle(1,4), Whitecyrcle(1,5), Whitecyrcle(5,1), Whitecyrcle(5,4)])
b17 = Board(4, [Purbleballs(4,4), Redballs(1,1), Metalballs(1,3), Metalballs(3,1), Whitecyrcle(2,2), Whitecyrcle(2,4), Whitecyrcle(3,3), Whitecyrcle(4,2)])
b18 = Board(6, [Purbleballs(5,4), Redballs(5,3), Metalballs(1,4), Metalballs(3,1), Metalballs(3,6), Whitecyrcle(2,4), Whitecyrcle(3,2), Whitecyrcle(3,3), Whitecyrcle(3,4), Whitecyrcle(3,6)])
b19 = Board(5, [Purbleballs(1,3), Redballs(3,3), Metalballs(1,2), Metalballs(1,4), Metalballs(5,2), Metalballs(5,4), Whitecyrcle(2,1), Whitecyrcle(2,5), Whitecyrcle(3,2), Whitecyrcle(4,1), Whitecyrcle(4,3), Whitecyrcle(4,5)])
b20 = Board(5, [Purbleballs(5,3), Redballs(5,4), Metalballs(1,2), Metalballs(1,3), Metalballs(5,1), Whitecyrcle(1,2), Whitecyrcle(1,4), Whitecyrcle(2,1), Whitecyrcle(3,1), Whitecyrcle(4,1)])

try:
    while True:
        print("Leveles 1->20")
        level = int(input("Chose a Level: "))
        if level == 1:
            board = b1
        elif level == 2:
            board = b2
        elif level == 3:
            board = b3
        elif level == 4:
            board = b4
        elif level == 5:
            board = b5
        elif level == 6:
            board = b6
        elif level == 7:
            board = b7
        elif level == 8:
            board = b8
        elif level == 9:
            board = b9
        elif level == 10:
            board = b10
        elif level == 11:
            board = b11
        elif level == 12:
            board = b12
        elif level == 13:
            board = b13
        elif level == 14:
            board = b14
        elif level == 15:
            board = b15
        elif level == 16:
            board = b16
        elif level == 17:
            board = b17
        elif level == 18:
            board = b18
        elif level == 19:
            board = b19
        elif level == 20:
            board = b20
            board.Printboard()
        print("if you want to play this game enter p")
        print("if you want to solve this game in BFS enter b")
        print("if you want to solve this game in DFS enter d")
        solve_s = input("input: ")
        if solve_s == "p":
            while True:
                board.Printboard()
                row = int(input("Enter the ball row "))
                col = int(input("Enter the ball col "))
                t_row = int(input("Enter the distination row "))
                t_col = int(input("Enter the distination col "))
                b1 = board.move(row, col, t_row, t_col)
                if b1 is not False:
                    board = b1
                    status = board.solved()
                    if status is True:
                        break
            board.Printboard()
            print(Fore.CYAN + "''Congratulations''")
            print(Fore.RESET + "  ")
        elif solve_s == "b":
            board.BFS_Search()
        elif solve_s == "d":
            board.DFS_Search()
except ValueError:
            print("Invaild Input!, Please Enter integers only")