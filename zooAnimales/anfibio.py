# zooAnimales/anfibio.py
from zooAnimales.animal import Animal  # Importa la clase Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    anfibios = []

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso

    @staticmethod
    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "charcos", genero, "verde", False)
        Anfibio.ranas += 1
        Anfibio.anfibios.append(rana)
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "bosques", genero, "amarillo", True)
        Anfibio.salamandras += 1
        Anfibio.anfibios.append(salamandra)
        return salamandra

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.anfibios)

