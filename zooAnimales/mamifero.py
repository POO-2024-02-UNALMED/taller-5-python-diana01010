class Mamifero(Animal):
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        if nombre.lower() == "caballo":
            Mamifero.caballos += 1
        elif nombre.lower() == "leon":
            Mamifero.leones += 1

    @staticmethod
    def cantidadMamiferos():
        return Mamifero.caballos + Mamifero.leones

