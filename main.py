import pygame
import random
import json
from biblioteca import *
from config import *

pygame.display.set_caption("BUSCAMINA")

pygame.display.set_icon(icono)



contador = 0
corriendo = True
mostrar_inicio=True

while corriendo == True:

    if mostrar_inicio:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo=False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio=False
                if boton_salir.collidepoint(event.pos):
                    corriendo=False
    else:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento)


        #pantalla.blit(imagen_cuadrado,(50,0))
        pygame.display.flip()

pygame.quit()