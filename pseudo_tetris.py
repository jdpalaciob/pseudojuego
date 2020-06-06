""" JUEGO TRIBUTO A TETRIS """

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

### EXECUTION LOOP ####
RUN = True
while RUN:

    # Colisng window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    for x in range(cX):
        for y in range(cY):

            # Generating grid
            grid = [
                ((x)   * WC, (y)   * HC),
                ((x+1) * WC, (y)   * HC),
                ((x+1) * WC, (y+1) * HC),
                ((x)   * WC, (y+1) * HC)
            ]
            pygame.draw.polygon(screen, (25, 25, 25), grid, 1)

    # Showing screen
    pygame.display.flip()
