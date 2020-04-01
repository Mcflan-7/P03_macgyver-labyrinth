#! /usr/bin/env python3
"""
Module used to display the maze 
and move hero using the package pygame
"""
from models.laby import Laby
from models.hero import Hero
from models.item import Item
from models.move import left, right, up, down

import pygame 
import time

class MazeGame:
    """
    Maze game handle
    the display and
    the move of the hero 
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        self.title_screen = pygame.display.set_caption("Mac Gayver - Labyrinth Game!")
        self.background_img = pygame.image.load("media/images/background.jpg").convert()
        self.icon_img = pygame.image.load("media/images/mg.jpg").convert_alpha()
        self.macgayver_img = pygame.image.load("media/images/macg.png").convert_alpha()
        self.start_img = pygame.image.load("media/images/start.png").convert_alpha()
        self.end_img = pygame.image.load("media/images/end.png").convert_alpha()
        self.walls_img = pygame.image.load("media/images/walls.png").convert_alpha()
        self.paths_img = pygame.image.load("media/images/paths.png").convert_alpha()

    def display(self):
        """
        Handle the display
        """
        pygame.display.set_icon(self.icon_img)
        self.screen.blit(self.macgayver_img, (0, 0))
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.start_img, (0, 0))
        self.screen.blit(self.macgayver_img, (0, 0))
        self.screen.blit(self.walls_img, (0, 160))
        self.screen.blit(self.paths_img, (0, 370))
        self.screen.blit(self.end_img, (0, 600))
        pygame.display.flip() 

    def move_character(self):
         """
        Move MacGyver 
        inside the maze 
        """
        laby = Laby()
        hero = Hero(laby)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP :
                        print("haut")
                        hero.move(up)
                    if event.key == pygame.K_DOWN :
                        print("bas")
                        hero.move(down)
                        running = False
                    if event.key == pygame.K_LEFT :
                        print("gauche")
                        hero.move(left)
                    if event.key == pygame.K_RIGHT :
                        print("droite")
                        hero.move(right)
                print(hero.position)
                print("inventaire", hero.inventory)

def test_game_work_as_excepted():
    
    laby = Laby()
    hero = Hero(laby)
    i1, i2, i3 = Item('Aiguille', laby), Item('Ether', laby), Item('Tube', laby)
    mazegame = MazeGame()
    mazegame.display()
    mazegame.move_character()


test_game_work_as_excepted()



	
