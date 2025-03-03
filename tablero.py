
import pygame
#Se establecen los colores que usaremos
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
YELLOW = (255, 255, 0)
AMARILLO_CLARO = (255, 255, 200)
NARANJA = (255, 140, 0)
GRIS = (128, 128, 128)

COLORES = {
    "NEGRO": NEGRO,
    "BLANCO": BLANCO,
    "AZUL": AZUL,
    "VERDE": VERDE,
    "ROJO": ROJO,
    "YELLOW": YELLOW,
    "AMARILLO_CLARO": AMARILLO_CLARO,
    "NARANJA": NARANJA,
    "GRIS": GRIS,
}

#Sección para crear el tablero 
def tablero(app):
    #Aplicamos color
    pygame.draw.rect(app, AMARILLO_CLARO, (100, 10, 597, 597))
    pygame.draw.rect(app, GRIS, (369, 13, 63, 597))
    pygame.draw.rect(app, GRIS, (100, 279, 574, 63))
    pygame.draw.rect(app, VERDE, (103, 413, 195, 195))
    pygame.draw.rect(app, AZUL, (503, 413, 195, 195))
    pygame.draw.rect(app, YELLOW, (103, 13, 195, 195))
    pygame.draw.rect(app, ROJO, (503, 13, 195, 195))
    pygame.draw.rect(app, NARANJA, (303, 126, 61, 24))
    pygame.draw.rect(app, NARANJA, (437, 126, 61, 24))
    pygame.draw.rect(app, NARANJA, (369, 13, 63, 24))
    pygame.draw.rect(app, NARANJA, (216, 213, 24, 61))
    pygame.draw.rect(app, NARANJA, (216, 347, 24, 61))
    pygame.draw.rect(app, NARANJA, (559, 347, 24, 61))
    pygame.draw.rect(app, NARANJA, (559, 213, 24, 61))
    pygame.draw.rect(app, NARANJA, (369, 584, 63, 24))
    pygame.draw.rect(app, NARANJA, (103, 279, 24, 63))
    pygame.draw.rect(app, NARANJA, (674, 279, 24, 63))
    pygame.draw.rect(app, NARANJA, (303, 467, 61, 26))
    pygame.draw.rect(app, NARANJA, (437, 467, 61, 26))
    pygame.draw.rect(app, GRIS, (353, 262, 97, 97))
    
    
    puntos = [(100, 10), (700, 10), (700, 610), (100, 610), (100, 10)] 
    pygame.draw.lines(app, NEGRO, True, puntos, 5) #Borde del tablero
    #Parte interna del tablero
    pygame.draw.line(app, NEGRO, (300,10), (300, 610), 5)
    pygame.draw.line(app, NEGRO, (500,10), (500, 610), 5)
    pygame.draw.line(app, NEGRO, (100,210), (700, 210), 5)
    pygame.draw.line(app, NEGRO, (100,410), (700, 410), 5)
    pygame.draw.line(app, NEGRO, (300,210), (500, 410), 5)
    pygame.draw.line(app, NEGRO, (300,410), (500, 210), 5)
    lol = [(350, 260), (450, 260), (450, 360), (350, 360), (350, 260)]
    pygame.draw.lines(app, NEGRO, True, lol, 5)
    pygame.draw.line(app, NEGRO, (366, 10), (366, 260), 5)
    pygame.draw.line(app, NEGRO, (434, 10), (434, 260), 5)
    pygame.draw.line(app, NEGRO, (366, 360), (366, 610), 5)
    pygame.draw.line(app, NEGRO, (434, 360), (434, 610), 5)
    pygame.draw.line(app, NEGRO, (100, 276), (350, 276), 5)
    pygame.draw.line(app, NEGRO, (100, 344), (350, 344), 5)
    pygame.draw.line(app, NEGRO, (450, 276), (700, 276), 5)
    pygame.draw.line(app, NEGRO, (450, 344), (700, 344), 5)
    pygame.draw.line(app, NEGRO, (300, 38), (500, 38), 5)
    pygame.draw.line(app, NEGRO, (300, 66), (500, 66), 5)
    pygame.draw.line(app, NEGRO, (300, 94), (500, 94), 5)
    pygame.draw.line(app, NEGRO, (300, 123), (500, 123), 5)
    pygame.draw.line(app, NEGRO, (300, 152), (500, 152), 5)
    pygame.draw.line(app, NEGRO, (300, 181), (500, 181), 5)
    pygame.draw.line(app, NEGRO, (128, 210), (128, 410), 5)
    pygame.draw.line(app, NEGRO, (156, 210), (156, 410), 5)
    pygame.draw.line(app, NEGRO, (184, 210), (184, 410), 5)
    pygame.draw.line(app, NEGRO, (213, 210), (213, 410), 5)
    pygame.draw.line(app, NEGRO, (242, 210), (242, 410), 5)
    pygame.draw.line(app, NEGRO, (271, 210), (271, 410), 5)
    pygame.draw.line(app, NEGRO, (528, 210), (528, 410), 5)
    pygame.draw.line(app, NEGRO, (556, 210), (556, 410), 5)
    pygame.draw.line(app, NEGRO, (584, 210), (584, 410), 5)
    pygame.draw.line(app, NEGRO, (613, 210), (613, 410), 5)
    pygame.draw.line(app, NEGRO, (642, 210), (642, 410), 5)
    pygame.draw.line(app, NEGRO, (671, 210), (671, 410), 5)
    pygame.draw.line(app, NEGRO, (300, 438), (500, 438), 5)
    pygame.draw.line(app, NEGRO, (300, 466), (500, 466), 5)
    pygame.draw.line(app, NEGRO, (300, 494), (500, 494), 5)
    pygame.draw.line(app, NEGRO, (300, 523), (500, 523), 5)
    pygame.draw.line(app, NEGRO, (300, 552), (500, 552), 5)
    pygame.draw.line(app, NEGRO, (300, 581), (500, 581), 5)


    