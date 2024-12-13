class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    @staticmethod
    def resetContadores():
        Anfibio.ranas = 0
        Anfibio.salamandras = 0

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "pradera", genero, "verde", False)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "bosque", genero, "amarillo", True)

