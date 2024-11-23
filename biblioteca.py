import pygame
import random
from config import *

#-----------------------------  PANTALLA  ------------------------------------------------------


def pantalla_inicio(pantalla,font_inicio):
    pantalla.fill((0, 0, 0))
    dibujar_texto("BUSCAMINA",font_inicio,(255,255,255),PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2-100)
    pygame.draw.rect(pantalla,(255, 255, 0),boton_jugar)
    pygame.draw.rect(pantalla,(255, 0, 0),boton_salir)
    pantalla.blit(texto_boton_jugar,(boton_jugar.x+50,boton_jugar.y+10))
    pantalla.blit(texto_boton_salir,(boton_salir.x+50,boton_salir.y+10))
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


# """ FUNCION PARA CUADRADOS (AGREGAR FLAG)"""
# def crear_cuadrados_tablero(matriz,tablero,pantalla):
#         for fila in range(len(tablero)):
#             for columna in range(len(tablero[0])):
#                 desplazamiento_x = (PANTALLA_ANCHO - len(matriz) * 50) // 2
#                 desplazamiento_y = (PANTALLA_ALTO - len(matriz) * 50) // 2
#                 x = desplazamiento_x + columna * 50  # Desplazamiento en el eje X
#                 y = desplazamiento_y + fila * 50
#                 pantalla.blit(imagen_cuadrado, (x, y)) 



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



def crear_rectangulos(matriz, estados, pantalla: pygame.Surface):
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            desplazamiento_x = (PANTALLA_ANCHO - len(matriz) * 50) // 2
            desplazamiento_y = (PANTALLA_ALTO - len(matriz) * 50) // 2
            x = desplazamiento_x + col * 50
            y = desplazamiento_y + fila * 50

            if estados[(fila, col)]:  # Si está cubierto (estado true)
                pantalla.blit(imagen_cuadrado, (x, y))
            else:  # Descubierto
                numero = matriz[fila][col]
                texto = font_inicio.render(str(numero), True, (0, 0, 0))
                pantalla.blit(texto, (x + 15, y + 10))
