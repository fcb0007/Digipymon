import digipymon
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 0

    def consultar_digicoin (self):
        return self.digicoins
    
    def añadir_digipymon (self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1

    def consultar_digipymon (self):
        for i in range(0, len(self.lista_digipymon)):
            print(i + self.lista.digipymon[i])
