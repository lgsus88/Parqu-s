import pygame 

#Función para obtener una casilla de acuerdo a sus coordenadas
def Ccasilla(tablero, coordenadas):
    for clave, casilla in tablero.items():
        if (casilla["x"], casilla["y"]) == coordenadas:
            return clave
    return None

#Se crea una clase para definir todas las características y funciones que tendrán las fichas
class Ficha:
    def __init__(self, color, posicion_inicial):
        self.color = color
        self.posicion = posicion_inicial 
        self.en_prision = True  #Todas las fichas comienzan en prisión
        self.en_meta = False  #Indica si la ficha ha llegado a la meta

#También creamos una clase para definir las características y funciones de los jugadores
class Jugador:
    def __init__(self, nombre, color, posicion_inicial):
        self.nombre = nombre
        self.color = color
        self.fichas = [Ficha(color, posicion_inicial) for _ in range(4)]  #Esto sirve para crear 4 fichas por jugador
        self.casilla_inicial = posicion_inicial  #Aquí se guarda la posición inicial para reiniciar fichas

    #Función para dibujar las fichas
    def dibujar_fichas(self, ventana):
        for i, ficha in enumerate(self.fichas):
            if ficha.posicion is not None:
                x, y = ficha.posicion
                #Aplicamos un desplazamiento a cada ficha para evitar superposiciones
                offset_x = (i % 2) * 20  
                offset_y = (i // 2) * 20 
                #Dibujamos un borde negro para las fichas
                pygame.draw.circle(ventana, (0, 0, 0), (int(x + offset_x), int(y + offset_y)), 17)  
                #Dibujamos la ficha
                pygame.draw.circle(ventana, self.color, (int(x + offset_x), int(y + offset_y)), 15)  

    #Función para que las fichas cambien de casilla
    def mover_ficha(self, pasos, tablero, jugadores):
        #Aquí se verifica si el jugador tiene fichas en prisión y si el valor del dado es 5
        if any(ficha.en_prision for ficha in self.fichas) and (pasos == 5):
            for ficha in self.fichas:
                if ficha.en_prision:
                    ficha.en_prision = False
                    ficha.posicion = self.casilla_inicial  #Se pone la ficha en la posición inicial
                    return True  #Se saca una ficha de prisión
        else:
            #Sirve para mover una ficha si no hay fichas en prisión o no se obtuvo un 5 para sacar una ficha de
            #prisión
            for ficha in self.fichas:
                if not ficha.en_prision:
                    nueva_posicion = self.calcular_nueva_posicion(ficha, pasos, tablero)
                    if nueva_posicion is not None and not self.verificar_colision(nueva_posicion, jugadores):
                        ficha.posicion = nueva_posicion
                        return True  
        return False  #Solo si no se pudo mover ninguna ficha

    #Sirve para calcular la nueva posición
    def calcular_nueva_posicion(self, ficha, pasos, tablero):
        pos_actual = ficha.posicion
        casilla_actual = Ccasilla(tablero, pos_actual)
        if casilla_actual is None:
            return None  # La ficha no está en una casilla válida
        #Sirve para hacer avanzar las fichas
        for _ in range(pasos):
            siguiente = tablero[casilla_actual]["siguiente"]
            if siguiente is None:
                return None  #Solo si no hay más casillas
            casilla_actual = siguiente
        return (tablero[casilla_actual]["x"], tablero[casilla_actual]["y"])

    def verificar_colision(self, nueva_posicion, jugadores):
        for jugador in jugadores.values():
            for ficha in jugador.fichas:
                if ficha.posicion == nueva_posicion:
                    return True
        return False

    #Sirve para sacar a las fichas de prisión
    def offprison(self, tablero):
        #Se busca la casilla inicial en el tablero
        casilla_inicial_clave = Ccasilla(tablero, self.casilla_inicial)
        if casilla_inicial_clave is None:
            print("Error: No se encontró la casilla inicial en el tablero.")
            return False
        
        for ficha in self.fichas:
            if ficha.en_prision:
                ficha.en_prision = False
                #Se mueve la ficha a la siguiente casilla
                siguiente_casilla_clave = tablero[casilla_inicial_clave]["siguiente"]
                if siguiente_casilla_clave is not None:
                    ficha.posicion = (tablero[siguiente_casilla_clave]["x"], tablero[siguiente_casilla_clave]["y"])
                    return True
                else:
                    print("Error: No hay una casilla siguiente para mover la ficha.")
                    return False
        return False

    #Sirve para calcular si el jugador tiene alguna ficha disponible para mover
    def fichas_disponibles_para_mover(self, pasos, tablero, jugadores):
        #Creamos una lista vacía para luego agregar las fichas disponibles
        fichas_disponibles = []
        for ficha in self.fichas:
            #Indica que solo podemos sacar una ficha de prisión con un 5
            if ficha.en_prision:
                if pasos == 5:  
                    fichas_disponibles.append(ficha)
            else:
                nueva_posicion = self.calcular_nueva_posicion(ficha, pasos, tablero)
                #Si la nueva posición no es None (indicando que no hay más casillas para avanzar para ese jugador)
                #la ficha se agrega a la lista de fichas disponibles
                if nueva_posicion is not None and not self.verificar_colision(nueva_posicion, jugadores):
                    fichas_disponibles.append(ficha)
        return fichas_disponibles

    #Sirve para seleccionar la ficha que el jugador quiere mover
    def seleccionar_ficha(self, pasos, tablero, jugadores):
        #Solo se puede seleccionar una ficha que se pueda mover
        fichas_disponibles = self.fichas_disponibles_para_mover(pasos, tablero, jugadores)
        #Si no tiene fichas para mover, se pasa el turno
        if not fichas_disponibles:
            print("No tienes fichas disponibles para mover. Turno perdido.")
            return False
        
        if len(fichas_disponibles) == 1:
            #Si solo se puede mover una ficha, se moverá automáticamente
            ficha = fichas_disponibles[0]
            if ficha.en_prision:
                self.offprison(tablero)
                print(f"Ficha {self.fichas.index(ficha) + 1} ha salido de prisión.")
            else:
                nueva_posicion = self.calcular_nueva_posicion(ficha, pasos, tablero)
                ficha.posicion = nueva_posicion
                print(f"Ficha {self.fichas.index(ficha) + 1} se ha movido a la casilla {nueva_posicion}.")
            return True
        
        #Mostramos las opciones si hay más de una ficha disponible
        print(f"Turno de {self.nombre}. Elige una ficha para mover:")
        for i, ficha in enumerate(fichas_disponibles):
            estado = "En prisión" if ficha.en_prision else f"En casilla {ficha.posicion}"
            print(f"{i + 1}. Ficha {self.fichas.index(ficha) + 1} ({estado})")
        
        #Implementamos un try en caso de que se seleccione una cosa diferente o se haga algo distinto
        try:
            eleccion = int(input("Selecciona el número de la ficha: ")) - 1
            if 0 <= eleccion < len(fichas_disponibles):
                ficha = fichas_disponibles[eleccion]
                if ficha.en_prision:
                    self.offprison(tablero)
                    print(f"Ficha {self.fichas.index(ficha) + 1} ha salido de prisión.")
                else:
                    nueva_posicion = self.calcular_nueva_posicion(ficha, pasos, tablero)
                    ficha.posicion = nueva_posicion
                    print(f"Ficha {self.fichas.index(ficha) + 1} se ha movido a la casilla {nueva_posicion}.")
                return True
            else:
                print("Selección no válida.")
                return False
        except ValueError:
            print("Entrada no válida. Introduce un número.")
            return False