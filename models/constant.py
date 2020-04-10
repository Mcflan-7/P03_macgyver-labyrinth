"""Settings for the game : windows, sprite and images."""

import pygame


pygame.display.init()
pygame.display.set_mode()

sprite_size = 32
title_screen = pygame.display.set_caption("MacGyver - Labyrinth Game")
control_keyboard = pygame.image.load(
    "media/images/control_keyboard.png"
).convert_alpha()

macgyver = pygame.image.load("media/images/macg.png").convert_alpha()
macgyver_dead = pygame.image.load("media/images/macg_dead.png").convert_alpha()
logo_screen = pygame.display.set_icon(macgyver)

walls = pygame.image.load("media/images/walls.png").convert_alpha()
paths = pygame.image.load("media/images/paths.png").convert_alpha()

needle = pygame.image.load("media/images/needle.png").convert_alpha()
tube = pygame.image.load("media/images/tube.png").convert_alpha()
ether = pygame.image.load("media/images/ether.png").convert_alpha()

start = pygame.image.load("media/images/start.png").convert_alpha()
end = pygame.image.load("media/images/end.png").convert_alpha()

won = pygame.image.load("media/images/won_game.jpg").convert_alpha()
lose = pygame.image.load("media/images/lost_game.jpg").convert_alpha()
