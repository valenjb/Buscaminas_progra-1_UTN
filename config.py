import pygame

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

font_inicio=pygame.font.Font("font/mifuente.otf",24)


#---------------------------  IMAGENES  -------------------------------------------------

icono=pygame.image.load("img/logo_app.png")

imagen_cuadrado=pygame.image.load("img/CUADRADO_BUSCAMINA.jpg")

imagen_cuadrado=pygame.transform.scale(imagen_cuadrado,(50,50))

imagen_mina = pygame.image.load("img/mina.png")
imagen_mina = pygame.transform.scale(imagen_mina, (50, 50))

imagen_bandera = pygame.image.load("img/bandera.png")
imagen_bandera = pygame.transform.scale(imagen_mina, (50, 50))

#--------------------------- BOTONES  --------------------------------------------------

boton_jugar=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2-50,200,50)

boton_salir=pygame.Rect(PANTALLA_ANCHO/2-100,PANTALLA_ALTO/2+50,200,50)

texto_boton_jugar=font_inicio.render("Jugar",True,(0,0,0))

texto_boton_salir=font_inicio.render("Salir",True,(255,255,255))