import random

class Laby:
    def __init__(self):
        self.murs = list()
        self.chemins = list()
        self.start = list()
        self.end = list()
        self.map = list()
 
    def read_from_file(self):
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
                        self.map.append((ligne_n, col_n))
                    
laby = Laby()
laby.read_from_file()
print("Départ: ", laby.start, "Exit: ", laby.end)

def random_position():
    pos = random.sample(laby.chemins, 5)
    print("Random position :", pos)
random_position()



