#! /usr/bin/env python3

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class Laby:
    """Laby: Class that represent the play zone
    and the labyrinth
    """
    def __init__(self):

        self.walls = []
        self.paths = []
        self.start = []
        self.end = []
        self.width = None 
        self.height = None
        self._random_positions = None
        self.read_from_file()
 
    def read_from_file(self):
        """Read_from_file is reading each lines of path.txt and return an
        enumerate list for wall (unauthorized path) or path (authorized path)
        with index and value it includes the starting position and the exit and
        finally a method to get random position."""

        try:
          with open("maps/map1.txt", "r") as f:
            for ligne_n, ligne in enumerate(f):
                self.height = ligne_n + 1
                for col_n, col in enumerate(ligne):
                    self.width = col_n + 1
                    if col == "#":
                        self.walls.append((col_n, ligne_n))
                    elif col == ".":
                        self.paths.append((col_n, ligne_n))
                    elif col == "S":
                        self.start.append((col_n, ligne_n))
                    elif col == "X":
                        self.end.append((col_n, ligne_n))

          self._random_positions = iter(random.sample(self.paths, len(self.paths)))
          self.paths.extend(self.start) 
          self.paths.extend(self.end)
        
        except FileNotFoundError:
          logging.warning("Map not found")       
                
    def get_random_position(self):
        """Generate random position for the laby so path always changed."""
        
        return next(self._random_positions)