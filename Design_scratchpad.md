# File for writing about design concepts
## Game board
So, to store the board state I need a list of lists. Each cell will need to hold two pieces of information, ship ID (if the cell is "owned" by a ship) and bomb status.

Example (3x3) game board:

board = [
    [[False,False],[False,False],[False,False]],
    [[False,False],[False,False],[False,False]],
    [[False,False],[False,False],[False,False]]
]

## Ships
Not entirely sure how to implement ships and how they're stored.
My current plan is to have ship creation done like this:

player1_ships = Ships([[2,1], [1,3], [4,5]])
The above assignment would create an object with two single tile ships, one three length ship and four five length ships.

After that, use a method for placing. I'm thinking about using a subclass for storing individual method data. Dunno, something to think about later.
