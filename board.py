import pygame


class Board(pygame.sprite.Sprite):
    image = None

    def __init__(self, rect: pygame.Rect, cell_size, *groups):
        super().__init__(*groups)
        self.rect = rect
        self.surface = pygame.Surface(rect.size, pygame.SRCALPHA)

        self.cell_size = cell_size

    def render(self, board):
        self.image = self.get_surface(self.surface.copy(), board)

    def get_surface(self, surface, board) -> pygame.Surface:
        pass
