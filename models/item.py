#! /usr/bin/env python3

from .laby import Laby  
from .item import Item  
from .hero import Hero
from .move import left, right, up, down
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

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