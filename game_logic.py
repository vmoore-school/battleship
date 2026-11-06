class Board:
    """
    This is where the board state for each player is stored. The layout works like this (3x3 board for example):
        [
        [[False,False],[False,False],[False,False]],
        [[False,False],[False,False],[False,False]],
        [[False,False],[False,False],[False,False]]
        ]

        !!! VERY IMPORTANT NOTE !!!
        THE BOARD IS ROTATED 90 DEGREES CLOCKWISE COMPARED TO HOW IT IS VISUALLY REPRESENTED ABOVE!
        REFERENCE IT AS IF IT IS NOT.
    """
    def __init__(self, x, y):
        try:
            x, y = int(x), int(y)
        except:
            raise ValueError
        if x <= 0 or y <=0:
            raise ValueError
        self.bounds = (x, y)
        self.board = []
        for column in range(x):
            self.board.append([])
        for row in range(y):
            for column in range(x):
                self.board[column].append([False,False])

    def __repr__(self):
        return str(self.board)

    def bomb(self, pos):
        if pos[0] <= self.bounds[0] and pos[1] <= self.bounds[1]:
            pass
        else:
            raise ValueError(f"Attempting to update a tile on a board must be within the board's bounds ({self.bounds[0]},{self.bounds[1]}).")
        self.board[pos[0]][pos[1]][1] = True
        if self.board[pos[0]][pos[1]][0] != False:
            return True
        else:
            return False


class Ships:
    class Vessel:
        def __init__(self, length, id):
            self.length = length
            self.id = id #Not defined here, but a ship name is len (its length) num (its number of that length), so the second 4 length ship on a fleet would be len4num2
            self.hits = 0
            self.position = [-1,-1] #Position is always defined by the upper left most portion of the ship.
            self.orientation = "H"

        def place(self):
            pass

        def __repr__(self):
            return self.id

    def __init__(self, ships):
        self.ships = {}
        for ship_group in ships:
            for ship in range(ship_group[1]):
                self.ships.update({f"len{ship_group[0]}num{ship+1}":Ships.Vessel(ship_group[0],f"len{ship_group[0]}num{ship+1}")})

    def __repr__(self):
        return str(list(self.ships))


class Player(Ships, Board):
    """
    Inputs for player class work like this:
    Name - This is cosmetic, users can have matching names
    ID - Unique for each player, must not match
    Ships - The ship definition list. Ships are defined like this [[2,2],[3,1],[4,2]] (This would generate two two lengths, one three length and two four lengths.)
    Board size - The board size to generate for the player
    """
    def __init__(self, name, id, ships, board): #Name is not expected to be unique. ID is.
        self.name = name
        self.id = id
        self.fleet = Ships(ships)
        self.board = Board(*board)

    def place_ship(self, id, pos, orientation):
        if id in list(self.fleet.ships):
            pass
        else:
            return (False, "Ship not in fleet.")
        if orientation == "H":








default_board_size = (10,10)
default_fleet = ((2,1), (3,2), (4,1), (5,1))

player1 = Player("Player 1", 1, default_fleet, default_board_size)
print(player1.fleet)
while True:
    ship_to_place = input(": ")
