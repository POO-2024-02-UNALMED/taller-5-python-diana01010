from Animal import Animal

class Mamifero(Animal):
    cantidad_mamiferos = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)
        Mamifero.cantidad_mamiferos += 1

    @staticmethod
    def cantidad_mamiferos():
        return Mamifero.cantidad_mamiferos

    def movimiento(self):
        return "caminar o correr"
