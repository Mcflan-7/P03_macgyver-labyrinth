#! /usr/bin/env python3

from .laby import Laby  
from .item import Item  
from .move import left, right, up, down
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

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
    logging.debug(h.position)