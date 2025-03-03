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

def GODmode():
    while True:
        try:
            dado1 = int(input("Ingresa el valor del primer dado (1-6): "))
            dado2 = int(input("Ingresa el valor del segundo dado (1-6): "))
            if 1 <= dado1 <= 6 and 1 <= dado2 <= 6:
                return dado1, dado2
            else:
                print("Los valores deben estar entre 1 y 6. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Introduce números enteros.")

def main():
    #Esta es la función del modo desarrollador, sirve para seleccionar manualmente los números de los dados
    #Inicia desactivado
    GODmod = False
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
        app.fill((255, 255, 255))  # Limpiar la pantalla
        tablero(app)  # Dibujar el tablero

        # Mostrar los valores de los dados
        app.blit(imagenes_dados[dados[0]], (750, 250))
        app.blit(imagenes_dados[dados[1]], (750, 350))

        # Dibujar las fichas en el tablero
        for jugador in jugadores.values():
            jugador.dibujar_fichas(app)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Al presionar ENTER
                    if GODmod:
                        print("GOD mode: Ingresa los valores de los dados.")
                        nuevos_dados = GODmode()  # Solicitar valores de los dados
                        if nuevos_dados:  # Si se ingresaron valores válidos
                            dados = nuevos_dados
                    else:
                        dados = lanzar_dados()  # Lanzar los dados aleatoriamente

                    jugador_actual = jugadores[turno[indice_turno]]  # Obtener el jugador actual
                    total_dados = dados[0] + dados[1]  # Suma de los dados

                    # Verificar si la suma de los dados es 5 y hay fichas en prisión
                    if total_dados == 5 and any(ficha.en_prision for ficha in jugador_actual.fichas):
                        if jugador_actual.offprison(xdd):
                            print(f"{jugador_actual.nombre} ha sacado una ficha de prisión.")
                        else:
                            print(f"{jugador_actual.nombre} no pudo sacar una ficha de prisión.")
                    else:
                        # Permitir al jugador elegir qué valor del dado usar
                        print(f"Turno de {jugador_actual.nombre}. Valores de los dados: {dados[0]} y {dados[1]}")
                        print("Elige qué valor del dado usar (1 o 2):")
                        try:
                            eleccion_dado = int(input("Selecciona 1 o 2: ")) - 1
                            if 0 <= eleccion_dado < 2:
                                pasos = dados[eleccion_dado]
                                if not jugador_actual.seleccionar_ficha(pasos, xdd, jugadores):
                                    print("No se pudo mover ninguna ficha.")
                            else:
                                print("Selección no válida.")
                        except ValueError:
                            print("Entrada no válida. Introduce 1 o 2.")

                    # Cambiar al siguiente jugador, a menos que se hayan obtenido dobles
                    if dados[0] != dados[1]:
                        indice_turno = (indice_turno + 1) % len(turno)
                    else:
                        print(f"{jugador_actual.nombre} obtuvo dobles y juega de nuevo.")

                # Si se presiona la tecla 9, se activa/desactiva el GODmode
                elif evento.key == pygame.K_9:
                    GODmod = not GODmod  # Alternar entre GODmode y automático
                    if GODmod:
                        print("GOD mode activado. Presiona 9 de nuevo para desactivarlo.")
                    else:
                        print("GOD mode desactivado.")
        pygame.display.flip() #Sirve para actualizar la pantalla
    pygame.quit()  #Función para abandonar el juego

if __name__ == "__main__":
    main()
