from zooAnimales.animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color=None, profundidad=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color = color
        self.profundidad = profundidad

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        # Crear un salmón con valores predeterminados
        pez = Pez(nombre, edad, "océano", genero, "rojo")
        Pez.salmones += 1  # Incrementar el contador de salmones
        return pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        # Crear un bacalao con valores predeterminados
        pez = Pez(nombre, edad, "mar profundo", genero, "plateado")
        Pez.bacalaos += 1  # Incrementar el contador de bacalaos
        return pez


