class Ave(Animal):
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        if nombre.lower() == "halcon":
            Ave.halcones += 1
        elif nombre.lower() == "aguila":
            Ave.aguilas += 1

    @staticmethod
    def cantidadAves():
        return Ave.halcones + Ave.aguilas

