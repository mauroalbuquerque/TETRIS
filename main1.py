import sys, pygame
from pygame.locals import *
import time

HIDTH = 600
WEIGTH = 300
SCREEN_SIZE = WEIGTH, HIDTH
BG_COLOR = 0, 0, 0
LINE_COLOR = 48, 48, 48
SIZE_GRID = 20
COLOR_FIGURE = 245, 219, 91
MOVE_DOWN_TIME = .2
CYCLE_SCAN = .05
board = list()
rowList = list()


def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('TETRIS')
    screen.fill(BG_COLOR)
    draw_grid()
    create_board()
    board[0][7] = 1
    draw_figure()


def create_board():
    for row in range(HIDTH // SIZE_GRID):
        for col in range(WEIGTH // SIZE_GRID):
            rowList.append(0)
        board.append(rowList[:])
        rowList.clear()


def draw_figure():
    screen.fill(BG_COLOR)
    draw_grid()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                pygame.draw.rect(screen, COLOR_FIGURE, pygame.Rect(col * SIZE_GRID, row * SIZE_GRID, SIZE_GRID, SIZE_GRID))


def draw_grid():
    cont_horizontal = 0
    while cont_horizontal < HIDTH:
        pygame.draw.line(screen, LINE_COLOR, (0, cont_horizontal), (WEIGTH, cont_horizontal))
        cont_horizontal += SIZE_GRID

    cont_vertical = 0
    while cont_vertical < WEIGTH:
        pygame.draw.line(screen, LINE_COLOR, (cont_vertical, 0), (cont_vertical, HIDTH))
        cont_vertical += SIZE_GRID


def move_right():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row < len(board) - 1:
                if col < (len(board[row]) - 1) and board[row][col] == 1 and board[row + 1][col] != 1:
                    board[row][col + 1] = 1
                    board[row][col] = 0
                    break
    draw_figure()


def move_left():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row < len(board) - 1:
                if col > 0 and board[row][col] == 1 and board[row + 1][col] != 1:
                    board[row][col - 1] = 1
                    board[row][col] = 0
                    break
    draw_figure()


def move_down():
    for row in range(len(board) - 2, -1, -1):
        for col in range(len(board[row])):
            if board[row + 1][col] == 0:
                if board[row][col] == 1:
                    if board[row + 1][col] != 1:
                        board[row + 1][col] = 1
                        board[row][col] = 0

    draw_figure()


def touch_fund():
    board[0][7] = 1
    draw_figure()


main()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_right()

            if event.key == K_LEFT:
                move_left()

            if event.key == K_DOWN:
                move_down()

    pygame.display.update()
