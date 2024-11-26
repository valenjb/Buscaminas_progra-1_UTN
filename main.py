import pygame
from biblioteca import *
from config import *
import random
import json
pygame.init()
#NOMBRE DE ARCHIVO E ICONO
pygame.display.set_caption("BUSCAMINAS")
pygame.display.set_icon(icono)



mi_evento=pygame.USEREVENT + 1
un_segundo=1000
pygame.time.set_timer(mi_evento,un_segundo)
contador_segundos=0
mi_texto=font_timer.render(f"{contador_segundos}0:00",True,"white")




#AUDIO
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

sonido_mutado = False

contador = 0
corriendo = True
mostrar_inicio = True                                                                      # Diccionario para las banderas
mostrar_nivel=False
mostrar_puntaje = False
jugar=False
mensaje_perder_mostrado = False
ganaste = False
juego_terminado = False

while corriendo:
    if mostrar_inicio:
        puntos = 0
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
                    test_matriz(matriz_completa)
                    evento=event.pos

                elif boton_nivel.collidepoint(event.pos):
                    mostrar_inicio=False
                    mostrar_nivel=True

                elif boton_salir.collidepoint(event.pos):
                    corriendo = False

                elif boton_puntajes.collidepoint(event.pos):
                    mostrar_inicio = False
                    mostrar_puntaje = True
                    
    if mostrar_nivel==True:
        mostrar_niveles(pantalla,imagen_fondo)
        dibujar_boton_volver(pantalla, boton_volver, texto_boton_volver)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver.collidepoint(event.pos):
                    mostrar_inicio = True
                    mostrar_nivel = False

    elif mostrar_puntaje == True:
        mostrar_puntajes(pantalla,imagen_fondo_puntajes)
        dibujar_boton_volver(pantalla, boton_volver, texto_boton_volver)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver.collidepoint(event.pos):
                    mostrar_inicio = True
                    mostrar_puntaje = False

    elif jugar == True:
        pantalla.blit(imagen_fondo_juego, (0, 0))
        
        desplazamiento_x = (PANTALLA_ANCHO - len(matriz_completa[0]) * (50)) // 2
        desplazamiento_y = (PANTALLA_ALTO - len(matriz_completa) * (50)) // 2

        dibujar_fondo_tablero(pantalla, matriz_completa, COLOR_TABLERO)
        dibujar_boton_volver(pantalla, boton_volver, texto_boton_volver)
        crear_rectangulos(matriz_completa, estados, pantalla, desplazamiento_x, desplazamiento_y, margen=2)
        redibujar_bandera(banderas, desplazamiento_x, desplazamiento_y, evento)
        boton_reiniciar = dibujar_boton_reiniciar(pantalla,imagen_reiniciar, 263, 670)
        mostrar_puntos_tablero(pantalla, puntos, font_inicio, (75, 83, 32), (255,255,255), desplazamiento_x + 27, desplazamiento_y - 75, 100, 50)
        dibujar_boton_timer(pantalla, boton_timer, mi_texto)

        if verificar_victoria(matriz_completa, estados) and ganaste == False:
            ganaste = True
            print("¡Ganaste!")
            limpiar_tablero(estados, matriz_completa, banderas)
            juego_terminado = True

        if juego_terminado:  
            nick = pedir_usuario(pantalla, font_inicio, imagen_fondo_puntajes)  # Pedir el nombre
            guardar_puntaje(nick, puntos)  
            mostrar_inicio = True 
            jugar = False
            ganaste = False
            contador_segundos = False
            juego_terminado = False


        for event in pygame.event.get():
            if event.type == mi_evento and not mensaje_perder_mostrado:
                minutos, segundos = contador_reloj(contador_segundos)
                mi_texto = font_timer.render(f"{minutos:02}:{segundos:02}", True, "white")
                contador_segundos += 1
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver.collidepoint(event.pos):
                    mostrar_inicio = True           # Volver al menú inicial
                    jugar = False 
                    mensaje_perder_mostrado = False
                    ganaste = False
                pos = event.pos
                if boton_reiniciar.collidepoint(event.pos):
                    puntos = 0
                    contador_segundos=0
                    tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado, ganaste = reiniciar_partida(tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado, ganaste)

                if manejar_perdida(matriz_completa, estados, pos, desplazamiento_x, desplazamiento_y, banderas) and mensaje_perder_mostrado == False:
                    print("¡Hiciste clic en una mina! \n Fin del juego.")
                    mensaje_perder_mostrado = True
                    limpiar_tablero(estados, matriz_completa, banderas)
                elif not manejar_perdida(matriz_completa, estados, pos, desplazamiento_x, desplazamiento_y, banderas) and mensaje_perder_mostrado == False:
                    puntos = descubre_casillero(estados, banderas, pos, desplazamiento_x, desplazamiento_y,matriz_completa, puntos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = event.pos
                poner_sacar_banderas(estados, banderas, pos, desplazamiento_x, desplazamiento_y)
    pygame.display.flip()
pygame.quit()