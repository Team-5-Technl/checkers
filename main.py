import os
import pygame, sys

pygame.font.init()

# STATIC VARIABLES #
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))
FPS = 10
####################
white_pieces = {}
black_pieces = {}


def draw_window():
    WINDOW.blit(BOARD, (0, 0))
    for i in range(24):
        if i < 12:
            rectangle_i = pygame.Rect(25 + (200 * (i % 4) + (100 * ((i // 4) % 2))), 25 + 100 * (i // 4), 50, 50)
            white_pieces['rectangle_'+str(i+1)] = rectangle_i[0:2]
            pygame.draw.ellipse(WINDOW, 'white', rectangle_i)
        else:
            rectangle_i = pygame.Rect(25 + (200 * (i % 4) + (100 * (i // 4 % 2))), 225 + 100 * (i // 4), 50, 50)
            black_pieces['rectangle_' + str(i + 1)] = rectangle_i[0:2]
            pygame.draw.ellipse(WINDOW, (88, 16, 0), rectangle_i)
    # print(white_pieces)
    # print(black_pieces)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # if pygame.winner() != None:
            # print(pygame.winner())
            # run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for i in white_pieces.values():
                    # works. but object is a rectangle. it considers that whole are a piece, not just the circle
                    if abs(i[0] + 25 - pos[0]) <= 25 and abs(i[-1] + 25 - pos[-1]) <= 25:
                        print('piece selected', pos, i)

    pygame.quit()


if __name__ == "__main__":
    main()
