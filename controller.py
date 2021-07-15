import pygame

from model import TetrisModel
from view import TetrisBoard, FigureBoard


class TetrisController:
    def __init__(self, size, tetris_rect, figure_rect, cell_size, group):
        self.model = TetrisModel(*size)

        self.tetris_board = TetrisBoard(tetris_rect, cell_size, group)
        self.figure_board = FigureBoard(figure_rect, cell_size, group)

    def update(self, delta):
        self.model.update(delta)
        self.tetris_board.render(self.model.board)
        self.figure_board.render(self.model.next)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.model.rotate()
            if event.key == pygame.K_DOWN:
                self.model.move(y=1)
            if event.key == pygame.K_LEFT:
                self.model.move(x=-1)
            if event.key == pygame.K_RIGHT:
                self.model.move(x=1)

            if event.key == pygame.K_SPACE:
                self.model.start()

    def resize(self, tetris_rect, figure_rect, cell_size):
        self.tetris_board.__init__(tetris_rect, cell_size)
        self.figure_board.__init__(figure_rect, cell_size)
