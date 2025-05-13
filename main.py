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
print(generar_digipymon_aleatorio())

def menu():
    print("Elige una opcion")
    print("1. Buscar Digipymon") 
    print("2. Luchar contra un entrenador")
    print("3. Ir a la teinda")
    print("4. Usar objeto")
    print("5. Consultar inventario")
    print("6. Consultar Digipymons")
    print("7. Salir")
    respuesta = 0
    respuesta = (input(""))
    return respuesta

def buscar_digipymon():
    digipymon_encontrado = generar_digipymon_aleatorio()
    probabilidad_captura = 100 - (digipymon_encontrado.nivel *10)
    print("Has encontrado un...")
    print(digipymon_encontrado)
    print("La probabilidad de captura al " + digipymon_encontrado.nombre + " en de un " + str(probabilidad_captura) + "%")

def digishop(jugador, inventario):
    print("|-----Catalogo de Digishop-----|")
    print("A. Digipyballs --> 5 digicoins c/u")
    print("B. Pocion curativa (Restaura 10p de salud) --> 3 Digiicoins c/u")
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
    """bucle = True
    while bucle:
        menu()
        respuesta = input()
    if respuesta == "1":
        buscar_digipymon()
    elif respuesta =="3":
        digishop()
    elif respuesta == "7":
        bucle = False"""
main()
