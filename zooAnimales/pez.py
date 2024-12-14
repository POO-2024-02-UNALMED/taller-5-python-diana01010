# Pez.py

from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        if nombre.lower() == "salmon":
            Pez.salmones += 1
        elif nombre.lower() == "bacalao":
            Pez.bacalaos += 1

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        return Pez(nombre, edad, "océano", genero, "plateado", 2)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        return Pez(nombre, edad, "mar", genero, "verde", 3)

