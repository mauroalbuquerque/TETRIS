import sys, pygame
from pygame.locals import *
import time

pygame.init()

HIDTH = 600
WEIGTH = 400
SCREEN_SIZE = WEIGTH, HIDTH
BG_COLOR = 0, 0, 0
LINE_COLOR = 48, 48, 48
SIZE_GRID = 20
COLOR_FIGURE = 245, 219, 91
MOVE_DOWN_TIME = .2
CYCLE_SCAN = .05


def draw_grid():
    screen.fill(BG_COLOR)
    cont_horizontal = 0
    while cont_horizontal < HIDTH:
        pygame.draw.line(screen, LINE_COLOR, (0, cont_horizontal), (WEIGTH, cont_horizontal))
        cont_horizontal += SIZE_GRID

    cont_vertical = 0
    while cont_vertical < WEIGTH:
        pygame.draw.line(screen, LINE_COLOR, (cont_vertical, 0), (cont_vertical, HIDTH))
        cont_vertical += SIZE_GRID


def draw_figure(x, y):
    draw_grid()
    pygame.draw.rect(screen, COLOR_FIGURE, pygame.Rect(x, y, 20, 20))


def move_down():
    global posY
    global posX
    global cont_time

    time.sleep(CYCLE_SCAN)
    cont_time += CYCLE_SCAN

    if cont_time >= MOVE_DOWN_TIME and posY < HIDTH - SIZE_GRID:
        posY += SIZE_GRID
        draw_figure(posX, posY)
        cont_time = 0


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('TETRIS')
draw_grid()
posX = posY = 0
draw_figure(posX, posY)
cont_time = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if posX < WEIGTH - SIZE_GRID:
                    posX += SIZE_GRID

            if event.key == K_LEFT:
                if posX > 0:
                    posX -= SIZE_GRID

            if event.key == K_UP:
                pass

            if event.key == K_DOWN:
                posY += SIZE_GRID


    move_down()

    pygame.display.update()
