import pygame
import random

pygame.font.init() 
# CONSTS
PANTALLA_ANCHO = 400
PANTALLA_ALTO = 400
RESOLUCION_PANTALLA = (PANTALLA_ANCHO, PANTALLA_ALTO)

color_fondo = [127, 157, 235]
posicion_personaje = [400, 300]

# COLORES: RGB[A] (Red, Green, Blue) [Alpha] -> 0 - 255
COLOR_ROJO = (255, 0, 0)
COLOR_NARANJA = (245, 79, 7)
COLOR_AZUL_CLARO = (127, 157, 235)
COLOR_FUCSIA = (204, 6, 161)

# Pantalla Principal
# pantalla = pygame.display.set_mode((800, 600))
# pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA)
pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA) # Ventana maximizable
# pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("BUSCAMINA")

# Imagenes:
icono=pygame.image.load("BUSCAMINA-PROYECTO\pngegg.png")
imagen_cuadrado=pygame.image.load("BUSCAMINA-PROYECTO\pngkit_white-button-png_2084464.png")
pygame.display.set_icon(icono)
imagen_cuadrado=pygame.transform.scale(imagen_cuadrado,(50,50))

#FUENTES
font_inicio=pygame.font.SysFont("Arial",36)


#BOTON
boton_jugar=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2-50,200,50)
boton_salir=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2+50,200,50)
texto_boton_jugar=font_inicio.render("Jugar",True,(0,0,0))
texto_boton_salir=font_inicio.render("Salir",True,(255,255,255))
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
matriz=crear_matriz_buscaminas(8,8,20)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print("")    