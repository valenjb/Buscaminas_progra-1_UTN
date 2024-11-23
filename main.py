import pygame
from biblioteca import *
from config import *
import random
import json


pygame.display.set_caption("BUSCAMINA")

pygame.display.set_icon(icono)

contador = 0
corriendo = True
mostrar_inicio=True

while corriendo:
    if mostrar_inicio:
        pantalla_inicio(pantalla, font_inicio)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio = False
                    tablero = crear_matriz_buscaminas(8, 8, 10)
                    estados = crear_diccionario_estados(8, 8)
                    matriz_completa = matriz_minas_contiguas(8, 8, tablero)
                elif boton_salir.collidepoint(event.pos):
                    corriendo = False
    else:
        pantalla.fill(COLOR_TABLERO)
        crear_rectangulos(matriz_completa, estados, pantalla)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic izquierdo
                mouse_x, mouse_y = event.pos
                desplazamiento_x = (PANTALLA_ANCHO - len(tablero) * 50) // 2
                desplazamiento_y = (PANTALLA_ALTO - len(tablero) * 50) // 2
                fila = (mouse_y - desplazamiento_y) // 50
                columna = (mouse_x - desplazamiento_x) // 50
                if (fila, columna) in estados:
                    estados[(fila, columna)] = False  # Descubrir casilla
            
            elif event.type == pygame.QUIT:
                corriendo = False
                print("cerrando juego...")

        pygame.display.flip()

pygame.quit()