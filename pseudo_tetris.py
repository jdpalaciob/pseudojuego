""" JUEGO TRIBUTO A TETRIS """

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

#### TETRIMINOS ####
O_tet = np.array(
    [1, 1],
    [1, 1])
J_tet = np.array(
    [0, 0, 1],
    [1, 1, 1])
L_tet = np.array(
    [1, 0, 0],
    [1, 1, 1])
I_tet = np.array(
    [1, 1, 1, 1])
S_tet = np.array(
    [0, 1, 1],
    [1, 1, 0])
Z_tet = np.array(
    [1, 1, 0],
    [0, 1, 1])
T_tet = np.array(
    [0, 1, 0],
    [1, 1, 1])

### EXECUTION LOOP ####
RUN = True
while RUN:
    screen.blit(fondo, (58, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
