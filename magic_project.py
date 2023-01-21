''' Juego MAGIC-GAME THE GATHERING PROJECT.
Propiedad intelectual de David y Lucas.
Todos los derechos reservados.
'''
#imports
import random
#Abrimos y leemos la base de datos de un txt
magicbd = open("D:\LUCAS\DAW\Programación\python\proyectos\magic-game/BD_magic_cartas.txt")
mensaje = {magicbd.read()}
for mensaje in magicbd:
    mensaje = magicbd.readlines()
#Printeamos la base de datos y posteriormente la cerramos.
magicbd.close()
'''
La idea es utilizarlo para pedirle al usuario que elija la carta que desea utilizar contra otra. Podemos empezar con eso he ir avanzando desde ahí.
'''
'''
def Play_Start():
def Finish_Play():
def Comp_Winner():
def Shiftplayer1():
def Shiftplayer2():
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
#Mulligan
def Mulligan(MulliganJ1, MulliganJ2):
    while True:
        if MulliganJ1 == "S":
            for mano in range(len(manojugador1)):
                manojugador1.append(Mazo_jugador1[random.randint(1,100)])
                manojugador1.pop(input("Elige la carta que desees eliminar: "))
        if MulliganJ2 == "S":
            for mano in range(len(manojugador2)):
                manojugador2.append(Mazo_jugador1[random.randint(1,100)])
                manojugador2.pop(input("Elige la carta que desees eliminar: "))
        else:
            print("Continuamos...")
#Inicio de juego, explicación de reglas e inscripción de jugadores.
print("Vas a jugar al juego Magic The Gathering. ¡Preparate para vencer o ser vencido!", sep="\n")
reglas = input("¿Necesitas que te explique las reglas? S/N: ")
reglas = reglas.upper()
if reglas == "S":
    juego = open("D:\LUCAS\DAW\Programación\python\proyectos\magic-game/BD_reglas_magic.txt", encoding="utf-8")
    leer_juego = juego.read()
    print(leer_juego, end="\n")
jugador1 = input("Jugador 1, escribe tu Username para la partida: ")
print()
jugador2 = input("Jugador 2, escribe tu Username para la partida: ")
#inicializamos los dos mazos de los jugadores puestos en una base de datos y los obtenemos en formato diccionario. 
with open('mazoj1.txt', 'r') as archivo:
    separador = ':'
    Mazo_jugador1= {}
    for linea in archivo:
        key, value = linea.split(separador)
        Mazo_jugador1[key.strip()] = value.strip()
with open('mazoj2.txt', 'r') as archivo:
    separador = ':'
    Mazo_jugador2= {}
    for linea in archivo:
        key, value = linea.split(separador)
        Mazo_jugador2[key.strip()] = value.strip()
#Agregamos las manos iniciales de los jugadores con un bucle de 7 aleatorio de los diccionarios que contendrán las cartas de los mazos.
manojugador1 = []
manojugador2 = []
for mano in range(7):
    manojugador1.append(random.choice(list(Mazo_jugador1.values())))
    manojugador2.append(random.choice(list(Mazo_jugador1.values())))
#print de la mano inicial
print("Mano de ",jugador1," : ",manojugador1, end="\n")
print("Mano de ",jugador2," : ",manojugador2, end="\n")
#Mulligan de la mano inicial de cada Jugador
MulliganJ1 = input("jugador 1, ¿Deseas hacer mulligan o continuas con tu mano inicial?: S/N")
MulliganJ1 = MulliganJ1.upper()
print()
MulliganJ2 = input("jugador 2, ¿Deseas hacer mulligan o continuas con tu mano inicial?: S/N")
MulliganJ2 = MulliganJ1.upper()
''' Idea: Conforme juegue la mano el jugador, podemos ir eliminando las cartas del mazo e ir cambiando las de la mano. Actualizando el tablero a su vez.'''
draw_board()
