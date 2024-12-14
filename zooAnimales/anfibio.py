from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, esCarnivoro=None, patas=4):
        super().__init__(nombre, edad, habitat, genero)
        self.color = color
        self.esCarnivoro = esCarnivoro
        self.patas = patas

    @staticmethod
    def cantidadAnfibios():
        return Anfibio.ranas + Anfibio.salamandras

    def getColorPiel(self):
        return self.color  # Agregado para el test

    @staticmethod
    def crearRana(nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "pantano", genero, "verde")
        Anfibio.ranas += 1  # Incrementar el contador de ranas
        return anfibio

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "bosque", genero, "marrón")
        Anfibio.salamandras += 1  # Incrementar el contador de salamandras
        return anfibio


