"""
Módulo que contiene la clase Inventario
"""
class Inventario:
    """
    Clase Inventario que almacena los objetos del jugador en un diccionario
    
    Attributes:
        objetos (dict): Diccionario donde se almacenan los objetos del jugador
    """
    def __init__(self):
        """
        Constructor de inventario, crea un diccionario vacío
        """
        self.objetos = {}
   
    def añadir_objeto(self, nombre, cantidad):
        """
        Método para añadir un objeto al diccionario, primero comprueba
        que si el objeto ya está en el diccionario, si está suma la nueva cantidad
        a la anterior, si no, añade al diccionario el nombre y su cantidad asociada
        
        Args:
            nombre (str): Nombre o clave del objeto
            cantidad (int): Cantidad que añadiremos
        """
        
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad

        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, objeto):
        """
        Método usar_objeto de que, comprobando previamente si un objeto 
        se encuetra en el diccionario, le resta 1 a su valor asociado,
        si no, muestra un mensaje diciendo que no tienes el objeto

        Args:
            objeto (str): Nombre del objeto que usaremos
        """
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            
            if self.objetos[objeto] == 0:
                del self.objetos[objeto]
        else:
            print("No dispones de ese objeto")

    def mostrar_inventario(self):
        """
        Método que muestra todos los objetos contenidos en  el diccionario
        recorriéndolo con un bucle for
        """
        if self.objetos:
            print("--------------Estos son tus ítems------------------")
            for nombre, cantidad in self.objetos.items():
                print(f"Item: {nombre}, cantidad: {cantidad} ")
        else:
            print("No tienes items que mostrar")
