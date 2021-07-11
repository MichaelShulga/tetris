import pygame

from tetris import Tetris


class TetrisController:
    def __init__(self, width, height):
        self.tetris = Tetris(width, height)

        self.main_board = pygame.sprite.Sprite()
        self.current_figure = pygame.sprite.Sprite()

    def update(self, delta):
        self.tetris.update(delta)
