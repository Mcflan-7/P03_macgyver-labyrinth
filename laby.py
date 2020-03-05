#! /usr/bin/env python3
"""Main file for the MacGayver Labyrinth game
MacGayver Labybinth is a game where one character
has to pick up 3 items and reach the exit 
in order to succeed"""

import random

# -tc- Je ne pense pas que Laby soit la classe principale du jeu qui sera plutôt la 
# -tc- la classe Game ou Application. Laby a comme unique responsabilité de
# -tc- représenter le labyrinthe et sa structure.
class Laby:
    """Laby: Main class for the game
    Create several objects for the game
    """
    
    def __init__(self):
        """initialization of instances for the laby class """

        self.walls = []
        self.paths = []
        self.start = []
        # -tc- pourquoi une liste? La largeur (width) est un entier
        self.largeur = []
        # -tc- pourquoi une liste? La hauteur (height) est un entier
        self.hauteur = []
        self.end = []
        self._random_positions = None
 
    def read_from_file(self):
        """Read_from_file is reading each lines of path.txt
        and return an enumerate list for wall (unauthorized path)
        or path (authorized path) with index and value
        it includes the starting position and the exit
        and finally a method to get random position"""
        
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
                                        
    def get_random_position(self):
        """Generate random position
        for the laby so path always changed"""
        
        return next(self._random_positions)
    
class Hero:
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    # -tc- probablement que MacGyver devrait recevoir une instance de Laby en argument
    # -tc- de son constructeur.
    def __init__(self, laby):
        # -tc- La position de départ est donnée par l'attribut start de laby
        self.position= (0, 0)
        self.inventory = 0
        self.won = False

    def pick_up_item(self):
        """Method used to store the number
        of item MacGayver pick up and 
        give a random position to them each time 
        we load the class  """
        
        self.inventory += 1             
        if self.inventory == 3: # -tc- Non, car il faut rejoindre la sortie avant de gagner
            print("You won !")
            self.won = True
        else:
            print("Not so fast !", self.inventory  ,"item(s) picked up, you need 3.")
   
    def move(self): # -tc- la méthode move doit probablement prendre en paramètre la direction du déplacement
        """Method used to move MacGayver
        on the map """
        new_move = self.position # -tc- self.position donne la position actuelle, pas la nouvelle 
        if new_move in self.laby.paths: # -tc- du coup, il faut que ton constructeur enregistre laby en attribut
            self.position = new_move

def test_hero_works_as_expected():
    """Function that test if Class Hero is creating
    new instances and if the condition is working """
    Hero()
    h = Hero()
    h.pick_up_item()
    h.pick_up_item() 
    h.pick_up_item() 
    print("Succeed: ", h.won)

class Item:
    """Item: To generate new items in a 
    random position and incremente 
    Macgayver's inventory """
    
    # -tc- Une classe Item représente un item, pas 3
    def __init__(self):
        self.items = ["Ether", "Needle", "Syringe"]
    
Item()
print(Item().items)

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
    test_laby_works_as_expected()
    test_hero_works_as_expected()
