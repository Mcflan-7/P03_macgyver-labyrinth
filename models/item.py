#! /usr/bin/env python3
"""Handle the position of the items and their behaviors."""

import random


class Item:
    """Generate 3 randoms items in the paths."""

    items = {}

    def __init__(self, name, laby):
        self.laby = laby
        self.position = laby.get_random_position()
        self.name = name
        self.items[self.position] = self
