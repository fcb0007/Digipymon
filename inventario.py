class Inventario:
    def __init__(self):
        self.objetos = {}
   
    def añadir_objeto(self, nombre, cantidad):
        cantidad = 0
        if nombre in self.objetos:
            cantidad = self.objetos[nombre]
            self.objetos[nombre] = cantidad + 1

        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, objeto):
        if objeto in self.objetos:
            cantidad_previa = 0
            cantidad_previa = self.objetos[objeto]
            self.objetos[objeto] = cantidad_previa - 1
            
            if self.objetos[objeto] == 0:
                del(self.objetos[objeto])
        else:
            print("No dispones de ese objeto")

    