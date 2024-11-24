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
COLOR_AZUL_CLARO = (127, 157, 235)
COLOR_TABLERO = (169, 169, 169)

#----------------------------  FUENTE   -------------------------------------------------

pygame.font.init()

font_inicio=pygame.font.Font("font/mifuente.otf",24)


#---------------------------  IMAGENES  -------------------------------------------------

icono=pygame.image.load("img/logo_app.png")

imagen_cuadrado=pygame.image.load("img/CUADRADO_BUSCAMINA.jpg")
imagen_cuadrado=pygame.transform.scale(imagen_cuadrado,(50,50))

imagen_mina = pygame.image.load("img/mina.png")
imagen_mina = pygame.transform.scale(imagen_mina, (50, 50))  #PONERLO CON RESPECTO A EL TAMAÑO DE PANTALLA

imagen_bandera = pygame.image.load("img/bandera.png")
imagen_bandera = pygame.transform.scale(imagen_bandera, (50, 50))

imagen_fondo = pygame.image.load("img/fondo_menu.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (RESOLUCION_PANTALLA))

#--------------------------- BOTONES  --------------------------------------------------

boton_ancho = 200
boton_alto = 50

boton_nivel = pygame.Rect(200, 300, boton_ancho, boton_alto)
boton_jugar = pygame.Rect(200, 375, boton_ancho, boton_alto)
boton_puntajes = pygame.Rect(200, 450, boton_ancho, boton_alto)
boton_salir = pygame.Rect(200, 525, boton_ancho, boton_alto)

texto_boton_nivel=font_inicio.render("Nivel",True,(255,255,255))

texto_boton_jugar=font_inicio.render("Jugar",True,(255,255,255))

texto_boton_puntajes=font_inicio.render("Puntajes",True,(255,255,255))

texto_boton_salir=font_inicio.render("Salir",True,(255,255,255))