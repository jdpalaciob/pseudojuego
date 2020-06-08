""" JUEGO TRIBUTO A TETRIS """
from random import choice
import time
import numpy as np
import pygame

pygame.init()

#### INTERFACE ####
# Screen #
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
# Header #
icono = pygame.image.load('icono.jpeg')
pygame.display.set_icon(icono)
pygame.display.set_caption('PseudoTetris')
# Background #
screen.fill((25, 25, 25))
fondo = pygame.image.load('fondo.jpg').convert()
screen.blit(fondo, (58, 0))

#### GRID ####
# Cells #
cX, cY = 20, 20
WC = width // cY
HC = height // cY

#### TETRIMINOS ####
def tetrimino():
    tet = choice(('O', 'J', 'L', 'I', 'S', 'Z', 'T'))
    if tet == 'O':
        tet = np.array([
            [1, 1],
            [1, 1]])
    elif tet == 'J':
        tet = np.array([
            [0, 0, 1],
            [1, 1, 1]])
    elif tet == 'L':
        tet = np.array([
            [1, 0, 0],
            [1, 1, 1]])
    elif tet == 'I':
        tet = np.array([
            [1, 1, 1, 1]])
    elif tet == 'S':
        tet = np.array([
            [0, 1, 1],
            [1, 1, 0]])
    elif tet == 'Z':
        tet = np.array([
            [1, 1, 0],
            [0, 1, 1]])
    elif tet == 'T':
        tet = np.array([
            [0, 1, 0],
            [1, 1, 1]])
    return tet

### EXECUTION LOOP ####
RUN = True
while RUN:

    # CLEANING BACKGORUND
    screen.fill((25, 25, 25))
    screen.blit(fondo, (58, 0))

    # CLOSING WINDOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # GENERATING TETRIMINO
    # Importing structure
    fig = tetrimino()
    # Surface to enclose tetrimino
    s_fig = pygame.Surface((fig.shape[1]*WC, fig.shape[0]*HC))
    s_fig.set_colorkey((0, 0, 0))    # Making invisible
    # Generating rectangles
    for i in range(fig.shape[1]):
        for j in range(fig.shape[0]):
            if fig[j, i] == 1:
                r = pygame.Rect((i*WC, j*HC), (WC, HC))
                pygame.draw.rect(s_fig, (250, 0, 0), r)
    # Enclosing surface in a rectangle
    fig_rect = s_fig.get_rect()
    fig_rect.move_ip((8*WC, 0))    # Se mueve para que aparezca en la mitad
    screen.blit(s_fig, fig_rect)    # Imprime la ruperficie s_fig, dodne esté fig_rect

    # GENERATING GRID
    for x in range(cX):
        for y in range(cY):

            grid = [
                ((x)   * WC, (y)   * HC),
                ((x+1) * WC, (y)   * HC),
                ((x+1) * WC, (y+1) * HC),
                ((x)   * WC, (y+1) * HC)
            ]
            #Grid just visible in background image
            if 60 // WC < (x) < 630 // WC:
                pygame.draw.polygon(screen, (25, 170, 190), grid, 1)

    # SHOWING SCREEN
    pygame.display.flip()
    time.sleep(1)
