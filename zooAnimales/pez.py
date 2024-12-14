from zooAnimales.animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        # Crear un salmón con valores predeterminados
        pez = Pez(nombre, edad, "océano", genero)
        Pez.salmones += 1  # Incrementar el contador de salmones
        return pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        # Crear un bacalao con valores predeterminados
        pez = Pez(nombre, edad, "mar profundo", genero)
        Pez.bacalaos += 1  # Incrementar el contador de bacalaos
        return pez

