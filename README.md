# Battleships game (WIP!)

## Design ideology
The way the game is designed here is such that the game logic is independent of the presentation code. I play to have two playable versions of the game (Terminal-based and pygame). The end goal of the project is to have these two seperate versions of the same game playable with as little duplicated code as possible, as well as much modulatity/customisation to game functionality as possible (Customisable fleets, grid sizes, etc.)

### The game is split into three files:
- game_logic.py - This is the underlying logic of the game, it handles the logic of battleship but nothing else. Running this will not result in anything. (In development)
- battleship_terminal.py - This is the version of the game designed to run in the terminal, used to make sure game_logic can be used to play a successful game of battleship. (In development)
- battleship_pygame.py - This version of the game uses pygame. I hope to have proper graphics and audio as well as all of the functionality from the terminal version. (Planned)
