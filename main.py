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
            self.id = id
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

game_ships = Ships(([1,3],[2,7],[4,4]))
print(repr(game_ships))
