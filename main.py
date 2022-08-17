import os
import pygame

pygame.font.init()

# STATIC VARIABLES #
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))
FPS = 10
####################

def draw_window():
    WINDOW.blit(BOARD, (0, 0))
    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
    
