import pygame
import random
from config import *

#-----------------------------  PANTALLA  ------------------------------------------------------


def pantalla_inicio(sonido_mutado, pantalla, font_inicio):
    pantalla.blit(imagen_fondo, (0, 0))
    dibujar_boton_sonido(sonido_mutado, imagen_unmute, imagen_mute, boton_mute)
    # Crear texto con gradiente
    texto_gradiente = texto_con_gradiente("BUSCAMINAS", font_inicio, (255, 0, 0), (0, 0, 0), PANTALLA_ANCHO, PANTALLA_ALTO)
    pantalla.blit(texto_gradiente, (PANTALLA_ANCHO / 2 - texto_gradiente.get_width() // 2, PANTALLA_ALTO / 2 - 180))

    # Dibujar botones
    pygame.draw.rect(pantalla, (75, 83, 32), boton_nivel)
    pygame.draw.rect(pantalla, (75, 83, 32), boton_jugar)  
    pygame.draw.rect(pantalla, (75, 83, 32), boton_puntajes)
    pygame.draw.rect(pantalla, (115, 18, 18), boton_salir)   
    pantalla.blit(texto_boton_nivel, (boton_nivel.x + 60, boton_nivel.y + 10))
    pantalla.blit(texto_boton_jugar, (boton_jugar.x + 53, boton_jugar.y + 10))
    pantalla.blit(texto_boton_puntajes, (boton_puntajes.x + 30, boton_puntajes.y + 10))
    pantalla.blit(texto_boton_salir, (boton_salir.x + 58, boton_salir.y + 10))
    pygame.display.update()


def dibujar_texto(texto,fuente,color,x,y):
    img=fuente.render(texto,True,color)
    pantalla.blit(img,(x,y))


def generar_color_aleatorio()->list:
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]



#-----------------------------  LOGICA DE MINAS  ------------------------------------------------


def inicializar_matriz(cant_filas:int , cant_colum:int)->list:
    matriz=[]
    for _ in range(cant_filas):
            fila=[0]*cant_colum
            #print(fila)
            matriz.append(fila)
    return matriz



#-----------------------------  MATRIZ  ------------------------------------------------


def crear_matriz_buscaminas(cant_filas:int, cant_colum:int, minas:int)->list:
    matriz=inicializar_matriz(cant_filas,cant_colum)
    minas_colocadas=0
    
    while minas_colocadas < minas:
        fila_random=random.randint(0,cant_filas-1)
        columna_random=random.randint(0,cant_colum-1)

        if matriz[fila_random][columna_random]!=-1:
            matriz[fila_random][columna_random]=-1
            minas_colocadas+=1
            
    return matriz


def descrubir_minas_contiguas(cant_filas:int, cant_colum:int, matriz:list)->int:
    minas=0

    for i in range(cant_filas-1,cant_filas+2):#Pongo -1 y +2 para recorrer las diagonales y los costado
        for j in range(cant_colum-1,cant_colum+2):
            if i >=0 and i<len(matriz): #verifico que este dentro de las dimensiones de la matriz
                if (j >=0 and j<len(matriz[0]))and (i!=cant_filas or j != cant_colum):#Lo mismo aca,despues para que no recorra el mismo elemento.
                    if matriz[i][j]==-1:
                        minas+=1
    return minas


def matriz_minas_contiguas(cant_filas:int, cant_column:int, matriz:list)->list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==0:
                pistas=descrubir_minas_contiguas(i,j,matriz)  #Mando la posicion de la matriz a fijar si tiene minas contiguas
                if pistas > 0:
                    matriz[i][j]=pistas

                elif pistas==0:
                    pass#libera cuadrados de alrededor      FALTA  REVISAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return matriz


def test_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"({matriz[i][j]})",end=" ")
        print("")



def crear_diccionario_estados(cant_filas: int, cant_colum: int) -> dict:
    return {(fila, col): True 
            for fila in range(cant_filas) 
            for col in range(cant_colum)}

def crear_diccionario_banderas(cant_filas: int, cant_colum: int) -> dict:
    return {(fila, col): False
            for fila in range(cant_filas) 
            for col in range(cant_colum)}



def crear_rectangulos(matriz, estados, pantalla:pygame.Surface, desplazamiento_x, desplazamiento_y, margen=2):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x = desplazamiento_x + j * 50
            y = desplazamiento_y + i * 50

            if estados[(i, j)]:  # Si está cubierto (estando True)
                pantalla.blit(imagen_cuadrado, (x, y))
            elif matriz[i][j] == -1 and estados[(i, j)] == False:  # Si es una mina y descubierto
                pantalla.blit(imagen_mina, (x, y))
            elif matriz[i][j] == 0  and estados[(i, j)] == False:  # Si es un cuadrado vacío
                pygame.draw.rect(pantalla, COLOR_TABLERO, (x, y, 50, 50))
            else:  # Si es un número y se lo descubre
                numero = matriz[i][j]
                match numero:
                    case 1:
                        color = (0, 0, 255)  # Azul
                    case 2:
                        color = (0, 128, 0)  # Verde
                    case 3:
                        color = (255, 0, 0)  # Rojo
                    case 4:
                        color = (0, 0, 128)  # Azul oscuro
                    case 5:
                        color = (128, 0, 0)  # Rojo oscuro
                    case 6:
                        color = (0, 128, 128)  # Verde azulado
                    case 7:
                        color = (75, 41, 41)  # Negro
                    case 8:
                        color = (0, 0, 0)  # Gris

                texto = font_inicio.render(str(numero), True, color)
                pantalla.blit(texto, (x + 17, y + 10)) #el +17 y +10 es para centrar el numero y que quede mejor

            pygame.draw.line(pantalla, (0, 0, 0), (x, y), (x + 50, y), margen)  # Línea arriba
            pygame.draw.line(pantalla, (0, 0, 0), (x, y), (x, y + 50), margen)  # Línea izq
            pygame.draw.line(pantalla, (0, 0, 0), (x + 50, y), (x + 50, y + 50), margen)  # Línea der
            pygame.draw.line(pantalla, (0, 0, 0), (x, y + 50), (x + 50, y + 50), margen)  # Linea abajo



def descubre_casillero(estados, banderas, eventpos, desplazamiento_x, desplazamiento_y, matriz):
    mouse_x, mouse_y = eventpos
    fila = (mouse_y - desplazamiento_y) // 50
    columna = (mouse_x - desplazamiento_x) // 50

    if (fila, columna) in estados and banderas[(fila, columna)] == False:  # 
        if matriz[fila][columna] == 0:  # Si es un 0, descubre el área
            descubrir_area(matriz, estados, fila, columna,banderas)
        else:  # Si es un número, solo descubre esa celda
            estados[(fila, columna)] = False

def poner_sacar_banderas(estados,banderas,eventpos,desplazamiento_x,desplazamiento_y):
    mouse_x, mouse_y = eventpos
    
    
    fila = (mouse_y - desplazamiento_y) // 50
    columna = (mouse_x - desplazamiento_x) // 50
    if (fila, columna) in estados and estados[(fila, columna)] == True: 
                    #print(fila,"---------",columna,"------------",banderas) # Revisa si estás en un casillero y si este está tapado
                    if banderas[(fila, columna)] == False:                              # Si la posicion no está en la misma posicion de una bandera, pone una bandera
                        banderas[(fila, columna)] = True
                        #print(banderas)  
                    else:                                                            # Si ya tiene bandera, saca la bandera
                        banderas[(fila, columna)]=False
                        #print(banderas)
    


def redibujar_bandera(banderas,desplazamiento_x,desplazamiento_y,eventpos):
    mouse_x,mouse_y = eventpos
    
    fila = (mouse_y - desplazamiento_y) // 50
    columna = (mouse_x - desplazamiento_x) // 50
    for (fila, columna) in banderas:    
        if banderas[(fila,columna)]==True:                                        # Redibujar las banderas
            x = desplazamiento_x + columna * 50
            y = desplazamiento_y + fila * 50
            pantalla.blit(imagen_bandera, (x, y))


def texto_con_gradiente(texto, fuente, color_inicio, color_fin, ancho, alto):
    # Renderizar texto en blanco para tomar las dimensiones
    texto_superficie = fuente.render(texto, True, (255, 255, 255))
    texto_rect = texto_superficie.get_rect(center=(ancho // 2, alto // 2))
    
    # Crear superficie para el texto
    superficie = pygame.Surface((texto_rect.width, texto_rect.height), pygame.SRCALPHA)
    
    # Crear gradiente
    for i in range(texto_rect.height):
        # Interpolación lineal entre color_inicio y color_fin
        factor = i / texto_rect.height
        color_actual = (
            int(color_inicio[0] + factor * (color_fin[0] - color_inicio[0])),
            int(color_inicio[1] + factor * (color_fin[1] - color_inicio[1])),
            int(color_inicio[2] + factor * (color_fin[2] - color_inicio[2]))
        )
        pygame.draw.line(superficie, color_actual, (0, i), (texto_rect.width, i))
    
    # Combinar texto y gradiente (multiplicación alfa)
    superficie.blit(texto_superficie, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
    return superficie


def manejar_perdida(matriz, estados, eventpos, desplazamiento_x, desplazamiento_y, banderas):
    mouse_x, mouse_y = eventpos
    fila = (mouse_y - desplazamiento_y) // 50
    columna = (mouse_x - desplazamiento_x) // 50
    retorno=False
    if (fila, columna) in estados and matriz[fila][columna] == -1 and banderas[(fila,columna)]== False:
        retorno=True  # pierde
    return retorno  # no perdio

def limpiar_tablero(estados, matriz, banderas):
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            estados[(i,j)] = False
            banderas[(i,j)] = False



def mostrar_niveles(pantalla,imagen_fondo):
    pantalla.blit(imagen_fondo, (0, 0))

    pygame.draw.rect(pantalla, (75, 83, 32), boton_facil)
    pygame.draw.rect(pantalla, (75, 83, 32), boton_medio)  
    pygame.draw.rect(pantalla, (75, 83, 32), boton_dificil)   

    pantalla.blit(texto_boton_Facil, (boton_facil.x + 60, boton_facil.y + 10))
    pantalla.blit(texto_boton_medio, (boton_medio.x + 53, boton_medio.y + 10))
    pantalla.blit(texto_boton_Dificil, (boton_dificil.x + 30, boton_dificil.y + 10))

    pygame.display.update()


def dibujar_boton_reiniciar(pantalla, imagen_boton, x, y):
    boton_reiniciar = pygame.Rect(x, y, imagen_boton.get_width(), imagen_boton.get_height())
    pantalla.blit(imagen_reiniciar, (boton_reiniciar.x, boton_reiniciar.y))
    return boton_reiniciar



def reiniciar_partida(tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado):
    tablero = crear_matriz_buscaminas(8, 8, 10)
    estados = crear_diccionario_estados(8, 8)
    banderas = crear_diccionario_banderas(8, 8)
    matriz_completa = matriz_minas_contiguas(8, 8, tablero)
    mensaje_perder_mostrado = False
    print("Partida reiniciada.")
    return tablero, estados, banderas, matriz_completa, mensaje_perder_mostrado

def descubrir_area(matriz, estados, fila, columna,banderas):
    # Condiciones base
    if (fila < 0 or fila >= len(matriz) or columna < 0 or columna >= len(matriz[0]) or estados[(fila, columna)] == False):  # Si está fuera de los límites o ya descubierta
        return

#Descubre la celda actual
    estados[(fila, columna)] = False

    if banderas[(fila, columna)]==True:
        estados[(fila,columna)]=True

    # Si la celda no es 0, no continúa
    if matriz[fila][columna] != 0 :
        return

    # Llama a las celdas adyacentes (8 direcciones)
    descubrir_area(matriz, estados, fila - 1, columna,banderas)  # Arriba
    descubrir_area(matriz, estados, fila + 1, columna,banderas)  # Abajo
    descubrir_area(matriz, estados, fila, columna - 1,banderas)  # Izquierda
    descubrir_area(matriz, estados, fila, columna + 1,banderas)  # Derecha
    descubrir_area(matriz, estados, fila - 1, columna - 1,banderas)  # Arriba-Izquierda
    descubrir_area(matriz, estados, fila - 1, columna + 1,banderas)  # Arriba-Derecha
    descubrir_area(matriz, estados, fila + 1, columna - 1,banderas)  # Abajo-Izquierda
    descubrir_area(matriz, estados, fila + 1, columna + 1,banderas)  # Abajo-Derecha


def cambiar_estado_sonido(sonido_mutado):
    sonido_mutado = not sonido_mutado
    if sonido_mutado:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(0.1)
    return sonido_mutado

def dibujar_boton_sonido(sonido_mutado, imagen_unmute, imagen_mute, boton_mute):
    if sonido_mutado:
        pantalla.blit(imagen_mute, boton_mute)
    else:
        pantalla.blit(imagen_unmute, boton_mute)