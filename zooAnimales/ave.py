from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas

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
        ave = Ave(nombre, edad, "montañas", genero, "café glorioso")
        Ave.halcones += 1
        return ave

    @staticmethod
    def crearAguila(nombre, edad, genero):
        ave = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return ave

    def toString(self):
        return self.__str__()

