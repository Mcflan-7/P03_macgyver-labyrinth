#! /usr/bin/env python3
"""Module used to launch the game"""
from controller.maze_display import MazeGame

def main():
    game = MazeGame()
    game.start()

if __name__ == "__main__":
    main()
