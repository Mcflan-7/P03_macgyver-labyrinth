#! /usr/bin/env python3
"""Module used to display the maze
"""

import pygame

from views.hero_sprite import HeroSprite
from views.item_sprite import ItemSprite
from models.laby import Laby
from models.hero import Hero
from models.item import Item
from models.move import left, right, up, down
from models.constant import (
    sprite_size,
    walls,
    paths,
    start,
    end,
    title_screen,
    logo_screen,
    needle,
    ether,
    tube,
    control_keyboard,
    won,
    lose,
)


class MazeGame:
    """Maze game handle the display and the move of the hero."""

    def __init__(self):
        pygame.init()

        self.laby = Laby()
        self.hero = Hero(self.laby)
        self.needle = Item("needle", self.laby)
        self.ether = Item("Ether", self.laby)
        self.tube = Item("Tube", self.laby)

        self.screen = pygame.display.set_mode((480, 520))
        self.title_screen = title_screen
        self.logo_screen = logo_screen

        self.background = pygame.Surface((710, 700))
        self.background.fill((255, 255, 255))
        self.start_img = start
        self.end_img = end

        self.wall = walls

        for wall in self.laby.walls:
            x, y = wall
            self.background.blit(self.wall, (x * sprite_size, y * sprite_size))

        self.path = paths
        for path in self.laby.paths:
            x, y = path
            self.background.blit(self.path, (x * sprite_size, y * sprite_size))

        self.end_pos = end
        for end_pos in self.laby.end:
            x, y = end_pos
            self.background.blit(self.end_pos, (x * sprite_size, y * sprite_size))

        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(ItemSprite(self.needle, needle))
        self.allsprites.add(ItemSprite(self.ether, ether))
        self.allsprites.add(ItemSprite(self.tube, tube))
        self.allsprites.add(HeroSprite(self.hero))

        pygame.display.update()

    def start(self):
        """Method that launch all
        instances needed for the game and
        keep a while loop running"""
        self.running = True

        while self.running:
            font = pygame.font.Font(None, 30)
            text = font.render(f"Inventory ({self.hero.inventory})", 1, (1, 0, 0))
            control = font.render(f"Move with:", 1, (1, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(text, (10, 490))
            self.screen.blit(start, (0, 0))
            self.screen.blit(control, (320, 490))
            self.screen.blit(control_keyboard, (428, 476))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.hero.move(up)

                    elif event.key == pygame.K_DOWN:
                        self.hero.move(down)

                    elif event.key == pygame.K_RIGHT:
                        self.hero.move(right)

                    elif event.key == pygame.K_LEFT:
                        self.hero.move(left)
                    
                    elif event.key == pygame.K_RETURN or pygame.K_KP_ENTER or pygame.K_q:
                        self.running = False

            if self.hero.inventory == 3 and self.hero.position == (14, 14):
                self.screen.blit(won, (50, 200))
                self.hero.position = (14, 14)

            elif self.hero.inventory != 3 and self.hero.position == (14, 14):
                self.screen.blit(lose, (50, 200))
                self.hero.position = (14, 14)

            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.update()
