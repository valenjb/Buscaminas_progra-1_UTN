import pygame
from biblioteca import *
from config import *
import random
import json

#NOMBRE DE ARCHIVO E ICONO
pygame.display.set_caption("BUSCAMINAS")
pygame.display.set_icon(icono)

#AUDIO
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

contador = 0
corriendo = True
mostrar_inicio = True                                                                      # Diccionario para las banderas
mostrar_nivel=False
jugar=False
while corriendo:
    if mostrar_inicio:
        pantalla_inicio(pantalla, font_inicio)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN  and event.button == 1:
                if boton_jugar.collidepoint(event.pos):
                    jugar=True
                    mostrar_inicio = False
                    tablero = crear_matriz_buscaminas(8,8,10)
                    estados = crear_diccionario_estados(8,8)
                    banderas = crear_diccionario_banderas(8,8)
                    matriz_completa = matriz_minas_contiguas(8,8, tablero)
                    

                    evento=event.pos
                elif boton_nivel.collidepoint(event.pos):
                    mostrar_inicio=False
                    mostrar_nivel=True
                elif boton_salir.collidepoint(event.pos):
                    corriendo = False
    if mostrar_nivel==True:
        pantalla.blit(imagen_fondo, (0, 0))
        # Dibujar botones
        pygame.draw.rect(pantalla, (75, 83, 32), boton_facil)
        pygame.draw.rect(pantalla, (75, 83, 32), boton_medio)  
        pygame.draw.rect(pantalla, (75, 83, 32), boton_dificil)   
        pantalla.blit(texto_boton_Facil, (boton_facil.x + 60, boton_facil.y + 10))
        pantalla.blit(texto_boton_medio, (boton_medio.x + 53, boton_medio.y + 10))
        pantalla.blit(texto_boton_Dificil, (boton_dificil.x + 30, boton_dificil.y + 10))
        pygame.display.update()
    elif jugar==True:
        pantalla.fill(COLOR_TABLERO)
        margen = 2
        desplazamiento_x = (PANTALLA_ANCHO - len(matriz_completa[0]) * (50 + margen)) // 2
        desplazamiento_y = (PANTALLA_ALTO - len(matriz_completa) * (50 + margen)) // 2
        
        crear_rectangulos(matriz_completa, estados, pantalla, desplazamiento_x, desplazamiento_y, margen=2)
        
        redibujar_bandera(banderas, desplazamiento_x, desplazamiento_y, evento)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                                        # Clic izquierdo para descubrir cuadrados
                if manejar_perdida(matriz_completa, estados, event.pos, desplazamiento_x, desplazamiento_y):
                    limpiar_tablero(estados, matriz_completa)                                 
                else:
                    event=event.pos
                    descubre_casillero(estados,banderas,event,desplazamiento_x,desplazamiento_y)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:                                      # Clic derecho para poner/sacar banderas
                event=event.pos

                poner_sacar_banderas(estados,banderas,event,desplazamiento_x,desplazamiento_y)

            elif event.type == pygame.QUIT:
                corriendo = False
                print("cerrando juego...")

        pygame.display.flip()

pygame.quit()