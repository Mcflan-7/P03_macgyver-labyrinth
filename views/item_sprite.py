import pygame
from models.constant import sprite_size

class ItemSprite(pygame.sprite.Sprite):
    """Method handling the sprite
    for the items"""

    def __init__(self, item, image):
        super().__init__()
        self.item = item
        self.image = image
        self.rect = self.image.get_rect()

        self.update()

    def update(self):
        """Updating the 
        position and the sprite"""
        x, y = self.item.position
        self.rect.x = x * sprite_size
        self.rect.y = y * sprite_size