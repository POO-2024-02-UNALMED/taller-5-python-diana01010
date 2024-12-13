class Pez(Animal):
    salmones = 0
    bacalaos = 0
    peces = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        salmon = Pez(nombre, edad, "océano", genero, "plateado", 4)
        Pez.salmones += 1
        Pez.peces.append(salmon)
        return salmon

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        bacalao = Pez(nombre, edad, "mares fríos", genero, "blanco", 3)
        Pez.bacalaos += 1
        Pez.peces.append(bacalao)
        return bacalao

    @staticmethod
    def cantidadPeces():
        return len(Pez.peces)

