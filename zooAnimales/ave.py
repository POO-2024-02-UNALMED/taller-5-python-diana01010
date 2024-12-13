class Ave(Animal):
    halcones = 0
    aguilas = 0

    @staticmethod
    def resetContadores():
        Ave.halcones = 0
        Ave.aguilas = 0

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "cielo", genero, "gris")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "marrón")

