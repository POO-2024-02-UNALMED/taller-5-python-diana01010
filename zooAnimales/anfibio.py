from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        if nombre.lower() == "rana":
            Anfibio.ranas += 1
        elif nombre.lower() == "salamandra":
            Anfibio.salamandras += 1

    @staticmethod
    def cantidadAnfibios():
        return Anfibio.ranas + Anfibio.salamandras

    # Métodos getters y setters
    def getColorPiel(self):
        return self.colorPiel

    def setColorPiel(self, colorPiel):
        self.colorPiel = colorPiel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso

    @staticmethod
    def crearRana(nombre, edad, genero):
        return Anfibio(nombre, edad, "agua", genero, "verde", False)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        return Anfibio(nombre, edad, "bosque", genero, "amarillo", True)
