class Hero():
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
            print("You won !")
            self.won = True
        else:
            print("Not so fast !", self.inventory  ,"item(s) picked up, you need 3.")

    def move(self, direction):
        """Method used to move the hero
        in the labyrinth and test if it is
        authorized path or not """
        new_position = direction(self.position)
        #if new_position in self.laby.paths:
        self.position = new_position
