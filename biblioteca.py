import pygame
import random

#-----------------------------  PANTALLA  ------------------------------------------------

PANTALLA_ALTO = 800
PANTALLA_ANCHO = 600
RESOLUCION_PANTALLA = (PANTALLA_ANCHO, PANTALLA_ALTO)


pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA)
color_fondo = [127, 157, 235]
posicion_personaje = [400, 300]


#-----------------------------  COLORES  -------------------------------------------------

# Colores: RGB[A] (Red, Green, Blue) [Alpha] -> 0 - 255

COLOR_ROJO = (255, 0, 0)
COLOR_NARANJA = (245, 79, 7)
COLOR_AZUL_CLARO = (127, 157, 235)
COLOR_FUCSIA = (204, 6, 161)
COLOR_TABLERO = (169, 169, 169)

#----------------------------  FUENTE   -------------------------------------------------

pygame.font.init()

font_inicio=pygame.font.Font("Buscaminas_progra-1_UTN/img/mifuente.otf",36)


#---------------------------  IMAGENES  -------------------------------------------------

icono=pygame.image.load("Buscaminas_progra-1_UTN/img/logo_app.png")

imagen_cuadrado=pygame.image.load("Buscaminas_progra-1_UTN/img/CUADRADO_BUSCAMINA.jpg")

imagen_cuadrado=pygame.transform.scale(imagen_cuadrado,(50,50))

imagen_mina = pygame.image.load("Buscaminas_progra-1_UTN/img/mina.png")
imagen_mina = pygame.transform.scale(imagen_mina, (50, 50))

imagen_bandera = pygame.image.load("Buscaminas_progra-1_UTN/img/bandera.png")
imagen_bandera = pygame.transform.scale(imagen_mina, (50, 50))

#--------------------------- BOTONES  --------------------------------------------------

boton_jugar=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2-50,200,50)

boton_salir=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2+50,200,50)

texto_boton_jugar=font_inicio.render("Jugar",True,(0,0,0))

texto_boton_salir=font_inicio.render("Salir",True,(255,255,255))










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

    #FALTA QUE LO PONGA EN EL MEDIO

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
                    #libera cuadrados de alrededor      FALTA  REVISAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    pass
                
    return matriz







def test_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"({matriz[i][j]})",end=" ")
        print("")