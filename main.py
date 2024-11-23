import pygame
from biblioteca import *
from config import *
import random
import json


pygame.display.set_caption("BUSCAMINA")
pygame.display.set_icon(icono)

contador = 0
corriendo = True
mostrar_inicio = True

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
                    banderas = crear_diccionario_banderas(8, 8)
                    matriz_completa = matriz_minas_contiguas(8, 8, tablero)
                elif boton_salir.collidepoint(event.pos):
                    corriendo = False
    else:
        pantalla.fill(COLOR_TABLERO)
        crear_rectangulos(matriz_completa, estados, pantalla)
        
        desplazamiento_x = (PANTALLA_ANCHO - len(tablero) * 50) // 2
        desplazamiento_y = (PANTALLA_ALTO - len(tablero) * 50) // 2

        for (fila, columna) in banderas:                                                 # Redibujar las banderas
            if banderas[(fila, columna)] == True:                                        # Solo redibujar casillas con bandera
                x = desplazamiento_x + columna * 50
                y = desplazamiento_y + fila * 50
                pantalla.blit(imagen_bandera, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:               # Clic izquierdo para descubrir casilla
                mouse_x, mouse_y = event.pos
                fila = (mouse_y - desplazamiento_y) // 50
                columna = (mouse_x - desplazamiento_x) // 50
                
                if (fila, columna) in estados and banderas[(fila, columna)] == False :   # Verifica que no tenga bandera, si no tiene descubre la casilla
                    estados[(fila, columna)] = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:             # Clic derecho para poner/sacar banderas
                mouse_x, mouse_y = event.pos
                fila = (mouse_y - desplazamiento_y) // 50
                columna = (mouse_x - desplazamiento_x) // 50

                if (fila, columna) in estados and estados[(fila, columna)] == True:      # Revisa si estás en un casillero y si este está tapado
                    if banderas[(fila, columna)] == False :                              # Si la posicion no está en la misma posicion de una bandera, pone una bandera
                        banderas[(fila, columna)] = True
                        print(banderas)
                    else:                                                                # Si ya tiene bandera, saca la bandera
                        banderas[(fila, columna)] = False
                        print(banderas)

            elif event.type == pygame.QUIT:
                corriendo = False
                print("cerrando juego...")

        pygame.display.flip()

pygame.quit()
