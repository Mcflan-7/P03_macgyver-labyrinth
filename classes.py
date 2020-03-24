#! /usr/bin/env python3
"""Module for the MacGayver Labyrinth game
classes that handle laby, hero and item"""

from functions import move
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#dossier en rapport avec la fonction

class Laby:
    """Laby: Class that represent the play zone
    and the labyrinth
    """
    def __init__(self):
        """initialization of instances for the laby class """

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
                        self.walls.append((ligne_n, col_n))
                    elif col == ".":
                        self.paths.append((ligne_n, col_n))
                    elif col == "S":
                        self.start.append((ligne_n, col_n))
                    elif col == "X":
                        self.end.append((ligne_n, col_n))

          self._random_positions = iter(random.sample(self.paths, len(self.paths)))
        except FileNotFoundError as e:
          logging.warning("Map not found", e)       
                
    def get_random_position(self):
        """Generate random position
        for the laby so path always changed"""
        
        return next(self._random_positions)

class Hero:
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    def __init__(self, laby):
        self.laby = laby
        self.position= (0, 0)
        self.inventory = 0
        self.won = False

    def pick_up_item(self):
        """Method used to store the number
        of item MacGayver pick up and 
        give a random position to them each time 
        we load the class  """
        
        self.inventory += 1             
        if self.inventory == 3 and self.position == "X": 
            logging.info("You won !")
            self.won = True
        else:
            logging.info("Not so fast !", self.inventory  ,"item(s) picked up, you need 3.")

    def move(self, direction):
        """Method used to move the hero
        in the labyrinth and test if it is
        authorized path or not """
        new_position = direction(self.position)
        if new_position in self.laby.paths: 
            self.position = new_position

def test_hero_works_as_expected():
    """Function that test if Class Hero is creating
    new instances and if the condition is working """
    labyrinthe = Laby() # j'instancie laby 
    labyrinthe.read_from_file()
    h = Hero(labyrinthe) # je passe en paramètre labyrinth
    h.move(move.right)
    h.move(move.up)
    h.move(move.up)
    h.move(move.up)
    h.move(move.up)
    h.move(move.up)
    h.move(move.down)
    logging.debug(h.position)
    #logging.debug(labyrinthe.paths)

def test_laby_works_as_expected():
    laby = Laby()
    laby.read_from_file()
    logging.debug("Départ: ", laby.start, "Exit: ", laby.end)

class Item:
    """Item: To generate new items 
     """
 # add item to path / randomize pos / 
    def __init__(self, name, laby):
        self.laby = laby  # j'utilise laby pour retourner une instance
        self.position = laby.get_random_position()
        self.name = name
   
def test_item_works_as_expected():
        laby = Laby()
        i1, i2, i3 = Item('Aiguille', laby), Item('Ether', laby), Item('Tube', laby)
        logging.debug(i1.position)
        logging.debug(i2.position)
        logging.debug(i3.position)
if __name__ == "__main__":
    test_item_works_as_expected()