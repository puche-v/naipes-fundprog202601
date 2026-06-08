import time
import random
print("Adivina en donde está la reina de corazones!")
opciones = str(input("Para jugar escriba [J], para ver la tabla de posiciones escriba [P], para salir escriba [S]: "))
opciones = opciones.lower()
puntos = 0
carta1 = """
 ___
|J  |
| ♦ |
|__J|
"""
carta2 = """
 ___
|8  | 
| ♣ |
|__8|
"""
carta3 = """
 ___
|Q  | 
| ♥ | 
|__Q|
""" #reina de corazones
carta4 = """
 ___
|A  | 
| ♣ | 
|__A|
"""
carta5 = """
 ___
|K  | 
| ♣ | 
|__K|
"""
carta6 = """
 ___
|A  | 
| ♦ |
|__A|
"""
carta7 = """
 ___
|A  | 
| ♠ |
|__A|
"""
carta8 = """
 ___
|Q  | 
| ♠ |
|__Q|
"""
carta9 = """
 ___
|6  | 
| ♠ |
|__6|
"""
carta10 = """
 ___
|3  | 
| ♣ | 
|__3|
"""
baraja = [carta1, carta2, carta3, carta4, carta5, carta6, carta7, carta8, carta9, carta10]
partida = random.sample(baraja, 3)
#print(*partida) #intento de hacer partidas aleatorias con random (para despues jiji)
cartainv = """
 ___
|   |
|   |
|___|
"""
if opciones == "j":
    nombre = str(input("Por favor escriba su nombre: "))
    while puntos == 0:
        print(f"Hola {nombre}, ¿estás listo/a?")
        print("posición 1: ", carta1 , "posición 2: ", carta2, "posición 3", carta3)
        print("Iniciando la partida")
        time.sleep(3)
        print("revolviendo...")
        time.sleep(3)
        print("revolviendo...")
        time.sleep(3)
        print("revolviendo...")
        time.sleep(1)
        print("En que posición crees que esta la carta?")
        posicioncor = 3 #posición de la reina de corazones
        print("posicion 1: ", cartainv , "posición 2: ", cartainv, "posición 3", cartainv)
        posicionjug = int(input("número de posición de la reina de corazones: ")) #posición que dijo el jugador
        if posicionjug == posicioncor:
            puntos = puntos + 1
            print("Ganaste! las posiciones eran")
            print("posición 1: ", carta2 , "posición 2: ", carta1, "posición 3", carta3)
            volver = str(input("Quieres volver a jugar? escribe [S] para seguir, [N] para salir: "))
            voler = volver.lower()
            if volver == "s":
                puntos = 0
            elif volver == "n":
                break
        elif posicionjug != posicioncor:
            print("Perdiste :(, las posiciones eran")
            print("posición 1: ", carta2 , "posición 2: ", carta1, "posición 3", carta3)
            volver = str(input("¿Quieres intentarlo de nuevo? Escribe [S] para seguir, [N] para salir: "))
            volver = volver.lower()
            if volver == "s":
                puntos = 0
            elif volver == "n":
                break
            else:
                break
        else:
            volver = str(input("Opción invalida :(, ¿quieres volver a jugar? escribe [S] para seguir, [N] para salir: "))
            voler = volver.lower()
            if volver == "s":
                puntos = 0
            elif volver == "n":
                break
            else:
                break
            
elif opciones == "p":
    print("La tabla de posiciones no está disponible por el momento :c")
elif opciones == "s":
    print("Adios!")
    
else:
    print("Opción no encontrada :(")
    
