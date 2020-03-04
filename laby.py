#! /usr/bin/env python3
"""Main file for the MacGayver Labyrinth game
MacGayver Labybinth is a game where one character
has to pick up 3 items and reach the exit 
in order to succeed"""

import random

class Laby:
    """Laby: Main class for the game
    Create several objects for the game
    """
    
    def __init__(self):
        """initialization of instances """

        self.walls = []
        self.paths = []
        self.start = []
        self.largeur = []
        self.hauteur = []
        self.end = []
        self._random_positions = None
 
    def read_from_file(self):
        """Read_from_file is reading each line of path.txt
        and return an enumerate list for wall (unauthorized path)
        or path (authorized path)
        it includes also the starting position and the exit"""
        
        with open("maps/path.txt", "r") as f:
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
                    
                                    
        # -tc- tu peux même déplacer la création de positions aléatoire ici, dès que la liste
        # -tc- paths a été initialisée.
        self._random_positions = iter(random.sample(self.paths, len(self.paths)))
                                        
    # -tc- encore mieux d'en faire une méthode
    def get_random_position(self):
        """Generate random position
        for the laby so path always changed"""
        # -tc- si self._random_positions est créer sous forme d'un itérateur, il te suffit d'utiliser next()
        # -tc- pour retourner à chaque fois la prochaine position aléatoire
        return next(self._random_positions)

def right (position):
    ligne_n, col_n = position
    return ligne_n, col_n +1
    
class Hero:
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    def __init__(self):
        self.position= (0, 0)
        self.inventory = 0
        self.won = False

    def pick_up_item(self):
        self.inventory += 1                #si hereo va sur case vide et item present, incremente +1 inventory
        if self.inventory == 3:
            print("You won !")
            self.won = True
        else:
            print("Not so fast !", self.inventory  ,"item(s) picked up, you need 3.")
    def move(self):
       pass

def test_hero_works_as_expected():
    Hero()
    h = Hero()
    h.pick_up_item()
    h.pick_up_item() 
    h.pick_up_item() 
    print("Succeed: ", h.won)
test_hero_works_as_expected()

class Item:
    """Item: To generate new items in a 
    random position and incremente 
    Macgayver's inventory """
    
    def __init__(self):
        self.items = ["Ether", "Needle", "Syringe"]
    
    

Item()
print(Item().items)

# -tc- Pour le code de test, prendre l'habitude d'utiliser une fonction également
def test_laby_works_as_expected():
    laby = Laby()
    laby.read_from_file()
    print("Départ: ", laby.start, "Exit: ", laby.end)
    print(laby.get_random_position())
    print(laby.get_random_position())
    print(laby.get_random_position())
    print("largeur: ", laby.largeur )
    print("hauteur: ", laby.hauteur )
   
# -tc- et prendre l'habitude de le lancer uniquement après cette condition (voir cours "Perfectionnez-vous en python")
if __name__ == "__main__":
    test_laby_works_as_expected()