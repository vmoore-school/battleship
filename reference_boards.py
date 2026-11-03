#For use in python to test board code

tung43 = [ #Reference 4,3 board
    [[False,False],[False,False],[False,False]], # [left]
    [[False,False],[False,False],[False,False]], # x
    [[False,False],[False,False],[False,False]],
    [[False,False],[False,False],[False,False]]  # [right]
    ]

tung34 = [ #Reference 3,4 board
    [[False,False],[False,False],[False,False],[False,False]], # [left]
    [[False,False],[False,False],[False,False],[False,False]], # x
    [[False,False],[False,False],[False,False],[False,False]] # [right]
    ]

class Ships:
    class Vessel:
        def __init__(self, length):
            self.length = length
            self.name = "name" #Need to think of a proper vessel naming system
            self.hits = 0
    def __init__(self, ships):
        for vessel in ships:
