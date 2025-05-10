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
    respuesta = 0
    respuesta = input("")
    return respuesta
    
def buscar_digipymon(jugador, inventario):
    digipymon_encontrado = generar_digipymon_aleatorio()
    probabilidad_captura = 100 - (digipymon_encontrado.nivel *10)
    
    print("Has encontrado un...")
    print(digipymon_encontrado)
    print("La probabilidad de captura al " + digipymon_encontrado.nombre + " es de un " + str(probabilidad_captura) + "%")
    print("¿Deseas capturar al digipymon?")
    print("1. Sí")
    print("2. No")
    opcion = input()
    if opcion == "1":
        if "digipyballs" in inventario.objetos and jugador.cantidad_digipymons < 6:
            inventario.usar_objeto("digypiballs")

            if random.randint(1, 100) < probabilidad_captura:
                print("Has capturado un nuevo digipymon!!")
                jugador.listadigypimon.append(digipymon_encontrado)
            else:
                print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")    

        elif "digipyballs" not in inventario.objetos:
            print("No te quedan digipyballs")
        elif jugador.cantidad_digipymons == 6:
            print("Ya tienes 6 digipymons, no puedes capturar más")

    elif opcion == "2":
        print("Has huido")
    else:
        print("Introduce una opción correcta")            


    
def main(): 
   """ bucle = True
    while bucle:
     jugador1 = Jugador("Pepe")

    
    respuesta = menu()
    if respuesta == "1":

    elif respuesta == "7":
        bucle = False"""

    
main()

    
