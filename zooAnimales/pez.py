class Pez(Animal):
    salmones = 0
    bacalaos = 0

    @staticmethod
    def resetContadores():
        Pez.salmones = 0
        Pez.bacalaos = 0

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "río", genero, "rojo", 3)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "mar", genero, "verde", 2)

