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
pygame.mixer.music.set_volume(0.2)

contador = 0
corriendo = True
mostrar_inicio = True                                                                      # Diccionario para las banderas
mostrar_nivel=False
jugar=False
sonido_mutado = False
mensaje_perder_mostrado = False

while corriendo:
    if mostrar_inicio:
        pantalla_inicio(sonido_mutado, pantalla, font_inicio)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_mute.collidepoint(event.pos):
                    sonido_mutado = cambiar_estado_sonido(sonido_mutado)

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
        mostrar_niveles(pantalla,imagen_fondo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False


    elif jugar == True:
        pantalla.fill(COLOR_TABLERO)
        margen = 2
        desplazamiento_x = (PANTALLA_ANCHO - len(matriz_completa[0]) * (50 + margen)) // 2
        desplazamiento_y = (PANTALLA_ALTO - len(matriz_completa) * (50 + margen)) // 2

        crear_rectangulos(matriz_completa, estados, pantalla, desplazamiento_x, desplazamiento_y, margen=2)
        redibujar_bandera(banderas, desplazamiento_x, desplazamiento_y, evento)
        boton_reiniciar = dibujar_boton_reiniciar(pantalla,imagen_reiniciar, 243, 640)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                if boton_reiniciar.collidepoint(event.pos):
                    tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado = reiniciar_partida(tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado)
                if manejar_perdida(matriz_completa, estados, pos, desplazamiento_x, desplazamiento_y, banderas) and mensaje_perder_mostrado == False:
                    print("¡Hiciste clic en una mina! \n Fin del juego.")
                    mensaje_perder_mostrado = True
                    limpiar_tablero(estados, matriz_completa, banderas)
                else:
                    descubre_casillero(estados, banderas, pos, desplazamiento_x, desplazamiento_y,matriz_completa)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = event.pos
                poner_sacar_banderas(estados, banderas, pos, desplazamiento_x, desplazamiento_y)

    pygame.display.flip()
pygame.quit()