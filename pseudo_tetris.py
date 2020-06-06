""" JUEGO TRIBUTO A TETRIS """
from random import choice
import numpy as np
import pygame

# Functions


def play_music(path_track, volume, loop=1000):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load(path_track)
    pygame.mixer.music.play(loops=loop)


def stop_music():
    pygame.mixer.music.stop()


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

# Add music to the window
play_music("sources/music/the_wall_theme.mp3", 0.8)

### EXECUTION LOOP ####
RUN = True
while RUN:

    # Colisng window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    for x in range(cX):
        for y in range(cY):

            # Grid just in background image
            if 60 <= (x * WC) < 630:
                # Generating grid
                grid = [
                    ((x)   * WC, (y)   * HC),
                    ((x+1) * WC, (y)   * HC),
                    ((x+1) * WC, (y+1) * HC),
                    ((x)   * WC, (y+1) * HC)
                ]
                pygame.draw.polygon(screen, (25, 170, 190), grid, 1)

    # Showing screen
    pygame.display.flip()


