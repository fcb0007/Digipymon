import random
class ListaNombres:
    def __init__(self):
        self.lista_nombres_digipymons = ["Printmon", "Bugmon", "Loopmon", "Importmon", "Syntaxmon",
        "Bytepymon", "Arraymon", "Debuggermon", "Stackmon", "Recursimon",
        "Lambdaemon", "Regexmon", "Nopemon", "OOPmon", "Modulemon",
        "Pipmon", "Trymon", "Fstringmon", "Exceptmon", "Yieldmon"]
        
        self.lista_nombres_entrenadores = ["Profe Paco", "Bucles Beto", "Errores Ernesto", "Clases Clara", "Pipero Pedro",
        "Depura Dani", "Listas Lola", "Código Carla", "Python Pablo", "Importa Iván",
        "Recursivo Ramón", "Objetos Omar", "Prueba Paula", "Consola Carla", "Modular Marta",
        "Variable Víctor", "Debug Diego", "Mensaje Manuel", "Cadena Carmen", "Script Samuel"]

    def obtener_nombre_digipymon(self):
        nombre_digipymon = random.choice(self.lista_nombres_digipymons)
        return nombre_digipymon
    
    def obtener_nombre_entrenador(self):
        nombre_entrenador = random.choice(self.lista_nombres_entrenadores)
        return nombre_entrenador
