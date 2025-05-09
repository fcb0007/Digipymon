from Digipymon import Digipymon
from Enemigo import Enemigo
from Inventario import Inventario
from ListaNombres import ListaNombres
import random
def main ():
    lista_nombres1 = ListaNombres() 
    def generar_digipymon_aleatorio():
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
        respuesta = int(input(""))
        return respuesta
    
    def buscar_digipymon():
        digipymon_encontrado = generar_digipymon_aleatorio()
        probabilidad_captura = 100 - (digipymon_encontrado.nivel *10)
        print("Has encontrado un...")
        print(digipymon_encontrado)
        print("La probabilidad de captura al " + digipymon_encontrado.nombre + " en de un " + str(probabilidad_captura) + "%")
    
    bucle = True
    while bucle:
        menu()
        respuesta = input()
    if respuesta == "1":
        buscar_digipymon()
    elif respuesta == "7":
        bucle = False

    
main()
