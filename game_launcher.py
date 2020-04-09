#! /usr/bin/env python3
"""Module used to display the maze and move hero using the package pygame.
Will launch the game once the modul is started
"""
from controller.maze_display import MazeGame

def main():
    game = MazeGame()
    game.start()


if __name__ == "__main__":
    main()
