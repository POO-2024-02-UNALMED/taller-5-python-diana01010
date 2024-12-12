from Animal import Animal

class Reptil(Animal):
    cantidad_reptiles = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)
        Reptil.cantidad_reptiles += 1

    @staticmethod
    def cantidad_reptiles():
        return Reptil.cantidad_reptiles

    def movimiento(self):
        return "arrastrarse"
