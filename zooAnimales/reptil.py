class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    @staticmethod
    def resetContadores():
        Reptil.iguanas = 0
        Reptil.serpientes = 0

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "selva", genero, "verde", 1)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "desierto", genero, "amarillo", 0)

