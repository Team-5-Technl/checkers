import os
import pygame
import sys

pygame.font.init()

# STATIC VARIABLES #
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))
FPS = 10
selected_black_color = (88, 16, 0)
white_score = 0
red_score = 0
FONT = pygame.font.SysFont('Consolas', 40)
####################
white_pieces = {}
red_pieces = {}
kings = {}


def draw_side_bar():
    top_text = FONT.render(f"Checkers score:", True, (255, 255, 255))
    WINDOW.blit(top_text, (840, 50))
    pygame.draw.ellipse(WINDOW, 'white', (900, 250, 50, 50))
    pygame.draw.ellipse(WINDOW, 'red', (900, 500, 50, 50))
    pygame.draw.rect(WINDOW, (100, 100, 100), pygame.Rect(1030, 250, 100, 50))
    pygame.draw.rect(WINDOW, (100, 100, 100), pygame.Rect(1030, 500, 100, 50))
    white_score_text = FONT.render(f"    |  {white_score}", True, (255, 255, 255))
    red_score_text = FONT.render(f"    |  {red_score}", True, (255, 255, 255))
    WINDOW.blit(white_score_text, (900, 255))
    WINDOW.blit(red_score_text, (900, 505))
    pygame.display.update()


def draw_window():
    WINDOW.fill((100, 100, 100))
    WINDOW.blit(BOARD, (0, 0))
    for i in range(24):
        if i < 12:
            rectangle_i = pygame.Rect(25 + (200 * (i % 4) + (100 * ((i // 4) % 2))), 25 + 100 * (i // 4), 50, 50)
            white_pieces['rectangle_'+str(i+1)] = rectangle_i
            pygame.draw.ellipse(WINDOW, 'white', rectangle_i)
        else:
            rectangle_i = pygame.Rect(25 + (200 * (i % 4) + (100 * (i // 4 % 2))), 225 + 100 * (i // 4), 50, 50)
            red_pieces['rectangle_' + str(i + 1)] = rectangle_i
            pygame.draw.ellipse(WINDOW, 'red', rectangle_i)


def end_turn():
    end_turn_text = FONT.render('END TURN', True, 'black')
    pygame.draw.rect(WINDOW, 'white', pygame.Rect(900, 700, 200, 100), False)
    WINDOW.blit(end_turn_text, (910, 740))


def select_white_piece(x):
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    pygame.draw.ellipse(WINDOW, 'grey', rect)
    return True


def select_red_piece(x):
    rect = list(red_pieces.values())[list(red_pieces.values()).index(x)]
    pygame.draw.ellipse(WINDOW, selected_black_color, rect)
    return True


def move_white_piece(x):
    global white_score
    pos = pygame.mouse.get_pos()
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    if 50 < abs(pos[0]-rect.center[0]) < 150 and 50 < pos[1]-rect.center[1] < 150:
        new_place = (rect.x + ([-100, 100][pos[0] - rect.x > 0]), rect.y + 100, 50, 50)
        if new_place not in (white_pieces | red_pieces).values() and new_place[0] < 800:
            '''
            This is for when we have kings
if rect in kings.values():
    if 50 < abs(pos[0]-rect.center[0]) < 150 and 50 < abs(pos[1]-rect.center[1]) < 150:
        if rect.x+([-100, 100][pos[0]-rect.x > 0], rect.y+([-100, 100][pos[1]-rect.y > 0], 
    50, 50) not in white_pieces.values(): 'put the bottom code in here' rect.y+=([-100, 100][pos[1]-rect.y > 0]
            '''
            pygame.draw.ellipse(WINDOW, 'black', rect)
            rect.x += ([-100, 100][pos[0]-rect.x > 0])
            rect.y += 100
            pygame.draw.ellipse(WINDOW, 'white', rect)
            return True
        if new_place not in white_pieces.values() and new_place in red_pieces.values():
            capture_red_piece(x)
        else:
            print('Another piece at selected location. Try again')
            pygame.draw.ellipse(WINDOW, 'white', rect)
    else:
        print('Illegal move. Try again')
        pygame.draw.ellipse(WINDOW, 'white', rect)


def move_red_piece(x):
    global red_score
    pos = pygame.mouse.get_pos()
    print(pos)
    rect = list(red_pieces.values())[list(red_pieces.values()).index(x)]
    if 50 < abs(pos[0]-rect.center[0]) < 150 and -150 < pos[1]-rect.center[1] < -50:
        new_place = (rect.x+([-100, 100][pos[0]-rect.x > 0]), rect.y-100, 50, 50)
        if new_place not in (white_pieces | red_pieces).values() and new_place[0] < 800:
            pygame.draw.ellipse(WINDOW, 'black', rect)
            rect.x += ([-100, 100][pos[0]-rect.x > 0])
            rect.y -= 100
            pygame.draw.ellipse(WINDOW, 'red', rect)
            return True
        if new_place not in red_pieces.values() and new_place in white_pieces.values():
            capture_white_piece(x)
        else:
            print('Another piece at selected location. Try again')
            pygame.draw.ellipse(WINDOW, 'red', rect)
    else:
        print('Illegal move. Try again')
        pygame.draw.ellipse(WINDOW, 'red', rect)


# for red pieces
def capture_white_piece(x):
    global red_score
    end_turn()
    pos = pygame.mouse.get_pos()
    rect = list(red_pieces.values())[list(red_pieces.values()).index(x)]
    new_place = (rect.x + ([-100, 100][pos[0] - rect.x > 0]), rect.y - 100, 50, 50)
    newer_place = (rect.x + ([-200, 200][pos[0] - rect.x > 0]), rect.y - 200, 50, 50)

    if newer_place not in (white_pieces | red_pieces).values() and newer_place[1] > 0 and newer_place[0] < 800:
        pygame.draw.ellipse(WINDOW, 'black', rect)
        rect.x += ([-200, 200][pos[0] - rect.x > 0])
        rect.y -= 200
        white_capture = list(white_pieces.keys())[list(white_pieces.values()).index(new_place)]
        pygame.draw.ellipse(WINDOW, 'red', rect)
        pygame.draw.ellipse(WINDOW, 'black', white_pieces[white_capture])
        del white_pieces[white_capture]
        red_score += 1
        return True
    else:
        print('Capture failed. Another piece. Try again')
        pygame.draw.ellipse(WINDOW, 'red', rect)


# for white pieces
def capture_red_piece(x):
    global white_score
    end_turn()
    pos = pygame.mouse.get_pos()
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    new_place = (rect.x + ([-100, 100][pos[0] - rect.x > 0]), rect.y + 100, 50, 50)
    newer_place = (rect.x+([-200, 200][pos[0] - rect.x > 0]), rect.y + 200, 50, 50)
    if newer_place not in (white_pieces | red_pieces).values() and newer_place[0] < 800 and newer_place[1] < 800:
        pygame.draw.ellipse(WINDOW, 'black', rect)
        rect.x += ([-200, 200][pos[0] - rect.x > 0])
        rect.y += 200
        red_capture = list(red_pieces.keys())[list(red_pieces.values()).index(new_place)]
        pygame.draw.ellipse(WINDOW, 'white', rect)
        pygame.draw.ellipse(WINDOW, 'black', red_pieces[red_capture])
        del red_pieces[red_capture]
        white_score += 1
        return True
    else:
        print('Capture failed. Another piece. Try again')
        pygame.draw.ellipse(WINDOW, 'white', rect)


def main():
    global select
    clock = pygame.time.Clock()
    draw_window()
    run = True
    selected = False
    mouse_click = 0
    turn = 0
    while run:
        clock.tick(FPS)
        if red_score == 12 or white_score == 12:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if pygame.winner() != None:
            # print(pygame.winner())
            # run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_click += 1
                print(['white turn', 'red turn'][turn % 2])
                if 900 < pos[0] < 1100 and 700 < pos[1] < 800:
                    turn += 1
                    WINDOW.fill((100, 100, 100), (900, 700, 200, 100))
                    continue
                if selected is False:
                    for i in [white_pieces.values(), red_pieces.values()][turn % 2]:
                        # works. but object is a rectangle. it considers that whole are a piece, not just the circle
                        if abs(i.x + 25 - pos[0]) <= 25 and abs(i.y + 25 - pos[-1]) <= 25:
                            if turn % 2 == 0:
                                j = select_white_piece(i)
                            else:
                                j = select_red_piece(i)
                            if j:
                                select = i
                                selected = True
                if mouse_click >= 2 and selected:
                    # moves piece. Centers too
                    if turn % 2 == 0:
                        v = move_white_piece(select)
                    else:
                        v = move_red_piece(select)
                    if v:
                        turn += 1
                    selected = False
                    mouse_click = 0
        draw_side_bar()
        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
