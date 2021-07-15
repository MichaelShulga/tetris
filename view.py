import pygame

from board import Board
from config import BORDER

PALETTE = {0: pygame.Color("black"),
           1: pygame.Color("red"),
           2: pygame.Color("blue"),
           3: pygame.Color("orange"),
           4: pygame.Color("yellow"),
           5: pygame.Color("aquamarine"),
           6: pygame.Color("brown"),
           7: pygame.Color("ivory")
           }


class TetrisBoard(Board):
    def get_surface(self, surface, board) -> pygame.Surface:
        pygame.draw.rect(surface, PALETTE[1], surface.get_rect(), BORDER)
        for y, line in enumerate(board):
            for x, cell in enumerate(line):
                if cell:
                    pygame.draw.rect(surface, PALETTE[cell],
                                     (x * self.cell_size + BORDER,
                                      y * self.cell_size + BORDER,
                                      self.cell_size - 2 * BORDER,
                                      self.cell_size - 2 * BORDER))
        return surface


class FigureBoard(Board):
    def get_surface(self, surface, board) -> pygame.Surface:
        pygame.draw.rect(surface, PALETTE[1], surface.get_rect(), BORDER)
        if board:
            figure_board = pygame.Surface((len(board[0]) * self.cell_size,
                                           len(board) * self.cell_size), pygame.SRCALPHA)
            for y, line in enumerate(board):
                for x, cell in enumerate(line):
                    if cell:
                        pygame.draw.rect(figure_board, PALETTE[cell],
                                         (x * self.cell_size + BORDER,
                                          y * self.cell_size + BORDER,
                                          self.cell_size - 2 * BORDER,
                                          self.cell_size - 2 * BORDER))
            surface.blit(figure_board, figure_board.get_rect(center=surface.get_rect().center))
        return surface
