""" JUEGO TRIBUTO A TETRIS """

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

# Add music to the window
play_music("sources/music/the_wall_theme.mp3", 0.8)

### EXECUTION LOOP ####
RUN = True
while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.blit(fondo, (58, 0))
    pygame.display.flip()


