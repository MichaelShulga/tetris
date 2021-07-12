import pygame

from config import WIDTH, HEIGHT, FPS

from controller import TetrisController


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    tetris_controller = TetrisController()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)



        screen.fill(pygame.Color("grey"))

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
