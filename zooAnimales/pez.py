from zooAnimales.animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, profundidad=None, aletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color = color
        self.profundidad = profundidad
        self.aletas = aletas

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

    def getColorEscamas(self):
        return self.color  # Método para obtener el color de las escamas

    def getCantidadAletas(self):
        return self.aletas  # Método agregado para el test

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        pez = Pez(nombre, edad, "océano", genero, "rojo", 100, 2)
        Pez.salmones += 1
        return pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        pez = Pez(nombre, edad, "mar profundo", genero, "plateado", 200, 3)
        Pez.bacalaos += 1
        return pez




