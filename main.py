import pygame

from config import WIDTH, HEIGHT, FPS, TETRIS_SIZE

from controller import TetrisController

cell_size = 30
tetris_rect = pygame.Rect(0, 0, TETRIS_SIZE[0] * cell_size, TETRIS_SIZE[1] * cell_size)
figure_rect = pygame.Rect(tetris_rect.width + 20, 0, 5 * cell_size, 5 * cell_size)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    sprites = pygame.sprite.Group()

    tetris = TetrisController(TETRIS_SIZE, tetris_rect, figure_rect, cell_size, sprites)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            tetris.handle_event(event)

        delta = clock.tick(FPS) / 1000

        tetris.update(delta)

        screen.fill(pygame.Color("grey"))
        sprites.draw(screen)

        pygame.display.flip()
        print(clock.get_fps())
    pygame.quit()


if __name__ == '__main__':
    main()
