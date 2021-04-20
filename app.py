import os

import engine.core_game as pt

width, height = 700, 650
pos_x, pos_y = 350, 40
x_cells, y_cells = 50, 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos_x, pos_y)

background_color = (0, 0, 0)
grid_color = (25, 170, 190)
tetramino_color = (225, 19, 19)

pt.init_game(width, height, x_cells, y_cells, background_color, grid_color, tetramino_color)
