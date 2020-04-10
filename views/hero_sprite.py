"""Module used to display and move the hero using the package pygame.
"""
import pygame

from models.constant import sprite_size, macgyver


class HeroSprite(pygame.sprite.Sprite):
    """Method handling the sprite
    for the hero"""

    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.image = macgyver
        self.rect = self.image.get_rect()

        self.update()

    def update(self):
        """Updating the
        position and the sprite"""
        x, y = self.hero.position
        self.rect.x = x * sprite_size
        self.rect.y = y * sprite_size
