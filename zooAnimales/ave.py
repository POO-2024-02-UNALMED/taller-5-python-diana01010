from zooAnimales.animal import Animal

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

    # Métodos getters y setters
    def getColorPlumas(self):
        return self.colorPlumas

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        return Ave(nombre, edad, "montañas", genero, "gris")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        return Ave(nombre, edad, "bosque", genero, "blanco")
