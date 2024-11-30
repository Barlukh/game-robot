## Introduction
2D game written with the help of Pygame library. It is a simple collection game, where a player controls a robot and tries to collect coins.
If the player collides with a monster, the game ends. This is a final submission for the Advanced Python course in the MOOC 2024 teaching series.

## Functionality
- The player controls a robot and is being chased by a monster. Score increases based on the coins collected.
- If the monster touches the player, the game is over and the player can restart the game.
- There is no winning condition, only collecting more coins.
- Operate the game with arrow keys. Spacebar starts a new game.
- The code is separated into functions. Coin and entities have their own classes.
- Images have their own rectangles.
- Collision is detected based on the drawn rectangle for the given image.

## Installation
No installation. Must be launched through a Python interpreter. The game opens its own window after the code is executed. Execution happens through the game_start() function.