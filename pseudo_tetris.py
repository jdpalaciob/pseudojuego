""" JUEGO TRIBUTO A TETRIS """

import pygame

pygame.init()

# Ventana de prueba #
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
screen.fill((25, 25, 25))

### EXECUTION LOOP ####
RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False