class Board:
    def __init__(self, x, y):
        self.board = []
        for column in range(x):
            self.board.append([])
        for row in range(y):
            for column in range(x):
                self.board[row].append([False,False])

        tung = [
            [[False,False],[False,False],[False,False]], # [left]
            [[False,False],[False,False],[False,False]], # x
            [[False,False],[False,False],[False,False]]  # [right]
        ]

        if self.board == tung:
            print("tung")

gameboard = Board(2,3)

# down <-----------------y---------------------> up
