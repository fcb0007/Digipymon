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
        print(nombre)  
    generar_digipymon_aleatorio()   
main()
    