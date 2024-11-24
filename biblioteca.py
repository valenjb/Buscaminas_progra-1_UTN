import pygame
import random
from config import *

#-----------------------------  PANTALLA  ------------------------------------------------------


def pantalla_inicio(pantalla, font_inicio):
    pantalla.blit(imagen_fondo, (0, 0))

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
                texto = font_inicio.render(str(numero), True, (0, 0, 0))
                pantalla.blit(texto, (x + 17, y + 10)) #el +15 y +10 es para centrar el numero y que quede mejor

            pygame.draw.line(pantalla, (0, 0, 0), (x, y), (x + 50, y), margen)  # Línea arriba
            pygame.draw.line(pantalla, (0, 0, 0), (x, y), (x, y + 50), margen)  # Línea izq
            pygame.draw.line(pantalla, (0, 0, 0), (x + 50, y), (x + 50, y + 50), margen)  # Línea der
            pygame.draw.line(pantalla, (0, 0, 0), (x, y + 50), (x + 50, y + 50), margen)  # Linea abajo




def descubre_casillero(estados,banderas,eventpos,desplazamiento_x,desplazamiento_y):
    mouse_x, mouse_y = eventpos
    
    fila = (mouse_y - desplazamiento_y) // 50
    columna = (mouse_x - desplazamiento_x) // 50
    
    if (fila, columna) in estados and banderas[(fila,columna)]==False: # Verifica que no tenga bandera, si no tiene descubre la casilla
        #print(fila,"---------",columna,"------------",banderas)
        #print(estados,"-----------estadooooooooos")
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



def mostrar_bombas(matriz, estados, pantalla, desplazamiento_x, desplazamiento_y):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == -1 and estados[(fila, columna)] == False:  # Si es una bomba y está descubierta
                x = desplazamiento_x + columna * 50 
                y = desplazamiento_y + fila * 50    
                pantalla.blit(imagen_mina, (x, y))   
