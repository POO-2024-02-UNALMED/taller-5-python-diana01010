from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)  # Llamada al constructor de la clase base Animal
        self.colorEscamas = colorEscamas  # Asignación del color de las escamas
        self.largoCola = largoCola  # Asignación del largo de la cola

    @staticmethod
    def cantidadReptiles():
        # Retorna la cantidad total de reptiles, sumando iguanas y serpientes
        return Reptil.iguanas + Reptil.serpientes

    # Métodos getters
    def getNombre(self):
        return self.nombre  # Método para obtener el nombre del reptil

    def getEdad(self):
        return self.edad  # Método para obtener la edad del reptil

    def getHabitat(self):
        return self.habitat  # Método para obtener el habitat del reptil

    def getGenero(self):
        return self.genero  # Método para obtener el genero del reptil

    def getColorEscamas(self):
        return self.colorEscamas  # Método para obtener el color de las escamas

    def getLargoCola(self):
        return self.largoCola  # Método para obtener el largo de la cola

    @staticmethod
    def crearIguana(nombre, edad, genero):
        # Crea una iguana con los valores adecuados
        reptil = Reptil(nombre, edad, "selva", genero, "verde", 3)
        Reptil.iguanas += 1  # Incrementa el contador de iguanas
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        # Crea una serpiente con los valores adecuados
        reptil = Reptil(nombre, edad, "desierto", genero, "amarillo", 5)
        Reptil.serpientes += 1  # Incrementa el contador de serpientes
        return reptil
