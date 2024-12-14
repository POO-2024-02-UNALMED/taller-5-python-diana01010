from zooAnimales.animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, profundidad=None, aletas=0):
        # Llamamos al constructor de la clase base Animal
        super().__init__(nombre, edad, habitat, genero)
        self.color = color  # Asignamos el color correctamente
        self.profundidad = profundidad
        self.aletas = aletas  # Asignamos el número de aletas correctamente

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

    def getColorEscamas(self):
        return self.color  # Este método debe devolver el color de las escamas correctamente

    def getCantidadAletas(self):
        return self.aletas  # Este método debe devolver el número de aletas correctamente

    # Métodos estáticos para crear salmones y bacalaos
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





