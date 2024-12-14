from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, esVenenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color = color
        self.esVenenoso = esVenenoso

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes

    @staticmethod
    def crearIguana(nombre, edad, genero):
        # Crear una iguana con valores predeterminados
        reptil = Reptil(nombre, edad, "selva", genero, "verde")
        Reptil.iguanas += 1  # Incrementar el contador de iguanas
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        # Crear una serpiente con valores predeterminados
        reptil = Reptil(nombre, edad, "desierto", genero, "amarillo")
        Reptil.serpientes += 1  # Incrementar el contador de serpientes
        return reptil
