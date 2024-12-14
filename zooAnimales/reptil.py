# Reptil.py

from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        if nombre.lower() == "iguana":
            Reptil.iguanas += 1
        elif nombre.lower() == "serpiente":
            Reptil.serpientes += 1

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes

    @staticmethod
    def crearIguana(nombre, edad, genero):
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

