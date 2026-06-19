import time #para eso de que los intercambios varien en tiempo y asi
import random #para mezclar las cartas
print("Adivina en donde está la reina de corazones!")
opciones = str(input("Para jugar escriba [J], para ver la tabla de posiciones escriba [P], para salir escriba [S]: "))
opciones = opciones.lower()
puntos = 0
#las cartas antes estaban asi definidas con variables y multilinea pero no daba pa ponelas una al lado de la otra entonces este es el formato nuevo jiji
carta1 = [" ___ ", "|J  |", "| ♦ |", "|__J|"]
carta2 = [" ___ ", "|8  |", "| ♣ |", "|__8|"]
carta3 = [" ___ ", "|Q  |", "| ♥ |", "|__Q|"] #reina de corazones
carta4 = [" ___ ", "|A  |", "| ♣ |", "|__A|"]
carta5 = [" ___ ", "|K  |", "| ♣ |", "|__K|"]
carta6 = [" ___ ", "|A  |", "| ♦ |", "|__A|"]
carta7 = [" ___ ", "|A  |", "| ♠ |", "|__A|"]
carta8 = [" ___ ", "|3  |", "| ♠ |", "|__3|"]
carta9 = [" ___ ", "|6  |", "| ♠ |", "|__6|"]
carta10 = [" ___ ", "|9  |", "| ♣ |", "|__9|"]

baraja = [carta1, carta2, carta4, carta5, carta6, carta7, carta8, carta9, carta10]

cartainv1 = [" ___ ", "|   |", "|   |", "|___|"]
cartainv2 = [" ___ ", "|   |", "|   |", "|___|"]
cartainv3 = [" ___ ", "|   |", "|   |", "|___|"]

cartasinv = [cartainv1, cartainv2, cartainv3]

def partida(): #funcion para que salgan 2 cartas aleatorias y la reina de corazones (en posiciones aleatorias tmb)
    c1 = random.choice(baraja) #sacan una carta aleatoria de baraja
    c2 = random.choice(baraja)
    juego = random.sample([c1, c2, carta3], 3) #aqui con esas 2 cartas las junta con la reina pa que salga la partida ahora si
    return juego
def fila(listacartas): #funcion para que las cartas no se vean asi feas en una lista y que se pongan una al lado de la otra
    for i in range(4): #elciclo hace que como las cartas tienen 4 partes, se junten en una sola carta
        print(f"{listacartas[0][i]}   {listacartas[1][i]}   {listacartas[2][i]}") #esto es que las cartas se vayan armando (i es la parte de la carta y el numero es la carta en si, osea si i es 0 es el techo y asi)
def filainv(listacartasinv): 
    for i in range(4): 
        print(f"{listacartasinv[0][i]}   {listacartasinv[1][i]}   {listacartasinv[2][i]}")
#---------------------- funcionamiento del juego desde aqui
nombre = str(input("Por favor escriba su nombre: "))
while opciones != "s":
    if opciones == "j":
        print(f"Hola {nombre}, ¿estás listo/a?")
        juego = partida()
        fila(juego) #aqui imprime las cartas en fila
        print("Iniciando la partida, recuerda izquierda[I], centro[C], derecha[D]")
        time.sleep(3)

        numeros = [5, 6, 7, 8, 9, 10, 11]
        for i in range(random.choice(numeros)):
            posicion = random.randint(0, 5)
            if posicion == 0:
                time.sleep(2)
                postemp = juego[0]#postemp es posicion temporal, esto es un cambio de variable para que las cartas se muevan
                juego[0] = juego[1]
                juego[1] = postemp
                print("Intercambiando izquierda con centro")
            elif posicion == 1:
                time.sleep(2.5)
                postemp = juego[1]
                juego[1] = juego[2]
                juego[2] = postemp
                print("intercambiando Centro con Derecha")
            elif posicion == 2:
                time.sleep(3)
                postemp = juego[0]
                juego[0] = juego[2]
                juego[2] = postemp
                print("intercambiando Derecha con Izquierda")
            elif posicion == 3:
                time.sleep(1.5)
                postemp = juego[1]
                juego[1] = juego[0]
                juego[0] = postemp
                print("Intercambiando Centro con Izquierda")
            elif posicion == 4:
                time.sleep(1)
                postemp = juego[2]
                juego[2] = juego[1]
                juego[1] = postemp
                print("intercambiando Derecha con Centro")
            elif posicion == 5:
                time.sleep(1.7)
                postemp = juego[2]
                juego[2] = juego[0]
                juego[0] = postemp
                print("intercambiando Izquierda con Derecha")
        time.sleep(2)
        filainv(cartasinv) #aqui imprime las cartas invertidas en fila
        posicioncor = juego.index(carta3)
        if posicioncor == 0:
            posicioncor = "I"
        elif posicioncor == 1:
            posicioncor = "C"
        elif posicioncor == 2:
            posicioncor = "D"
        posicioncor = posicioncor.lower()

        #ya aqui es si el jugador gana o pierde
        posicionjug = str(input("número de posición de la reina de corazones, izquierda[I], centro[C], derecha [D]: ")) #posición que dijo el jugador
        posicionjug.lower()
        if posicionjug == posicioncor:
            puntos = puntos + 1
            print("Ganaste! las posiciones eran")
            fila(juego) 
            volver = str(input("Quieres volver a jugar? escribe [J] para seguir, [P] para ver la tabla de posiciones,[N] para salir: "))
            voler = volver.lower()
            if volver == "j":
                opciones = "j"
            elif volver == "p":
                opciones = "p"
            elif volver == "n":
                break

        elif posicionjug != posicioncor:
            print("Perdiste :(, las posiciones eran")
            fila(juego) 
            volver = str(input("Quieres volver a jugar? escribe [J] para seguir, [P] para ver la tabla de posiciones,[N] para salir: "))
            volver = volver.lower()
            if volver == "j":
                opciones = "j"
            elif volver == "p":
                opciones = "p"
            elif volver == "n":
                break

            else:
                break
        else:
            volver = str(input("Upsi, opciones no encontrada, escribe [J] para seguir, [P] para ver la tabla de posiciones,[N] para salir: "))
            voler = volver.lower()
            if volver == "j":
                opciones = "j"
            elif volver == "p":
                opciones = "p"
            elif volver == "n":
                break
            else:
                break
                
    elif opciones == "p": #PENDIENTE HACER ESO DE QUE GUARDE LA FECHA Y HORA DE LA MEJOR PARTIDA
        print(f"Jugador: {nombre}, puntos: {puntos}")
        volver = str(input("Quieres volver a jugar? escribe [J] para seguir, [P] para ver la tabla de posiciones,[N] para salir: "))
        voler = volver.lower()
        if volver == "j":
            opciones = "j"
        elif volver == "p":
            opciones = "p"
        elif volver == "n":
            print("Adios!")
            break
            
    elif opciones == "s":
        print("Adios!")
        break
        
        
    else:
        print("Opción no encontrada :(")
        opciones = "s" 
