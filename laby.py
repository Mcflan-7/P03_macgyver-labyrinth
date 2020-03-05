#! /usr/bin/env python3
"""file for the MacGayver Labyrinth game
that handle the laby and the methods 
link to it"""

import random

class Laby:
    """Laby: Class that represent the play zone
    and the labyrinth
    """
    def __init__(self):
        """initialization of instances for the laby class """

        self.walls = []
        self.paths = []
        self.start = []
        self.largeur = 0
        self.hauteur = 0
        self.end = []
        self._random_positions = None
 
    def read_from_file(self):
        """Read_from_file is reading each lines of path.txt
        and return an enumerate list for wall (unauthorized path)
        or path (authorized path) with index and value
        it includes the starting position and the exit
        and finally a method to get random position"""

        try:
          with open("maps/map1.txt", "r") as f:
            for ligne_n, ligne in enumerate(f):
                self.hauteur = ligne_n
                for col_n, col in enumerate(ligne):
                    self.largeur = col_n
                    if col == "#":
                        self.walls.append((ligne_n, col_n))
                    elif col == ".":
                        self.paths.append((ligne_n, col_n))
                    elif col == "S":
                        self.start.append((ligne_n, col_n))
                    elif col == "X":
                        self.end.append((ligne_n, col_n))
          self._random_positions = iter(random.sample(self.paths, len(self.paths)))
        except:
          print("Map not loaded")      
                                        
    def get_random_position(self):
        """Generate random position
        for the laby so path always changed"""
        
        return next(self._random_positions)

class Hero():
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    def __init__(self):
        self.position= (0, 0)
        self.pos_x = 0
        self.pos_y = 0
        self.inventory = 0
        self.won = False

    def pick_up_item(self):
        """Method used to store the number
        of item MacGayver pick up and 
        give a random position to them each time 
        we load the class  """
        
        self.inventory += 1             
        if self.inventory == 3 and self.position == "X": 
            print("You won !")
            self.won = True
        else:
            print("Not so fast !", self.inventory  ,"item(s) picked up, you need 3.")

    def move(self, direction):
        """Method used to move the hero
        in the labyrinth and test if it is
        authorized path or not """
        
        if direction == 'down':
            self.pos_x += 1
            print("Move down")

        elif direction == 'up':
            self.pos_x -= 1
            print("Move up")

        elif direction == 'left':
            self.pos_y -= 1
            print("Move left")

        elif direction == 'right':
            self.pos_y += 1
            print("Move right")

def test_hero_works_as_expected():
    """Function that test if Class Hero is creating
    new instances and if the condition is working """
    Hero()
    h = Hero()
    h.move("right")
    h.move("left")
    h.move("left")
    h.move("left")
    h.move("down")
    print(h.pos_x, h.pos_y)
  

class Item:
    """Item: To generate new items in a 
    random position and incremente 
    Macgayver's inventory """
 
    def __init__(self, item):
        self.items = item

def test_laby_works_as_expected():
    laby = Laby()
    laby.read_from_file()
    print("Départ: ", laby.start, "Exit: ", laby.end)
    print(laby.get_random_position())
    print(laby.get_random_position())
    print(laby.get_random_position())
    print("largeur: ", laby.largeur )
    print("hauteur: ", laby.hauteur )
   
if __name__ == "__main__":
  
  test_hero_works_as_expected()
