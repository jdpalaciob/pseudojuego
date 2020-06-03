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

# Estructura de datos para el estado de cada celda
gameState = np.zeros((nxC, nyC))

# Bucle de ejecución
while True:

    # Copia del estado que recibe la iteración.
    newState = np.copy(gameState)
    # Esta matriz recibirá los cambios que se realicen en cada ciclo.

    # Ciclo para recorrer las celdas generadas
    for x in range(nxC):
        for y in range(nyC):

            # Límites dimensionales de los rectángulos
            poly = [((x)   * dimCW, (y)   * dimCH),
                    ((x+1) * dimCW, (y)   * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Número de vecinos cercanos.
            n_vec = gameState[(x-1) % nxC, (y-1) % nyC] + \
                    gameState[(x)   % nxC, (y-1) % nyC] + \
                    gameState[(x+1) % nxC, (y-1) % nyC] + \
                    gameState[(x-1) % nxC, (y)   % nyC] + \
                    gameState[(x+1) % nxC, (y)   % nyC] + \
                    gameState[(x-1) % nxC, (y+1) % nyC] + \
                    gameState[(x)   % nxC, (y+1) % nyC] + \
                    gameState[(x+1) % nxC, (y+1) % nyC]
            
            # REGLA 1: Si muerta y 3 vecinas vivas, entonces revive.
            if gameState[x, y] == 0 and n_vec == 3:
                newState[x, y] = 1
            # REGLA 2: Si viva y, menos de 2 o más de 3 vivas, entonces muere.
            elif gameState[x, y] == 1 and (n_vec < 2 or n_vec > 3):
                newState[x, y] = 0


            # Dibuja los rectángulos. Recibe: pantalla, color, límites de polígonos, grosor
            if gameState[x, y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1) # 1 pixel (cuadrícula)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0) # 0 para rellenar completo

    # Actualizar el estado que inicia la siguiente iteración
    gameState = np.copy(newState)
    # Mostrar los resultados de cuadrícula para cada iteración
    pygame.display.flip()