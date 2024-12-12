from Animal import Animal

class Ave(Animal):
    cantidad_aves = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)
        Ave.cantidad_aves += 1

    @staticmethod
    def cantidad_aves():
        return Ave.cantidad_aves

    def movimiento(self):
        return "volar"
