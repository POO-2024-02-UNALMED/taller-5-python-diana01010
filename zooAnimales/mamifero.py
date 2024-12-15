class Mamifero(Animal):
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)

    @staticmethod
    def cantidadMamiferos():
        return Mamifero.caballos + Mamifero.leones

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "pradera", genero)
        Mamifero.caballos += 1
        return mamifero

    @staticmethod
    def crearLeon(nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "sabana", genero)
        Mamifero.leones += 1
        return mamifero

    def toString(self):
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
