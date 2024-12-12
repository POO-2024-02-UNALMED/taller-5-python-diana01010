class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        if nombre.lower() == "salmon":
            Pez.salmones += 1
        elif nombre.lower() == "bacalao":
            Pez.bacalaos += 1

    @staticmethod
    def cantidadPeces():
        return Pez.salmones + Pez.bacalaos

