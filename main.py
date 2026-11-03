from multiprocessing import Value

from reference_boards import tung34, tung43

class Board:
    def __init__(self, x, y):
        try:
            int(x)
            int(y)
        except:
            raise ValueError
        if x <= 0 or y <=0:
            raise ValueError

        self.board = []
        for column in range(x):
            self.board.append([])
        for row in range(y):
            for column in range(x):
                self.board[column].append([False,False])
    def __repr__(self):
        return str(self.board)

board1 = Board(4,3)
board2 = Board(3,4)

testboard = Board(1,1)
print(testboard)

if repr(board1) == repr(tung43):
    print("Test pass")
if repr(board2) == repr(tung34):
    print("Test pass")
