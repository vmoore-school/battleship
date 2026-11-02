# File for writing about design concepts
## Game board
So, to store the board state I need a list of lists. Each cell will need to hold two pieces of information, ship ID (if the cell is "owned" by a ship) and bomb status.

Example (3x3) game board:

board = [
    [[False,False],[False,False],[False,False]],
    [[False,False],[False,False],[False,False]],
    [[False,False],[False,False],[False,False]]
]
