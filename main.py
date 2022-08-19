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
            white_pieces['rectangle_'+str(i+1)] = rectangle_i
            pygame.draw.ellipse(WINDOW, 'white', rectangle_i)
        else:
            rectangle_i = pygame.Rect(25 + (200 * (i % 4) + (100 * (i // 4 % 2))), 225 + 100 * (i // 4), 50, 50)
            black_pieces['rectangle_' + str(i + 1)] = rectangle_i
            pygame.draw.ellipse(WINDOW, (88, 16, 0), rectangle_i)
    # print(white_pieces)
    # print(black_pieces)
    # pygame.display.update()


def select_piece(x):
    rect_num = list(white_pieces.keys())[list(white_pieces.values()).index(x)]
    pygame.draw.ellipse(WINDOW, 'grey', white_pieces[rect_num])
    print('selected piece function works')


def move_piece(x):
    pos = pygame.mouse.get_pos()
    print(pos)
    rect_num = list(white_pieces.keys())[list(white_pieces.values()).index(x)]
    rect = white_pieces[rect_num]
    pygame.draw.ellipse(WINDOW, 'black', white_pieces[rect_num])
    white_pieces[rect_num] = pygame.Rect(pos[0], pos[-1], 50, 50)
    print(pos[0] - rect[0], pos[-1] - rect[1], 50, 50)
    pygame.draw.ellipse(WINDOW, 'white', white_pieces[rect_num])


def main():
    global select
    clock = pygame.time.Clock()
    draw_window()
    run = True
    selected = False
    mouse_click = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if pygame.winner() != None:
            # print(pygame.winner())
            # run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_click += 1
                if selected is False:
                    for i in white_pieces.values():
                        # works. but object is a rectangle. it considers that whole are a piece, not just the circle
                        if abs(i[0] + 25 - pos[0]) <= 25 and abs(i[1] + 25 - pos[-1]) <= 25:
                            print('piece selected', pos, i)
                            select_piece(i)
                            select = i
                            selected = True
                if mouse_click == 2 and selected:
                    # moves piece. However it does not center
                    print('move maybe')
                    # print(select)
                    move_piece(select)
                    selected = False
                    mouse_click = 0
        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
