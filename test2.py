import pygame
from board import Board
import copy

sprites = pygame.sprite.Group()

rect = pygame.Rect(1, 1, 1, 1)
cell_size = 20

s1 = Board(rect, cell_size, sprites)
a = copy.copy(s1)

s1.__init__(rect, cell_size)

print(a == s1)
print(sprites.sprites()[0] == s1)
print(sprites)

