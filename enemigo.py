class Enemigo:
    """
    Clase Enemigo, representa a los entrenadores rivales que también poseen una lista
    de digipymons

    Attributes:
        nombre (str): Nombre del enemigo
        lista_digipymon (list): Lista de digipymons(objetos) del enemigo
        canitdad_digipymon (int): Número de digipymons del enemigo
    """
    def __init__(self, nombre):
        """
        Constructor de la clase enemigo

        Args:
            nombre (str): Nombre del enemigo
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self, digipymon):
        """
        Añade un digipymon a la lista del enemigo

        Args:
            digipymon (Digipymon): Objeto digipymon que se añadirá a la lista
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
