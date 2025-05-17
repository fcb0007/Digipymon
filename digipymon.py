class Digipymon:
    """
    Clase que representa a los digipymon que puede tener un jugador

    Attributes:
        nombre (str): Nombre del digipymon
        vida (int): Vida del digipymon
        ataque (int): Puntos de ataque del digipymon
        tipo (): Tipo de digipymon (fuego, agua...)
        nivel (int): Nivel del digipymon
    """        
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        """
        Constructor de la clase digipymon

        Args:
            nombre (str): Nombre del digipymon
            vida (int): Vida del digipymon
            ataque (int): Puntos de ataque del digipymon
            tipo (): Tipo de digipymon (fuego, agua...)
            nivel (int): Nivel del digipymon
        """
        self.nombre = nombre
        self. vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel 

    def __str__(self):
        """
        Método __str__ de digipymon

        Returns: 
            str: Devuelve los atributos del digipymon
        """
        return f"Nombre: {self.nombre}, vida: {self.vida}, ataque: {self.ataque}, tipo: {self.tipo}, nivel: {self.nivel}"
