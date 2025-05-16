class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 5

    def consultar_digicoin (self):
        return self.digicoins
    
    def añadir_digipymon (self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1

    def consultar_digipymon (self):
        if self.lista_digipymon:
            contador = 0
            for digipymon in self.lista_digipymon:
                print("Digipymon --------------------------" + str(contador) + "--------------------------") 
                print(digipymon)
                contador += 1
        else:
            print("No tienes digipymons que mostrar")
