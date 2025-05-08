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
        print("1. Buscar Digipymon") 
        print("2. Luchar contra un entrenador")
        print("3. Ir a la teinda")
        print("4. Usar objeto")
        print("5. Consultar inventario")
        print("6. Consultar Digipymons")
        print("7. Salir")

    bucle = True
    while bucle:
        menu()
        respuesta = input()
    bucle = False
main()
