import os
import pygame
import sys
import time

pygame.font.init()

# STATIC VARIABLES #
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = pygame.image.load(os.path.join('Assets', 'Board.png'))
FPS = 20
CROWN = pygame.transform.scale(pygame.image.load('Assets/crown.png'), (44, 25))
selected_black_color = (88, 16, 0)
white_score = 0
red_score = 0
FONT = pygame.font.SysFont('Consolas', 40)
####################
white_pieces = {}
red_pieces = {}
kings = {}


def draw_side_bar(turn):
    if turn % 2 == 0:
        turn_text = 'white'
    else:
        turn_text = 'red'
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
    pygame.draw.rect(WINDOW, (100, 100, 100), pygame.Rect(1000, 620, 200, 50))
    turn_text = FONT.render(f"Turn: {turn_text}", True, (255, 255, 255))
    WINDOW.blit(turn_text, (885, 630))
    y = 600
    pygame.display.update()


def draw_window():
    WINDOW.fill((100, 100, 100))
    WINDOW.blit(BOARD, (0, 0))
    for p in range(24):
        if p < 12:
            rectangle_p = pygame.Rect(25 + (200 * (p % 4) + (100 * ((p // 4) % 2))), 25 + 100 * (p // 4), 50, 50)
            white_pieces['rectangle_' + str(p + 1)] = rectangle_p
            pygame.draw.ellipse(WINDOW, 'white', rectangle_p)
        else:
            rectangle_p = pygame.Rect(25 + (200 * (p % 4) + (100 * (p // 4 % 2))), 225 + 100 * (p // 4), 50, 50)
            red_pieces['rectangle_' + str(p + 1)] = rectangle_p
            pygame.draw.ellipse(WINDOW, 'red', rectangle_p)


def end_turn():
    end_turn_text = FONT.render('END TURN', True, 'black')
    pygame.draw.rect(WINDOW, 'white', pygame.Rect(900, 700, 200, 100), False)
    WINDOW.blit(end_turn_text, (910, 740))


def select_white_piece(x):
    pygame.draw.ellipse(WINDOW, 'grey', x)
    rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
    pygame.draw.ellipse(WINDOW, 'grey', rect)
    '''TESTING THE DISPLAY OF THE CROWN IMAGE '''
    # WINDOW.blit(CROWN, (rect.left+2, rect.top+15))
    '''END TEST CODE'''
    return True


def select_red_piece(x):
    pygame.draw.ellipse(WINDOW, selected_black_color, x)
    return True


def move_white_piece(x):
    global white_score
    pos = pygame.mouse.get_pos()
    if x in white_pieces.values():
        rect = x
    else:
        rect = list(red_pieces.values())[list(red_pieces.values()).index(x)]
        pygame.draw.ellipse(WINDOW, 'red', rect)
        return False
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
            if rect.y > 700:
                ''' Need to declare piece as KING'''
                kings[x] = rect
                WINDOW.blit(CROWN, (rect.left + 2, rect.top + 15))
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
    if x in red_pieces.values():
        rect = x
    else:
        rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
        pygame.draw.ellipse(WINDOW, 'white', rect)
        return False
    if 50 < abs(pos[0]-rect.center[0]) < 150 and -150 < pos[1]-rect.center[1] < -50:
        new_place = (rect.x+([-100, 100][pos[0]-rect.x > 0]), rect.y-100, 50, 50)
        if new_place not in (white_pieces | red_pieces).values() and new_place[0] < 800:
            pygame.draw.ellipse(WINDOW, 'black', rect)
            rect.x += ([-100, 100][pos[0]-rect.x > 0])
            rect.y -= 100
            pygame.draw.ellipse(WINDOW, 'red', rect)
            ''' Need to declare piece as KING'''
            if rect.y <= 100:
                WINDOW.blit(CROWN, (rect.left + 2, rect.top + 15))
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
    if x in red_pieces.values():
        rect = x
    else:
        rect = list(white_pieces.values())[list(white_pieces.values()).index(x)]
        pygame.draw.ellipse(WINDOW, 'white', rect)
        return False
    new_place = (rect.x + ([-100, 100][pos[0] - rect.x > 0]), rect.y - 100, 50, 50)
    newer_place = (rect.x + ([-200, 200][pos[0] - rect.x > 0]), rect.y - 200, 50, 50)
    if newer_place not in (white_pieces | red_pieces).values() and newer_place[1] > 0 and newer_place[0] < 800:
        pygame.draw.ellipse(WINDOW, 'black', rect)
        rect.x += ([-200, 200][pos[0] - rect.x > 0])
        rect.y -= 200
        white_capture = list(white_pieces.keys())[list(white_pieces.values()).index(new_place)]
        pygame.draw.ellipse(WINDOW, 'red', rect)
        pygame.draw.ellipse(WINDOW, 'black', white_pieces[white_capture])
        ''' Need to delcare piece as KING'''
        if rect.y <= 100:
            WINDOW.blit(CROWN, (rect.left + 2, rect.top + 15))
        del white_pieces[white_capture]
        red_score += 1
        return True
    else:
        print('Capture failed. Another piece. Try again')
        pygame.draw.ellipse(WINDOW, 'red', rect)


# for white pieces
def capture_red_piece(x):
    global white_score
    print('sjdhfksjf')
    end_turn()
    pos = pygame.mouse.get_pos()
    if x in white_pieces.values():
        rect = x
    else:
        rect = list(red_pieces.values())[list(red_pieces.values()).index(x)]
        pygame.draw.ellipse(WINDOW, 'red', rect)
        return False
    new_place = (rect.x + ([-100, 100][pos[0] - rect.x > 0]), rect.y + 100, 50, 50)
    newer_place = (rect.x+([-200, 200][pos[0] - rect.x > 0]), rect.y + 200, 50, 50)
    if newer_place not in (white_pieces | red_pieces).values() and newer_place[0] < 800 and newer_place[1] < 800:
        pygame.draw.ellipse(WINDOW, 'black', rect)
        rect.x += ([-200, 200][pos[0] - rect.x > 0])
        rect.y += 200
        red_capture = list(red_pieces.keys())[list(red_pieces.values()).index(new_place)]
        pygame.draw.ellipse(WINDOW, 'white', rect)
        pygame.draw.ellipse(WINDOW, 'black', red_pieces[red_capture])
        if rect.y > 700:
            ''' delcare piece as KING'''
            WINDOW.blit(CROWN, (rect.left + 2, rect.top + 15))
        del red_pieces[red_capture]
        white_score += 1
        return True
    else:
        print('Capture failed. Another piece. Try again')
        pygame.draw.ellipse(WINDOW, 'white', rect)


def winner():
    if red_score >= 12:
        pygame.draw.rect(WINDOW, (190, 100, 100), pygame.Rect(0, 0, 1200, 800))
        winner_text = FONT.render(f"RED WINS!", True, (255, 255, 255))
        WINDOW.blit(winner_text, (WIDTH/2 - 100, HEIGHT/2 - 50))
    elif white_score >= 12:
        pygame.draw.rect(WINDOW, (200, 200, 200), pygame.Rect(0, 0, 1200, 800))
        winner_text = FONT.render(f"WHITE WINS!", True, (255, 255, 255))
        WINDOW.blit(winner_text, (WIDTH/2 - 100, HEIGHT/2 - 50))
    pygame.display.update()
    time.sleep(10)


def main():
    global i
    clock = pygame.time.Clock()
    draw_window()
    run = True
    selected = False
    mouse_click = 0
    turn = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_click += 1
                print(['white turn', 'red turn'][turn % 2])
                if 900 < pos[0] < 1100 and 700 < pos[1] < 800:
                    turn += 1
                    WINDOW.fill((100, 100, 100), (900, 700, 200, 100))
                    pass
                if selected is False:
                    for i in [white_pieces.values(), red_pieces.values()][turn % 2]:
                        # works. but object is a rectangle. it considers that whole are a piece, not just the circle
                        if abs(i.x + 25 - pos[0]) <= 25 and abs(i.y + 25 - pos[-1]) <= 25:
                            if turn % 2 == 0:
                                select_white_piece(i)
                            else:
                                select_red_piece(i)
                            selected = True
                            break
                if mouse_click >= 2 and selected:
                    # moves piece. Centers too
                    if turn % 2 == 0:  # and abs(pos[0]-i[0]+25) > 25 : fix the selection bug
                        v = move_white_piece(i)
                    else:
                        v = move_red_piece(i)
                    if v:
                        turn += 1
                    selected = False
                    mouse_click = 0
        draw_side_bar(turn)
        if red_score == 12 or white_score == 12:
            winner()
            run = False
        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
