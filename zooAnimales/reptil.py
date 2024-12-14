from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        if nombre.lower() == "iguana":
            Reptil.iguanas += 1
        elif nombre.lower() == "serpiente":
            Reptil.serpientes += 1

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes

    # Métodos getters y setters
    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola

    def movimiento(self):
        return "deslizarse"

    def toString(self):
        return super().toString() + ", mi color de escamas es " + self.colorEscamas + " y mi largo de cola es " + str(self.largoCola)

    # Método estático para crear una Iguana
    @staticmethod
    def crearIguana(nombre, edad, genero):
        return Reptil(nombre, edad, "bosque", genero, "verde", 5)  # Asignamos un valor predeterminado para largo de cola

    # Método estático para crear una Serpiente
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        return Reptil(nombre, edad, "selva", genero, "marrón", 3)  # Asignamos un valor predeterminado para largo de cola

