import pygame


PALETTE = {1: pygame.Color("red"),
           2: pygame.Color("blue"),
           3: pygame.Color("orange"),
           4: pygame.Color("yellow"),
           5: pygame.Color("aquamarine"),
           6: pygame.Color("brown"),
           7: pygame.Color("ivory")
           }
BORDER = 1


def render(surface, board, cell_size, shift_x, shift_y):
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell:
                pygame.draw.rect(surface, PALETTE[cell],
                                 (shift_x + x * cell_size + BORDER,
                                  shift_y + y * cell_size + BORDER,
                                  cell - 2 * BORDER, cell - 2 * BORDER))
