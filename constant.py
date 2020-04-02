"""
Setting for the game :
windows, sprite and more
"""
import pygame

pygame.display.init()
pygame.display.set_mode()

sprite_size = 32
walls = pygame.image.load("media/images/walls.png").convert_alpha()
paths = pygame.image.load("media/images/paths.png").convert_alpha()
start = pygame.image.load("media/images/start.png").convert_alpha()
end = pygame.image.load("media/images/end.png").convert_alpha()
background = pygame.image.load("media/images/background.jpg").convert_alpha()
macgyver = pygame.image.load("media/images/macg.png").convert_alpha()
