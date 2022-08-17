import os
import pygame

pygame.font.init()

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))

def draw_window():
    WINDOW.blit(BOARD, (0, 0))
    pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
