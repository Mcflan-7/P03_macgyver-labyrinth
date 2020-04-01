#! /usr/bin/env python3

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# deplace items sur laby pour affichage user modifier attribut pos 
class Item:
    """Generate 3 randoms items in 
    the paths"""
    items = {}
    def __init__(self, name, laby):
        self.laby = laby 
        self.position = laby.get_random_position()
        self.name = name
        self.items[self.position] = self
   
