from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes

    @staticmethod
    def crearIguana(nombre, edad, genero):
        # Crear una iguana con valores predeterminados
        reptil = Reptil(nombre, edad, "selva", genero)
        Reptil.iguanas += 1  # Incrementar el contador de iguanas
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        # Crear una serpiente con valores predeterminados
        reptil = Reptil(nombre, edad, "desierto", genero)
        Reptil.serpientes += 1  # Incrementar el contador de serpientes
        return reptil
