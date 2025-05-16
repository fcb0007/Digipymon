class Inventario:
    def __init__(self):
        self.objetos = {}
   
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            cantidad = self.objetos[nombre]
            self.objetos[nombre] += cantidad

        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            
            if self.objetos[objeto] == 0:
                del(self.objetos[objeto])
        else:
            print("No dispones de ese objeto")

    