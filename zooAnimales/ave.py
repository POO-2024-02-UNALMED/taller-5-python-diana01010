class Ave(Animal):
    halcones = 0
    aguilas = 0
    aves = []

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "cielo", genero, "gris")
        Ave.halcones += 1
        Ave.aves.append(halcon)
        return halcon

    @staticmethod
    def crearAguila(nombre, edad, genero):
        aguila = Ave(nombre, edad, "montañas", genero, "blanco")
        Ave.aguilas += 1
        Ave.aves.append(aguila)
        return aguila

    @staticmethod
    def cantidadAves():
        return len(Ave.aves)
