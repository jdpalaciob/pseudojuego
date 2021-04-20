import time

import pygame
from pygame import mixer

from model.TTetramino import TTetramino
from model.LineTetramino import LineTetramino


def init_game_window(height, width, background_image, background_color):
    icon = pygame.image.load("./resources/tetris.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris in python")
    screen.fill(background_color)
    screen.blit(background_image.convert(), (58, 0))
    return screen


def init_music_game():
    mixer.init()
    mixer.music.load("./resources/the_wall.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()


def draw_grid(HC, WC, grid_color, screen, x_cells, y_cells):
    for x in range(x_cells):
        for y in range(y_cells):

            grid = [
                ((x) * WC, (y) * HC),
                ((x + 1) * WC, (y) * HC),
                ((x + 1) * WC, (y + 1) * HC),
                ((x) * WC, (y + 1) * HC)
            ]
            # Grid just visible in background image
            if 60 // WC < (x) < 630 // WC:
                pygame.draw.polygon(screen, grid_color, grid, 1)


def init_game(width, height, x_cells, y_cells, background_color, grid_color, tetramino_color):
    pygame.init()
    background_image = pygame.image.load('./resources/fondo.jpg')
    screen = init_game_window(height, width, background_image, background_color)
    init_music_game()

    WC = width // x_cells
    HC = height // y_cells

    pos_tetramino_x = 8
    pos_tetramino_y = 0
    tetramino = LineTetramino()

    play = True
    while play:

        screen.fill(background_color)
        screen.blit(background_image, (58, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                tetramino.rotate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                pos_tetramino_x -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                pos_tetramino_y += HC
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                pos_tetramino_x += 1

        fig = tetramino.matrix_representation()
        s_fig = pygame.Surface((fig.shape[1] * WC, fig.shape[0] * HC))
        s_fig.set_colorkey((0, 255, 0))

        for i in range(fig.shape[1]):
            for j in range(fig.shape[0]):
                if fig[j, i] == 1:
                    r = pygame.Rect((i * WC, j * HC), (WC, HC))
                    pygame.draw.rect(s_fig, tetramino_color, r)

        fig_rect = s_fig.get_rect()
        fig_rect.move_ip((pos_tetramino_x * WC, pos_tetramino_y))
        screen.blit(s_fig, fig_rect)
        draw_grid(HC, WC, grid_color, screen, x_cells, y_cells)
        pygame.display.flip()
        time.sleep(0.3)

