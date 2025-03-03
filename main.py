import random
import pygame
from tablero import tablero
from areas import incasillas
from jugadores import Jugador

#Se cargan las imágenes de los dados asociados a su valor correspondiente
imagenes_dados = {
    1: pygame.image.load("imagenes/dado1.png"),
    2: pygame.image.load("imagenes/dado2.png"),
    3: pygame.image.load("imagenes/dado3.png"),
    4: pygame.image.load("imagenes/dado4.png"),
    5: pygame.image.load("imagenes/dado5.png"),
    6: pygame.image.load("imagenes/dado6.png"),
}

pygame.init()  #Iniciamos pygame
app = pygame.display.set_mode((900, 710))  #Establecemos el tamaño de la ventana
pygame.display.set_caption('Parqués')  #Le ponemos título a la ventana
app.fill((255, 255, 255))  #Establecemos un fondo blanco
tablero(app)

#Establecemos una función para calcular el valor de los dados en un rango
#entre 1 a 6, para cada dado
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    return dado1, dado2, total

def main():
    #Obtenemos la lista de casillas del tablero
    xdd = incasillas()  
    
    #Se inician las fichas en las posiciones de prisión
    jugadores = {
        "VERDE": Jugador("VERDE", (0, 255, 0), (190, 490)),  #Posición inicial para VERDE
        "AZUL": Jugador("AZUL", (0, 0, 255), (580, 490)),    #Posición inicial para AZUL
        "ROJO": Jugador("ROJO", (255, 0, 0), (580, 80)),    #Posición inicial para ROJO
        "AMARILLO": Jugador("AMARILLO", (255, 255, 0), (190, 80))  #Posición inicial para AMARILLO
    }
    #Establecemos una variable booleana 
    ejecutando = True
    dados = (1, 1, 2)  #Valores iniciales de los dados
    turno = list(jugadores.keys())  #Lista de jugadores en orden de turno
    indice_turno = 0 
    
    #Establecemos un bucle para que funcione siempre que el juego esté siendo ejecutado
    while ejecutando:
        #Dibujamos el tablero
        tablero(app) 
        
        #Mostramos los valores de los dados
        app.blit(imagenes_dados[dados[0]], (750, 250))
        app.blit(imagenes_dados[dados[1]], (750, 350))

        #Dibujamos las fichas en el tablero
        for jugador in jugadores.values():
            jugador.dibujar_fichas(app)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                #Siempre que se oprima enter, se lanzan los dados
                if evento.key == pygame.K_RETURN: 
                    dados = lanzar_dados()  
                    jugadorA = jugadores[turno[indice_turno]]  #Obtenemos el jugador actual
                    total_dados = dados[0] + dados[1]  #Sumamos el valor de los dados

                    #Se verifica si la suma de los dados es 5 y hay fichas en prisión
                    if total_dados == 5 and any(ficha.en_prision for ficha in jugadorA.fichas):
                        #Sacamos una ficha de prisión
                        if jugadorA.offprison(xdd):
                            print(f"{jugadorA.nombre} ha sacado una ficha de prisión.")
                        else:
                            print(f"{jugadorA.nombre} no pudo sacar una ficha de prisión.")
                    else:
                        #Se permite al jugador el elegir qué valor de cuál dado quiere usar
                        print(f"Turno de {jugadorA.nombre}. Valores de los dados: {dados[0]} y {dados[1]}")
                        print("Elige qué valor del dado usar (1 o 2):")
                        #Usamos un try en caso de que la selección no sea correcta
                        try:
                            eleccion_dado = int(input("Selecciona 1 o 2: ")) - 1
                            if 0 <= eleccion_dado < 2:
                                pasos = dados[eleccion_dado]
                                if not jugadorA.seleccionar_ficha(pasos, xdd, jugadores):
                                    print("No se pudo mover ninguna ficha.")
                            else:
                                print("Selección no válida.")
                        except ValueError:
                            print("Entrada no válida. Introduce 1 o 2.")
                    
                    #Aquí se cambia al siguiente jugador, a menos que se hayan obtenido dobles
                    if dados[0] != dados[1]:
                        indice_turno = (indice_turno + 1) % len(turno)
                    else:
                        print(f"{jugadorA.nombre} obtuvo dobles y juega de nuevo.")

        pygame.display.flip()  #Sirve para actualizar la pantalla
    pygame.quit()  #Función para abandonar el juego

if __name__ == "__main__":
    main()