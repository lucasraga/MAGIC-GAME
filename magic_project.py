''' Juego MAGIC-GAME THE GATHERING PROJECT.
Propiedad intelectual de David y Lucas.
Todos los derechos reservados.
'''
#imports
import random
#Abrimos y leemos la base de datos de un txt
magicbd = open("D:\LUCAS\DAW\Programación\python\proyectos\magic-game/BD_magic_cartas.txt")
mensaje = {magicbd.read()}
#Printeamos la base de datos y posteriormente la cerramos.
print(mensaje)
magicbd.close()
'''
La idea es utilizarlo para pedirle al usuario que elija la carta que desea utilizar contra otra. Podemos empezar con eso he ir avanzando desde ahí.
'''
'''
def Play_Start():
def Finish_Play():
def Comp_Winner():
def update_board():
    print("               ",jugador1)
    print("+------"*3, end="+")
    print()
    print("|           ","[MAZO]  |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("| [MAZO]""             |")
    print("+------"*3, end="+")
    print()
    print("",jugador2)
def Players():
'''
#Función que dibuja el tablero
def draw_board():
    print("               ",jugador1)
    print("+------"*3, end="+")
    print()
    print("|           ","[MAZO]  |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("| [MAZO]""             |")
    print("+------"*3, end="+")
    print()
    print("",jugador2)


#Inicio de juego, explicación de reglas e inscripción de jugadores.
print("Vas a jugar al juego Magic The Gathering. ¡Preparate para vencer o ser vencido!", sep="\n")
reglas = input("¿Necesitas que te explique las reglas? S/N: ")
if reglas == "S":
    juego = open("D:\LUCAS\DAW\Programación\python\proyectos\magic-game/BD_reglas_magic.txt", encoding="utf-8")
    leer_juego = juego.read()
    print(leer_juego, end="\n")
jugador1 = input("Jugador 1, escribe tu Username para la partida: ")
print()
jugador2 = input("Jugador 2, escribe tu Username para la partida: ")
#inicializamos los dos mazos de los jugadores
Mazo_jugador1 = {}
Mazo_jugador2 = {}
#Agregamos las manos iniciales de los jugadores con un bucle de 7 aleatorio de los diccionarios que contendrán las cartas de los mazos.
manojugador1 = {}
manojugador2 = {}
for mano in range(8):
   manojugador1.append(Mazo_jugador1[random.randint(1,100)])
   manojugador2.append(Mazo_jugador2[random.randint(1,100)])
''' Idea: Conforme juegue la mano el jugador, podemos ir eliminando las cartas del mazo e ir cambiando las de la mano. Actualizando el tablero a su vez.'''
draw_board()
