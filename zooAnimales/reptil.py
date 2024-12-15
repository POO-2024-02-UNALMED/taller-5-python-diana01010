from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas=None, esVenenoso=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.esVenenoso = esVenenoso
        self.largoCola = largoCola

    @staticmethod
    def cantidadReptiles():
        # Retorna la cantidad total de reptiles, sumando iguanas y serpientes
        return Reptil.iguanas + Reptil.serpientes

    # Métodos getters
    def getColorEscamas(self):
        return self.colorEscamas  # Devuelve el color de las escamas

    def getLargoCola(self):
        return self.largoCola  # Devuelve el largo de la cola

    # Métodos estáticos para crear iguanas y serpientes
    @staticmethod
    def crearIguana(nombre, edad, genero):
        # Crea una iguana con los valores adecuados
        reptil = Reptil(nombre, edad, "selva", genero, "verde", False, 2)
        Reptil.iguanas += 1  # Incrementa el contador de iguanas
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        # Crea una serpiente con los valores adecuados
        reptil = Reptil(nombre, edad, "desierto", genero, "amarillo", True, 5)
        Reptil.serpientes += 1  # Incrementa el contador de serpientes
        return reptil



