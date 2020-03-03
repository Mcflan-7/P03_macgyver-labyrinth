"""Ajouter une docstring ici."""

import random

# -tc- Traduire éventuellement chemins et murs ent paths et walls. map ne sert à rien

class Laby:
    """Ajouter une docstring ici."""
    
    def __init__(self):
        """Ajouter une docstring ici."""
        # -tc- de manière plus idiomatique, une liste vide se crée avec des crochets
        self.murs = []
        self.chemins = list()
        self.start = list()
        self.end = list()
        self.map = list() # -tc- inutile
        self._random_positions = None
 
    def read_from_file(self):
        """Ajouter une docstring ici."""
        with open("maps/path.txt", "r") as f:
            for ligne_n, ligne in enumerate(f):
                for col_n, col in enumerate(ligne):
                    if col == "#":
                        self.murs.append((ligne_n, col_n))
                    elif col == ".":
                        self.chemins.append((ligne_n, col_n))
                    elif col == "S":
                        self.start.append((ligne_n, col_n))
                    elif col == "X":
                        self.end.append((ligne_n, col_n))
                    elif col :
                        self.map.append((ligne_n, col_n)) # -tc- inutile
                                    
        # -tc- tu peux même déplacer la création de positions aléatoire ici, dès que la liste
        # -tc- chemins a été initialisée.
        self._random_positions = iter(random.sample(self.chemins, len(self.chemins)))
                                        
    # -tc- encore mieux d'en faire une méthode
    def get_random_position(self):
        """Ajouter une docstring ici."""
        # -tc- si self._random_positions est créer sous forme d'un itérateur, il te suffit d'utiliser next()
        # -tc- pour retourner à chaque fois la prochaine position aléatoire
        return next(self._random_positions)

# -tc- Pour le code de test, prendre l'habitude d'utiliser une fonction également
def test_laby_works_as_expected():
    laby = Laby()
    laby.read_from_file()
    print("Départ: ", laby.start, "Exit: ", laby.end)
    print(laby.get_random_position())
    print(laby.get_random_position())
    print(laby.get_random_position())
    
    
# -tc- et prendre l'habitude de le lancer uniquement après cette condition (voir cours "Perfectionnez-vous en python")
if __name__ == "__main__":
    test_laby_works_as_expected()



