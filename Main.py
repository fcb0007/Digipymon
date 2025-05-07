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
    
    def menu():
        print("1. Buscar Digipymon")
        print("2. Luchar contra un entrenador")
        print("3. Ir a la tienda")
        print("4. Usar objetos")
        print("5. Consultar inventario")
        print("6. Consultar digipymons")
        print("7. Salir")
        opcion = 0
        opcion = int(input(""))
        return opcion
    
    def buscar_digipymon():
        digipymon_encontrado = generar_digipymon_aleatorio()
        probabilidad_captura = 100 - (digipymon_encontrado.nivel * 10)
        print("Has encontrado un...")
        print(digipymon_encontrado)
        print("La probabilidad de capturar al " + digipymon_encontrado.nombre + " es de un " + str(probabilidad_captura) + "%")
        
        
        
    buscar_digipymon()     
main()

    