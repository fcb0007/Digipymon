import random
class ListaNombres:
    """
    Clase con listas de nombres que se asignarán a los digipymons generados y
    a los entrenadores enemigos
    
    Attributes:
        lista_nombres_digipymons (list): Lista de nombres para los digipymons
        lista_nombres_entrenadores (list): Lista de nombres para los entrenadores enemigos

    """
    def __init__(self):
        """
        Constructor de la clase ListasNombres
        """
        self.lista_nombres_digipymons = ["Printmon", "Bugmon", "Loopmon", "Importmon", "Syntaxmon",
        "Bytepymon", "Arraymon", "Debuggermon", "Stackmon", "Recursimon",
        "Lambdaemon", "Regexmon", "Nopemon", "OOPmon", "Modulemon",
        "Pipmon", "Trymon", "Fstringmon", "Exceptmon", "Yieldmon"]
        
        self.lista_nombres_entrenadores = ["Profe Paco", "Bucles Beto", "Errores Ernesto", "Clases Clara", "Pipero Pedro",
        "Depura Dani", "Listas Lola", "Código Carla", "Python Pablo", "Importa Iván",
        "Recursivo Ramón", "Objetos Omar", "Prueba Paula", "Consola Carla", "Modular Marta",
        "Variable Víctor", "Debug Diego", "Mensaje Manuel", "Cadena Carmen", "Script Samuel"]

    def obtener_nombre_digipymon(self):
        """
        Método que devueleve devuelve un nombre aleatorio de lista_nombres_digipymons

        Returns:
            str: Nombre del digipymon
        """
        nombre_digipymon = random.choice(self.lista_nombres_digipymons)
        return nombre_digipymon
    
    def obtener_nombre_entrenador(self):
        """
        Método que devuelve un nombre aleatorio de lista_nombres_entrenador

        Returns:
            str: Nombre que asignaremos al entrenador enemigo
        """
        nombre_entrenador = random.choice(self.lista_nombres_entrenadores)
        return nombre_entrenador
