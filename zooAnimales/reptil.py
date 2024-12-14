from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, esVenenoso=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color = color
        self.esVenenoso = esVenenoso
        self.largoCola = largoCola

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes

    def getColorEscamas(self):
        return self.color  # Método para obtener el color de las escamas

    def getLargoCola(self):
        return self.largoCola  # Método agregado para el test

    @staticmethod
    def crearIguana(nombre, edad, genero):
        reptil = Reptil(nombre, edad, "selva", genero, "verde", False, 2)
        Reptil.iguanas += 1  # Incrementar el contador de iguanas
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        reptil = Reptil(nombre, edad, "desierto", genero, "amarillo", True, 5)
        Reptil.serpientes += 1  # Incrementar el contador de serpientes
        return reptil


