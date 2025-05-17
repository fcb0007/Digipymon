class Jugador:
    """
    Clase que representa al personaje del usuario
    
    Attributes:
        nombre (str): Nombre del jugador
        lista_digipymon (list): Lista que almacena los digipymons (objetos) del jugador
        cantidad_digipymon (int): Número de digipymons del jugador
        digicoins (int): Dinero que posee el jugador
    """
    def __init__(self, nombre):
        """
        Constructor de la clase Jugador, instancia un jugador con 5 digicoins, 0 digipymons
        y obtiene el nombre por parámetro

        Args:
            nombre (str): Nombre del jugador
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 5

    def consultar_digicoin (self):
        """
        Devuelve la cantidad de digicoins del jugador

        Returns:
            int: Digicoins del jugador
        """
        return self.digicoins
    
    def añadir_digipymon (self, digipymon):
        """
        Método que añade un  digipymon al final de lista_digipymon y suma 1 a cantidad_digipymon

        Args:
            digipymon (Digipymon): Objeto digipymon que añadimos a la lista
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1

    def consultar_digipymon (self):
        """
        Método que muestra todos los digipymons que hay en lista_digipymon
        recorriendo la lista con un for y numerándolos según su posición en la lista
        si no hay digipymons mostrará un mensaje avisando al usuario
        """
        if self.lista_digipymon:
            contador = 0
            print("----------------Estos son tus Digipymon-----------------") 
            for digipymon in self.lista_digipymon:                
                print(f"{contador}. {digipymon}")
                contador += 1
        else:
            print("No tienes digipymons que mostrar")
