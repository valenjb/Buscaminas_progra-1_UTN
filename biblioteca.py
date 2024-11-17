import pygame
import random
from config import *



#PANTALLA DE
def pantalla_inicio():
    pantalla.fill((128, 0, 128))
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



#LOGICA DE MINAS
def inicializar_matriz(cant_filas:int , cant_colum:int)->list:
    matriz=[]
    for _ in range(cant_filas):
            fila=[0]*cant_colum
            #print(fila)
            matriz.append(fila)
    return matriz




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


def test_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print("")    