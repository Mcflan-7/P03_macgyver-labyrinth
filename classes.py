#! /usr/bin/env python3
"""Module for the MacGayver Labyrinth game
classes that handle laby, hero and item"""

from functions import move
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
        """Read_from_file is reading each lines of path.txt
        and return an enumerate list for wall (unauthorized path)
        or path (authorized path) with index and value
        it includes the starting position and the exit
        and finally a method to get random position"""

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
          self.paths.extend([self.start, self.end])
        
        except FileNotFoundError:
          logging.warning("Map not found")       
                
    def get_random_position(self):
        """Generate random position
        for the laby so path always changed"""
        
        return next(self._random_positions)

class Hero:
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    def __init__(self, laby, items):
        self.laby = laby
        self.position= (0, 0)
        self.inventory = 0
        self.items = items
        self.won = False

    def move(self, direction):
        """Method used to move the hero
        in the labyrinth and test if it is
        authorized path or not """
        new_position = direction(self.position)
        if new_position in self.laby.paths: 
            self.position = new_position
            if self.position in self.items:
                self.inventory += 1

def test_hero_works_as_expected():
    """Function that test if Class Hero is creating
    new instances and if the condition is working """
    laby = Laby()
    i1, i2, i3 = Item('Aiguille', laby), Item('Ether', laby), Item('Tube', laby)
    logging.debug("%s, %s",i1.name, i1.position)
    print(i2.name, i2.position)
    print(i3.name, i3.position)
    print(Item.items)
    items = Item.items
    laby.read_from_file()
    h = Hero(laby, items)
    h.move(move.right)
    logging.debug(h.position)

def test_laby_works_as_expected():
    laby = Laby()
    laby.read_from_file()

class Item:
    """Generate 3 randoms items in 
    the paths"""
    items = {}
    def __init__(self, name, laby):
        self.laby = laby 
        self.position = laby.get_random_position()
        self.name = name
        self.items[self.position] = self
   
def test_item_works_as_expected():
    """Function that test if Class Item is creating
    new items and place them randomly 
    on the maze"""

    laby = Laby()
    i1, i2, i3 = Item('Aiguille', laby), Item('Ether', laby), Item('Tube', laby)
    logging.debug("%s, %s",i1.name, i1.position)
    print(i2.name, i2.position)
    print(i3.name, i3.position)
    print(Item.items)

if __name__ == "__main__":
    test_hero_works_as_expected()