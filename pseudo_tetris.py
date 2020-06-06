""" JUEGO TRIBUTO A TETRIS """

import numpy as np
import pygame
from random import choice

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

#### TETRIMINOS ####
def tetrimino():
    tet = choice(('O', 'J', 'L', 'I', 'S', 'Z', 'T'))
    if tet == 'O':
        O_tet = np.array(
            [1, 1],
            [1, 1])
        return O_tet
    elif tet == 'J':
        J_tet = np.array(
            [0, 0, 1],
            [1, 1, 1])
        return J_tet
    elif tet == 'L':
        L_tet = np.array(
            [1, 0, 0],
            [1, 1, 1])
        return L_tet
    elif tet == 'I':
        I_tet = np.array(
            [1, 1, 1, 1])
        return I_tet
    elif tet == 'S':
        S_tet = np.array(
            [0, 1, 1],
            [1, 1, 0])
        return S_tet
    elif tet == 'Z':
        Z_tet = np.array(
            [1, 1, 0],
            [0, 1, 1])
        return Z_tet
    elif tet == 'T':
        T_tet = np.array(
            [0, 1, 0],
            [1, 1, 1])
        return Z_tet

### EXECUTION LOOP ####
RUN = True
while RUN:
    screen.blit(fondo, (58, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
