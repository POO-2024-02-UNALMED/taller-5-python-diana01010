class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    reptiles = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola

    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "bosques", genero, "verde", 3)
        Reptil.iguanas += 1
        Reptil.reptiles.append(iguana)
        return iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "selva", genero, "marrón", 5)
        Reptil.serpientes += 1
        Reptil.reptiles.append(serpiente)
        return serpiente

    @staticmethod
    def cantidadReptiles():
        return len(Reptil.reptiles)
