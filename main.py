from argparse import Namespace


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

class Ships:
    class Vessel:
        def __init__(self, length, id):
            self.length = length
            self.id = id #Not defined here, but a ship name is len (its length) num (its number of that length), so the second 4 length ship on a fleet would be len4num2
            self.hits = 0
            self.position = [0,0] #Position is always defined by the upper left most portion of the ship.
            self.orientation = "Horizontal"
        def __repr__(self):
            return self.id

    def __init__(self, ships):
        self.ships = []
        for ship_group in ships:
            for ship in range(ship_group[1]):
                self.ships.append(Ships.Vessel(ship_group[0],f"len{ship_group[0]}num{ship+1}"))

    def __repr__(self):
        toreturn = []
        for ship in self.ships:
            toreturn.append(ship.id)
        return str(toreturn)

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
        self.ships =
        self.board = Board()



game_ships = Ships(([1,3],[2,7],[4,4]))
print(repr(game_ships))
