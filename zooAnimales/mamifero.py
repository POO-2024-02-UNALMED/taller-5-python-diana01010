from zooAnimales.animal import Animal

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

    # Métodos getters y setters
    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        animal = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return animal

    @staticmethod
    def crearLeon(nombre, edad, genero):
        animal = Mamifero(nombre, edad, "sabana", genero, True, 4)
        return animal
