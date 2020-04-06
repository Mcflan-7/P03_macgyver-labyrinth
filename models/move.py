"""Module used to move the hero in the laby."""

def right(position):
    x, y = position
    return x+1, y

def left(position):
    x, y = position
    return x-1, y

def down(position):
    x, y = position
    return x, y+1

def up(position):
    x, y = position
    return x, y-1