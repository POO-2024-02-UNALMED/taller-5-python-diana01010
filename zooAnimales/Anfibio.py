from Animal import Animal

class Anfibio(Animal):
    cantidad_anfibios = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)
        Anfibio.cantidad_anfibios += 1

    @staticmethod
    def cantidad_anfibios():
        return Anfibio.cantidad_anfibios

    def movimiento(self):
        return "saltando o nadando"
