# zooAnimales/animal.py
class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.totalAnimales += 1

    @staticmethod
    def getTotalAnimales():
        return Animal.totalAnimales

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\n" \
               f"Aves: {Ave.cantidadAves()}\n" \
               f"Reptiles: {Reptil.cantidadReptiles()}\n" \
               f"Peces: {Pez.cantidadPeces()}\n" \
               f"Anfibios: {Anfibio.cantidadAnfibios()}"

    def toString(self):
        if self.zona:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, " \
                   f"habito en {self.habitat} y mi genero es {self.genero}, " \
                   f"la zona en la que me ubico es {self.zona.getNombre()}, " \
                   f"en el {self.zona.getZoo().getNombre()}. "
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, " \
                   f"habito en {self.habitat} y mi genero es {self.genero}"

    def movimiento(self):
        return "desplazarse"

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getZona(self):
        return self.zona

    def

