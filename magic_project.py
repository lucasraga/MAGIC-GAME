''' Juego MAGIC-GAME THE GATHERING PROJECT.
Propiedad intelectual de David y Lucas.
Todos los derechos reservados.
'''
#Abrimos y leemos la base de datos
magicbd = open("D:\LUCAS\DAW\Programación\python\proyectos\magic-game/BD_magic_cartas.txt")
mensaje = magicbd.read()
#Printeamos la base de datos y posteriormente la cerramos.
print(mensaje)
magicbd.close()
'''
La idea es utilizarlo para pedirle al usuario que elija la carta que desea utilizar contra otra. Podemos empezar con eso he ir avanzando desde ahí.
'''
