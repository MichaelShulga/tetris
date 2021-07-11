import pygame

from config import WIDTH, HEIGHT, FPS


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)



    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update objects
        clock.tick(FPS)
        print(clock.get_fps())

        # screen rendering
        screen.fill(pygame.Color("grey"))

        # update screen
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
