from Animal import Animal

class Pez(Animal):
    cantidad_peces = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)
        Pez.cantidad_peces += 1

    @staticmethod
    def cantidad_peces():
        return Pez.cantidad_peces

    def movimiento(self):
        return "nadar"
