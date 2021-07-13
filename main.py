import pygame

from config import WIDTH, HEIGHT, FPS, TETRIS_SIZE

from controller import TetrisController


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    tetris_controller = TetrisController(TETRIS_SIZE)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        delta = clock.tick(FPS)

        tetris_controller.update(delta)

        screen.fill(pygame.Color("grey"))

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
