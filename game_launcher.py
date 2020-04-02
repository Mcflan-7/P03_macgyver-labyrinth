#! /usr/bin/env python3
"""
Module used to display the maze 
and move hero using the package pygame
"""

from models.laby import Laby
from models.hero import Hero
from models.item import Item
from models.move import left, right, up, down
from constant import sprite_size, macgyver, walls, background, paths, start, end

import pygame

class MazeGame:
    """
    Maze game handle
    the display and
    the move of the hero 
    """
    def __init__(self):
        pygame.init()

        self.laby = Laby()
        self.hero = Hero(self.laby)

        self.screen = pygame.display.set_mode((500, 500))

        self.background = pygame.Surface((700, 700))
        self.background.fill((255, 255, 255))
        self.start_img = pygame.image.load("media/images/start.png").convert_alpha()
        self.end_img = pygame.image.load("media/images/end.png").convert_alpha()
        
        self.wall = walls
        for wall in self.laby.walls:
            x, y = wall
            self.background.blit(self.wall, (x * sprite_size, y * sprite_size))

        self.path = paths
        for path in self.laby.paths:
            x, y = path
            self.background.blit(self.path, (x * sprite_size, y * sprite_size))

        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(HeroSprite(self.hero))

        pygame.display.update()

    def start(self):
        self.running = True
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.start_img, (0, 0))
            self.screen.blit(self.end_img, (445, 446))

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

            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.update()


class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.image =  macgyver
        self.rect = self.image.get_rect()

        self.update()

    def update(self):
        x, y = self.hero.position
        self.rect.x = x * sprite_size
        self.rect.y = y * sprite_size


def main():
    game = MazeGame()
    game.start()

if __name__ == "__main__":
    main()