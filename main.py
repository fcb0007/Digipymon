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
    print("")
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
                    print("Has capturado un " + digipymon_encontrado.nombre + "!!")
                    jugador.lista_digipymon.append(digipymon_encontrado)
                    print(f"Te quedan {inventario.objetos["Digipyball"]} digipyballs")                    
                    salirBucle = False

                else:
                    print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                    print(f"Te quedan {inventario.objetos["Digipyball"]} digipyballs")
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

def combate(jugador: Jugador):    
    lista_nombres = ListaNombres()
    enemigo = Enemigo(lista_nombres.obtener_nombre_entrenador())
    bucleCombate = True
    for i in range(0, jugador.cantidad_digipymon ):
        enemigo.añadir_digipymon(lista_nombres.obtener_nombre_digipymon)

    while(bucleCombate):
        print("Te has encontrado con " + enemigo.nombre + " y te reta a un combate!")
        print("¿Quieres luchar?")
        print("1. Sí")
        print("2. No")
        opcion = input()
        if opcion == "1":
            victorias = 0    
            derrotas = 0
            for i in range (jugador.cantidad_digipymons):
                digipymon_jugador = jugador.lista_digypimons[i].nombre
                digipymon_enemigo = enemigo.lista_digypimons[i].nombre
                ataque_enemigo = enemigo.lista_digipymons[i].ataque
                ataque_jugador = jugador.lista_digipymons[i].ataque

                print("Tu " + digipymon_jugador)
                print("Se enfrenta a...")
                print(digipymon_enemigo)
                if jugador.lista_digipymon[i].vida <= 0:
                    print(f"Has perdido, tu digipymon {jugador.lista_digipymon[i].nombre}, tiene {jugador.lista_digipymon[i].vida} de vida")
                    derrotas += 1

                elif ataque_jugador > ataque_enemigo:
                    victorias += 1
                    jugador.lista_digipymon[i].vida = jugador.lista_digipymon[i].vida - ataque_enemigo
                    print("Tu " + digipymon_jugador + "ha vencido")
                    print("Ha perdido " + ataque_enemigo + " puntos de vida")
                    print("Sus puntos de vida restantes son: " + jugador.lista_digipymon[i].vida)
                    print("Llevas " + str(victorias) + " victorias y " + str(derrotas) + " derrotas")

                elif ataque_enemigo > ataque_jugador:
                    derrotas += 1
                    perdida_vida = ataque_jugador - ataque_enemigo
                    jugador.lista_digipymon[i].vida -= perdida_vida
                    if jugador.lista_digipymon[i].vida < 0:
                        jugador.lista_digipymon[i].vida = 0
                    print(f"Has perdido el combate, tu digipymon ha perdido {perdida_vida}, puntos de vida")
                    print(f"Su salud restante es de {jugador.lista_digipymon[i].vida}")

                elif ataque_enemigo == ataque_jugador:
                    daño_aleatorio = random.randint(1,5)
                    print(f"Has empatado, en el combate tu digipymon ha sufrido un daño de {daño_aleatorio}")
                    jugador.lista_digipymon[i].vida -= daño_aleatorio
                    if jugador.lista_digipymon[i].vida < 0:
                        jugador.lista_digipymon[i].vida = 0
                    print(f"Su salud restante es: {jugador.lista_digipymon[i].vida}")

            if victorias > derrotas:
                jugador.digicoins += victorias
                print(f"Has ganado! Tus victorias han sido: {victorias} y tus derrotas: {derrotas}")
                print(f"Ganas {victorias} digicoins, tus digicoins totales son {jugador.digicoins}")

            elif derrotas > victorias:
                jugador.digicoins -= derrotas

                if jugador.digicoins < 0:
                    jugador.digicoins = 0
                print(f"Has perdido! Tus victorias han sido: {victorias} y tus derrotas: {derrotas}")
                print(f"Pierdes {derrotas} digicoins, tus digicoins totales son {jugador.digicoins}")

            elif victorias == derrotas:
                print(f"Ha habido un empate, Tus victorias han sido: {victorias} y tus derrotas: {derrotas}")        

        elif opcion == "2":
            jugador.digicoins -= 1

            if jugador.digicoins < 0:
                jugador.digicoins = 0
            print("Has huído, se te cae un digicoin al salir corriendo")
            print(f"Te quedan {jugador.consultar_digicoins()} digicoins") 


def digishop(jugador, inventario):
    print("|-----Catalogo de Digishop-----|")
    print("1. Digipyballs --> 5 digicoins c/u")
    print("2. Pocion curativa (Restaura 10p de salud) --> 3 Digicoins c/u")
    print("3. Anabolizantes (Aumenta el ataque en 5p) --> 4 Digicoins c/u")
    print("¿Qué desea comprar?")
    opcion_compra = input()
    if opcion_compra == "1" and jugador.digicoins >= 5:
        print("Has comprado una digipyball")
        jugador.digicoins = jugador.digicoins - 5
        inventario.añadir_objeto("Digipyball", 1)

    elif opcion_compra == "2" and jugador.digicoins >= 3:
        print("Has comprado una pocion")
        jugador.digicoins = jugador.digicoins - 3
        inventario.añadir_objeto("Pocion", 1)

    elif opcion_compra == "3" and jugador.digicoins >= 4:
        print("Has comprado un anabolizante")
        jugador.digicoins = jugador.digicoins - 4
        inventario.añadir_objeto("Anabolizante", 1)

    else:
        print("No tienes fondos suficientes o no es la opcion correcta")


def usar_item(jugador, inventario):
    if jugador.lista_digipymon:
        print("¿Sobre que digipymon quieres utilizar tu objeto?")
        jugador.consultar_digipymon()
        seleccion = input()
        jugador.lista_digipymon[seleccion]

        print(inventario.objetos) 
        print("¿Que objeto quieres usar?")
        objeto = (input(""))

        if objeto == "digipyball":
            print("Este objeto no puede ser utilizado en tu digipymon")

        elif objeto == "pocion":
            
            jugador.lista_digipymon[seleccion].vida += 5
            inventario.usar_objeto("Pocion")
            print(f"Has usado una poción en tu {jugador.lista_digipymon[seleccion].nombre}, su vida ha aumentado de {jugador.lista_digipymon[seleccion].ataque}")

            print("La vida de")

        elif objeto == "anabolizante":
            jugador.lista_digipymon[seleccion].ataque += 3
            inventario.usar_objeto("Anabolizante")
            print(f"Has usado anabolizantes en tu {jugador.lista_digipymon[seleccion].nombre}, su ataque actual es de {jugador.lista_digipymon[seleccion].ataque}")
    else:
        print("No tienes digipymons sobre los que usar tus items")             
                                
    
def main():
    jugador1 = Jugador("Pepe")
    inventario1 = Inventario()
    inventario1.añadir_objeto("Digipyball", 2) 
    bucle = True
    while bucle:
        print("Elige una opcion")
        print("1. Buscar Digipymon") 
        print("2. Luchar contra un entrenador")
        print("3. Ir a la teinda")
        print("4. Usar objeto")
        print("5. Consultar inventario")
        print("6. Consultar Digipymons")
        print("7. Salir")
        respuesta = input("Introduce el valor: ")
        
        print(respuesta)
        if respuesta == "1":
            buscar_digipymon(jugador1, inventario1)
        elif respuesta == "2":
            combate(jugador1)
        elif respuesta == "3":
            digishop(jugador1, inventario1)
        elif respuesta == "4":
            usar_item(jugador1, inventario1)
        elif respuesta == "5":
            for nombre, cantidad in inventario1.objetos.items():
                print(f"Item: {nombre}, cantidad: {cantidad} ")
        elif respuesta == "6":
            print(jugador1.consultar_digipymon())
        elif respuesta == "7":
            print("Nos vemos")
            bucle = False
        else:
            print("Esa opcion no es valida")
        
        
    
    
    lista_nombres1 = ListaNombres() 
    enemigo1 = Enemigo(lista_nombres1.obtener_nombre_entrenador())
      
    buscar_digipymon(jugador1, inventario1)
    jugador1.añadir_digipymon(generar_digipymon_aleatorio())
    jugador1.consultar_digipymon()
    digishop(jugador1, inventario1)
    print(inventario1.objetos)
   
main()

    
   
