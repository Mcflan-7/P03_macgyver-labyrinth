#! /usr/bin/env python3
"""Handle the position of the hero"""

from .item import Item

import random
import logging
import pygame


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class Hero:
    """Hero: Class hero that set some actions
    (attributs) to Macgayver and
    manage the inventory """

    def __init__(self, laby):
        self.laby = laby
        self.position = (0, 0)
        self.inventory = 0

    def move(self, direction):
        """Method used to move the hero in the labyrinth and test if it is
        authorized path or not."""
        
        new_position = direction(self.position)
        if new_position in self.laby.paths:
            self.position = new_position
            if self.position in Item.items:
                self.inventory += 1
                item = Item.items[self.position]
                del Item.items[self.position]
                Item.items[(self.inventory - 1, 15)] = item
                
            if self.position in self.laby.end:
                if self.inventory == 3:
                    print("Bravo, vous avez gagné !")
                else:
                    print("Echec, vous n'avez pas récuperé les 3 items !")
