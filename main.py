from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from lista_nombres import ListaNombres
from jugador import Jugador
import random


def generar_digipymon_aleatorio():
    lista_nombres1 = ListaNombres()
    tipos = ["fuego", "agua", "planta"]
    nombre = lista_nombres1.obtener_nombre_digipymon()
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    tipo = random.choice(tipos)
    nivel = random.randint(1, 3)
    digipymon1 = Digipymon(nombre, vida, ataque, tipo, nivel)
    return digipymon1

def menu():
    print("Elige una opcion")
    print("1. Buscar Digipymon") 
    print("2. Luchar contra un entrenador")
    print("3. Ir a la teinda")
    print("4. Usar objeto")
    print("5. Consultar inventario")
    print("6. Consultar Digipymons")
    print("7. Salir")
    respuesta = input("")
    return respuesta
    
def buscar_digipymon(jugador, inventario):
    digipymon_encontrado = generar_digipymon_aleatorio()
    probabilidad_captura = 100 - (digipymon_encontrado.nivel *10)
    salirBucle = True
    while(salirBucle):
        print("Has encontrado un...")
        print(digipymon_encontrado)
        print("La probabilidad de captura al " + digipymon_encontrado.nombre + " es de un " + str(probabilidad_captura) + "%")
        print("¿Deseas capturar al digipymon?")
        print("1. Sí")
        print("2. No")
        opcion = input()
        if opcion == "1":
            if "Digipyball" in inventario.objetos and jugador.cantidad_digipymon < 6:
                inventario.usar_objeto("Digipyball")

                if random.randint(1, 100) < probabilidad_captura:
                    print("Has capturado un nuevo digipymon!!" + digipymon_encontrado.nombre)
                    jugador.lista_digipymon.append(digipymon_encontrado)                    
                    salirBucle = False

                else:
                    print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                    salirBucle = False    

            elif "Digipyball" not in inventario.objetos:
                print("No te quedan digipyballs")
                print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                salirBucle = False

            elif jugador.cantidad_digipymon == 6:
                print("Ya tienes 6 digipymons, no puedes capturar más")
                print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                salirBucle = False

        elif opcion == "2":
            print("Has huido")
            salirBucle = False
        else:
            print("Introduce una opción correcta")            

def combate(lista_nombres, enemigo, jugador):
    bucleCombate = True
    for i in range(0, jugador.cantidad_digipymon ):
        enemigo.añadir_digipymon(lista_nombres.obtener_nombre_digipymon)

    while(bucleCombate):
        print("Te has encontrado con " + enemigo.nombre + " y te reta a un combate!")
        print("¿Quieres luchar?")
        print("1. Sí")
        print("2. No")
        opcion = input()
        if (opcion == "1"):
            victorias = 0    
            derrotas = 0
            for i in range (jugador.cantidad_digipymons):
                digipymonJugador = jugador.lista_digypimons[i].nombre
                digipymonEnemigo = enemigo.lista_digypimons[i].nombre
                ataqueEnemigo = enemigo.lista_digipymons[i].ataque
                ataqueJugador = jugador.lista_digipymons[i].ataque

                print("Tu " + digipymonJugador)
                print("Se enfrenta a...")
                print(digipymonEnemigo)
                
                if (ataqueJugador > ataqueEnemigo):
                    perdidaVida = ataqueJugador - ataqueEnemigo
                    jugador.lista_digipymons[i].vida = jugador.lista_digipymons[i].vida - perdidaVida
                    victorias = victorias + 1
                    print("Tu " + digipymonJugador + "ha vencido")
                    print("Ha perdido " + perdidaVida + " puntos de vida")
                    print("Sus puntos de vida restantes son: " + jugador.lista_digipymons[i].vida)


        elif(opcion == "2"):
            print("Has huído, se te cae un digicoin al salir corriendo")
            print("Te quedan " + jugador.consultar_digicoins) 


def digishop(jugador, inventario):
    print("|-----Catalogo de Digishop-----|")
    print("A. Digipyballs --> 5 digicoins c/u")
    print("B. Pocion curativa (Restaura 10p de salud) --> 3 Digicoins c/u")
    print("C. Anabolizantes (Aumenta el ataque en 5p) --> 4 Digicoins c/u")
    print("¿Qué desea comprar?")
    opcion_compra = input()
    if opcion_compra == "A":
        jugador.digipoints >= 5
        print("Has comprado una digipyball")
        jugador.digipoints = jugador.digipoints - 5
        inventario.añadir_objeto("Digipyball", 1)
    elif opcion_compra == "B":
        jugador.digipoints >= 3
        print("Has comprado una pocion")
        jugador.digipoints = jugador.digipoints - 3
        inventario.añadir_objeto("Pocion", 1)
    elif opcion_compra == "C":
        jugador.digipoints >= 4
        print("Has comprado un anabolizante")
        jugador.digipoints = jugador.digipoints - 5
        inventario.añadir_objeto("Anabolizante", 1)
    else:
        print("No tienes fondos suficientes o no es la opcion correcta")
        
def usar_item(jugador, inventario):
    print("¿Sobre que digipymon quieres utilizar tu objeto?")
    jugador.consultar_digipymon()
    seleccion = input()
    jugador.lista_digipymon[seleccion]

    print(inventario()) 
    print("¿Que objeto quieres usar?")
    objeto = (input(""))
    if objeto == "digipyball":
        print("Este objeto no puede ser utilizado en tu digipymon")
    elif objeto == "pocion":
        jugador.lista_digipymon[seleccion].vida = jugador.lista_digipymon[seleccion].vida + 5
        inventario.usar_objeto("Pocion")
        print("La vida de")
    elif objeto == "anabolizante":
        jugador.lista_digipymon[seleccion].ataque = jugador.lista_digipymon[seleccion].ataque + 3
        inventario.usar_objeto("Anabolizante")
        print("")
              
                              
    
def main(): 
    """ bucle = True
    while bucle:
     jugador1 = Jugador("Pepe")

    
    respuesta = menu()
    if respuesta == "1":

    elif respuesta == "7":
    bucle = False"""
    jugador1 = Jugador("Pepe")
    inventario1 = Inventario()
    lista_nombres1 = ListaNombres() 
    enemigo1 = Enemigo(lista_nombres1.obtener_nombre_entrenador())
    inventario1.añadir_objeto("Digipyball", 2)   
    buscar_digipymon(jugador1, inventario1)
main()

    
   
