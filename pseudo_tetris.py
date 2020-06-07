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

    # Colisng window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    # Generating Tetrimino
    fig = tetrimino()
    print(fig)

    for x in range(cX):
        for y in range(cY):

            # Generating grid
            grid = [
                ((x)   * WC, (y)   * HC),
                ((x+1) * WC, (y)   * HC),
                ((x+1) * WC, (y+1) * HC),
                ((x)   * WC, (y+1) * HC)
            ]
            # Grid just visible in background image
            if 60 <= (x * WC) < 630:
                pygame.draw.polygon(screen, (25, 170, 190), grid, 1)
            
            # Tetrimino impression
            if x < fig.shape[1] and y < fig.shape[0]:
                if fig[y, x] == 1:
                    pygame.draw.polygon(screen, (250, 0, 0), grid, 0)


    # Showing screen
    pygame.display.flip()
    time.sleep(10)
