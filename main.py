"""
Módulo main, contiene funciones esenciales para la ejecución
del juego, así como la función main, donde llamaremos a todas 
ellas para crear el flujo principal del programa

- Generación de Digipymons aleatorios
- Menú principal del juego
- Buscar y añadir digipymons a la lista del jugador
- Combate con otros entrenadores (enemigo)
- Compra de ítems
- Uso de ítems
"""
import random
from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from lista_nombres import ListaNombres
from jugador import Jugador

def generar_digipymon_aleatorio():
    """
    Crea una instancia de la clase Digipymon con valores aleatorios

    Returns:
        digipymon1 (Digipymon): Objeto de la clase digipymon con valores aleatorios
    """
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
    """
    Función que imprime en pantalla el menú principal mostrando las distintas opciones

    Returns:
        respuesta (str): Devuelve un str con la opción del usuario
    """
    print("")
    print("Elige una opcion")
    print("1. Buscar Digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objeto")
    print("5. Consultar inventario")
    print("6. Consultar Digipymons")
    print("7. Salir")
    respuesta = input("")
    return respuesta
    
def buscar_digipymon(jugador: Jugador, inventario: Inventario):
    """
    Si el jugador tiene digipyballs y no tiene 6 o más digipymons puede intentar capturar
    un digipymon generado aleatoriamente
    
     Args:
        jugador (Jugador): El jugador al que asignaremos los digipymons si los captura
        inventario (Inventario): Inventario del que obtendremos las digipyballs
     """

    digipymon_encontrado = generar_digipymon_aleatorio()
    probabilidad_captura = 100 - (digipymon_encontrado.nivel *10)
    salir_bucle = True
    while salir_bucle:
        print("Has encontrado un...")
        print(digipymon_encontrado)
        print(f"La probabilidad de captura al {digipymon_encontrado.nombre} es de un {probabilidad_captura}%")
        print("¿Deseas capturar al digipymon?")
        print("1. Sí")
        print("2. No")
        opcion = input()
        if opcion == "1":
            if "Digipyball" in inventario.objetos and jugador.cantidad_digipymon <= 6:
                inventario.usar_objeto("Digipyball")

                if random.randint(1, 100) <= probabilidad_captura:
                    print("Has capturado un " + digipymon_encontrado.nombre + "!!")
                    jugador.añadir_digipymon(digipymon_encontrado)

                    if "Digipyball" in inventario.objetos:
                        print(f"Te quedan {inventario.objetos["Digipyball"]} digipyballs")

                    else:
                        print("No te quedan digipyballs!")                        
                    salir_bucle = False

                else:
                    print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")

                    if "Digipyball" in inventario.objetos:
                        print(f"Te quedan {inventario.objetos["Digipyball"]} digipyballs")
                        
                    else:
                        print("No te quedan digipyballs!")                        
                    salir_bucle = False 

            elif "Digipyball" not in inventario.objetos:
                print("No te quedan digipyballs")
                print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                salir_bucle = False

            elif jugador.cantidad_digipymon == 6:
                print("Ya tienes 6 digipymons, no puedes capturar más")
                print("El digipymon " + digipymon_encontrado.nombre + " ha escapado!")
                salir_bucle = False

            else:
                print("No tienes digipyballs o ya tienes el máximo de digipymons(6)")
                print(f"Digipyballs: {inventario.objetos["Digipyball"]}, digipymons: {jugador.cantidad_digipymon} ")
       
        elif opcion == "2":
            print("Has huido")
            salir_bucle = False

        else:
            print("Introduce una opción correcta")        

def combate(jugador: Jugador):
    """
    Función en la que realiazamos un combate contra un entrenador rival,
    su funcionamiento en resumen es el siguiente:
    
    - Se genera un objeto de ListaNombres del que obtendremos los nombres para el enemigo y sus digipymons
    - Creamos una instancia de enemigo y le añadimos tantos digipymons generados con atributos aleatorios como digipymons tengamos nosotros
    - Comparamos el ataque de sus digipymons y los nuestros para dar al ganador de cada combate
    - Si tienes mas victorias que derrotas ganas tantos digicoins como victorias tengas
    - Si tienes mas derrotas que victorias pierdes tantos digicoins como derrotas tengas
    - Si se produce un empate no pierdes ni ganas digicoins

    Args:
        jugador (Jugador): Jugador que entra en combate
    """ 
    lista_nombres = ListaNombres()
    enemigo = Enemigo(lista_nombres.obtener_nombre_entrenador())
    bucle_combate = True
    for i in range(len(jugador.lista_digipymon)):
        enemigo.añadir_digipymon(generar_digipymon_aleatorio())

    while bucle_combate:
        print("Te has encontrado con " + enemigo.nombre + " y te reta a un combate!")
        print("¿Quieres luchar?")
        print("1. Sí")
        print("2. No")
        opcion = input()

        if opcion == "1":
            victorias = 0    
            derrotas = 0
            for i in range (jugador.cantidad_digipymon):
                digipymon_jugador = jugador.lista_digipymon[i].nombre
                digipymon_enemigo = enemigo.lista_digipymon[i].nombre
                ataque_enemigo = enemigo.lista_digipymon[i].ataque
                ataque_jugador = jugador.lista_digipymon[i].ataque

                print("Tu " + digipymon_jugador)
                print("Se enfrenta a...")
                print(digipymon_enemigo)

                if jugador.lista_digipymon[i].vida <= 0:
                    print(f"Has perdido, tu digipymon {jugador.lista_digipymon[i].nombre}, tiene {jugador.lista_digipymon[i].vida} de vida")
                    derrotas += 1

                elif jugador.lista_digipymon[i].ataque > enemigo.lista_digipymon[i].ataque:
                    victorias += 1
                    jugador.lista_digipymon[i].vida = jugador.lista_digipymon[i].vida - ataque_enemigo
                    print(f"Tu {digipymon_jugador} ha vencido")
                    print(f"Ha perdido {ataque_enemigo} puntos de vida")
                    print(f"Sus puntos de vida restantes son: {jugador.lista_digipymon[i].vida}")
                    print(f"Llevas {victorias} victorias y {derrotas} derrotas")
                    bucle_combate = False


                elif ataque_enemigo > ataque_jugador:
                    derrotas += 1
                    perdida_vida = ataque_jugador - ataque_enemigo
                    jugador.lista_digipymon[i].vida -= perdida_vida
                    if jugador.lista_digipymon[i].vida < 0:
                        jugador.lista_digipymon[i].vida = 0
                    print(f"Has perdido el combate, tu digipymon ha perdido {perdida_vida}, puntos de vida")
                    print(f"Su salud restante es de {jugador.lista_digipymon[i].vida}")

                elif enemigo.lista_digipymon[i].ataque == jugador.lista_digipymon[i].ataque:
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
                bucle_combate = False

            elif derrotas > victorias:
                jugador.digicoins -= derrotas

                if jugador.digicoins < 0:
                    jugador.digicoins = 0
                print(f"Has perdido! Tus victorias han sido: {victorias} y tus derrotas: {derrotas}")
                print(f"Pierdes {derrotas} digicoins, tus digicoins totales son {jugador.digicoins}")
                bucle_combate = False

            elif victorias == derrotas:
                print(f"Ha habido un empate, Tus victorias han sido: {victorias} y tus derrotas: {derrotas}")
                bucle_combate = False
      
        elif opcion == "2":
            jugador.digicoins -= 1

            if jugador.digicoins < 0:
                jugador.digicoins = 0
            print("Has huído, se te cae un digicoin al salir corriendo")
            print(f"Te quedan {jugador.consultar_digicoins()} digicoins")
            bucle_combate = False


def digishop(jugador: Jugador, inventario: Inventario):
    print("|-----Catalogo de Digishop-----|")
    print(f"Monedero actual: {jugador.digicoins} digicoins")
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
    
    print(f"Te quedan {jugador.digicoins} digicoins")


def usar_item(jugador: Jugador, inventario: Inventario):
    bucle_item = True
    while bucle_item:
        if jugador.lista_digipymon:
            if inventario.objetos:
                print("¿Sobre que digipymon quieres utilizar tu objeto?")
                jugador.consultar_digipymon()
                seleccion = int(input())
                jugador.lista_digipymon[seleccion]

                inventario.mostrar_inventario()
                    
                print("¿Que objeto quieres usar? (introduce 'salir' para volver al menú)")
                objeto = input("")
                
                if objeto.lower() == "digipyball":
                    print("Este objeto no puede ser utilizado en tu digipymon")

                elif objeto.lower() == "pocion":
                    vida_previa = jugador.lista_digipymon[seleccion].vida
                    jugador.lista_digipymon[seleccion].vida += 5
                    inventario.usar_objeto("Pocion")
                    print(f"Has usado una poción en tu {jugador.lista_digipymon[seleccion].nombre}, su vida ha aumentado de {vida_previa} a {jugador.lista_digipymon[seleccion].vida}")
                    bucle_item = False

                elif objeto.lower() == "anabolizante":
                    ataque_previo = jugador.lista_digipymon[seleccion].ataque
                    jugador.lista_digipymon[seleccion].ataque += 3
                    inventario.usar_objeto("Anabolizante")
                    print(f"Has usado anabolizantes en tu {jugador.lista_digipymon[seleccion].nombre}, su ataque ha aumentado de {ataque_previo} a {jugador.lista_digipymon[seleccion].ataque}")
                    bucle_item = False

                elif objeto == "salir":
                    bucle_item = False

                else:
                    print("Introduce una opción válida")
            else:
                print("No tienes objetos que usar!")
                bucle_item = False
        else:
            print("No tienes digipymons sobre los que usar tus items")
            bucle_item = False

def main():
    print("Bienvenido a Digipymon!, Aquí empieza tu aventura...")
    print("¿Cómo te llamas?")
    nombre_jugador = input("")
    jugador1 = Jugador(nombre_jugador)
    inventario1 = Inventario()
    print("Al comenzar en.... recibes una poción y tres digipyballs")
    inventario1.añadir_objeto("Digipyball", 3)
    
    bucle = True
    while bucle:
        respuesta = menu()        
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
            inventario1.mostrar_inventario()      
        elif respuesta == "6":
            jugador1.consultar_digipymon()
        elif respuesta == "7":
            print("Nos vemos!")
            bucle = False
        else:
            print("Esa opción no es válida")
       
main()