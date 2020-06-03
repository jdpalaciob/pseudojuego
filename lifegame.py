import pygame
import numpy as np

pygame.init()

# Crear pantalla
width, hight = 1000,1000    # dimensión en pixeles
screen = pygame.display.set_mode((width,hight))

# Color de fondo
bg = 25, 25, 25     # casi negro, casi oscuro
screen.fill(bg)     # llenado del fondo

# Celdas
nxC, nyC = 50, 50   # cantidad de celdas por eje
dimCW = width // nxC # ancho de cada celda
dimCH = hight // nyC # alto de cada celda

# Bucle de ejecución
while True:

    # Ciclo para recorrer las celdas generadas
    for x in range(nxC):
        for y in range(nyC):

            # Límites dimensionales de los rectángulos
            poly = [((x) * dimCW, (y) * dimCH),
            ((x+1) * dimCW, (y) * dimCH),
            ((x+1) * dimCW, (y+1) * dimCH),
            ((x) * dimCW, (y+1) * dimCH)]

            # Dibuja los rectángulos. Recibe: pantalla, color, límites de polígonos, grosor
            pygame.draw.polygon(screen, (128,128,128), poly, 1) # 1 pixel (cuadrícula)
    
    # Mostrar los resultados de cuadrícula para cada iteración
    pygame.display.flip()