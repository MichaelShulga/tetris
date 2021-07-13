import pygame

from tetris import Tetris


class TetrisController:
    def __init__(self, size):
        self.tetris = Tetris(*size)

    def update(self, delta):
        self.tetris.update(delta)
        self.main_board.render()
        self.current_figure.render()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.tetris.rotate()
            if event.key == pygame.K_DOWN:
                self.tetris.move(y=1)
            if event.key == pygame.K_LEFT:
                self.tetris.move(x=-1)
            if event.key == pygame.K_RIGHT:
                self.tetris.move(x=1)
