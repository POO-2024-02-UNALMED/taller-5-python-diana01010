# zooAnimales/mamifero.py
from zooAnimales.animal import Animal  # Importa la clase Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    mamiferos = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        Mamifero.mamiferos.append(caballo)
        return caballo

    @staticmethod
    def crearLeon(nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        Mamifero.mamiferos.append(leon)
        return leon

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.mamiferos)


