"""
This test serves as an overarching test of all functions that'd be used in a game by the game_logic library (made by me).

I might make more tests, not sure yet. TBD.
"""

import game_logic as bsgl
import random

# Default game details
default_board_size = (10,10)
default_fleet = ((2,1), (3,2), (4,1), (5,1))

# Create players
players = (bsgl.Player("Player 1", 1, default_fleet, default_board_size), bsgl.Player("Player 2", 2, default_fleet, default_board_size))

# Place fleet
for player in players:
    for vessel in list(player.fleet.ships):
        while True:

            xpos = random.randint(0,11)
            ypos = random.randint(0,11)
            orient = random.randint(0,1)
            if orient == 1:
                orient = "H"
            else:
                orient = "V"

            if player.place_ship(vessel,(xpos,ypos),orient):
                break
            else:
                pass
print("Place vessels COMPLETE")

while True:
    for player in players:
        pass
