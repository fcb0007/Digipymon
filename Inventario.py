class Inventario:
    def __init__(self):
        self.objetos = {}
   
    def añadir_objeto(self, nombre, cantidad):

        if nombre in self.objetos:
            self.cantidad = self.objetos.get(self.nombre)
            self.objetos[self.nombre] = self.cantidad + 1

        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, objeto):
        if objeto in self.objetos:
            cantidad_previa = 0
            cantidad_previa = self.objetos.get(self.objeto)
            self.objetos[objeto] = cantidad_previa - 1
            
            if self.objetos.get(self.objeto) == 0:
                del self.objetos[objeto]
        else:
            print("No dispones de ese objeto")