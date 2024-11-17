import pygame
import random
import json
from biblioteca import *
from config import *

pygame.display.set_caption("BUSCAMINA")

pygame.display.set_icon(icono)



contador = 0
corriendo = True
mostrar_inicio=True

while corriendo == True:

    if mostrar_inicio:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo=False

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio=False
                    
                    tablero = crear_matriz_buscaminas(8,8,10)
                    test_matriz(tablero)          #PARA USAR CUANDO TESTEAMOS

                if boton_salir.collidepoint(event.pos):
                    corriendo=False
                    print("Cerrando juego...")
    else:
        pantalla.fill(COLOR_TABLERO)
        
        desplazamiento_x = (PANTALLA_ANCHO - 8 * 50) // 2
        desplazamiento_y = (PANTALLA_ALTO - 8 * 50) // 2

        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):
                x = desplazamiento_x + columna * 50  # Desplazamiento en el eje X
                y = desplazamiento_y + fila * 50
                pantalla.blit(imagen_cuadrado, (x, y))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento)                      #INFO DE CORDENADAS DE DONDE HACE CLICK

        pygame.display.flip()

pygame.quit()

""" 
A VER A FUTURO!!!!!!!!!!!!!!!!!!!!!



if evento.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
    mouse_x, mouse_y = evento.pos  # Coordenadas del clic

if tablero[fila][columna] == -1:  # Si hay una mina
    pantalla.blit(imagen_mina, (x, y))
else:
    pantalla.blit(imagen_cuadrado, (x, y))
"""