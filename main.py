import os
import pygame, sys

pygame.font.init()

# STATIC VARIABLES #
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))
FPS = 10
black_color = (88, 16, 0)
####################
white_pieces = {}
black_pieces = {}
kings = {}


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
            pygame.draw.ellipse(WINDOW, black_color, rectangle_i)
    # print(white_pieces)
    # print(black_pieces)
    # pygame.display.update()


def select_piece(x):
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    pygame.draw.ellipse(WINDOW, 'grey', rect)
    # print('selected piece function works')


def move_piece(x):
    pos = pygame.mouse.get_pos()
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    if 50 < abs(pos[0]-rect.center[0]) < 150 and 50 < pos[1]-rect.center[1] < 150:
        if (rect.x+([-100, 100][pos[0]-rect.x > 0]), rect.y+100, 50, 50) not in white_pieces.values():
            '''
            This is for when we have kings
if rect in kings.values():
    if 50 < abs(pos[0]-rect.center[0]) < 150 and 50 < abs(pos[1]-rect.center[1]) < 150:
        if rect.x+=([-100, 100][pos[0]-rect.x > 0], rect.y+=([-100, 100][pos[1]-rect.y > 0], 
    50, 50) not in white_pieces.values(): 'put the bottom code in here' rect.y+=([-100, 100][pos[1]-rect.y > 0]
            '''
            pygame.draw.ellipse(WINDOW, 'black', rect)
            rect.x += ([-100, 100][pos[0]-rect.x > 0])
            rect.y += 100
            pygame.draw.ellipse(WINDOW, 'white', rect)
        else:
            print('Another piece at selected location. Try again')
            pygame.draw.ellipse(WINDOW, 'white', rect)
    else:
        print('Illegal move. Try again')
        pygame.draw.ellipse(WINDOW, 'white', rect)


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
                        if abs(i.x + 25 - pos[0]) <= 25 and abs(i.y + 25 - pos[-1]) <= 25:
                            # print('piece selected', pos, i)
                            select_piece(i)
                            select = i
                            selected = True
                if mouse_click == 2 and selected:
                    # moves piece. Centers too
                    # print(select)
                    move_piece(select)
                    selected = False
                    mouse_click = 0
        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
