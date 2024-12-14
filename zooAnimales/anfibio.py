from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)

    @staticmethod
    def cantidadAnfibios():
        return Anfibio.ranas + Anfibio.salamandras

    @staticmethod
    def crearRana(nombre, edad, genero):
        # Crear una rana con valores predeterminados
        anfibio = Anfibio(nombre, edad, "pantano", genero)
        Anfibio.ranas += 1  # Incrementar el contador de ranas
        return anfibio

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        # Crear una salamandra con valores predeterminados
        anfibio = Anfibio(nombre, edad, "bosque", genero)
        Anfibio.salamandras += 1  # Incrementar el contador de salamandras
        return anfibio

