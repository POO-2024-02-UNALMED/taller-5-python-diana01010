from zooAnimales.animal import Animal

class Mamifero(Animal):
    # Contadores estáticos para caballos y leones
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas

    @staticmethod
    def cantidadMamiferos():
        # Retorna la cantidad total de mamíferos creados
        return Mamifero.caballos + Mamifero.leones

    # Métodos getters y setters
    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        # Crear un Mamífero de tipo Caballo con valores predeterminados
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1  # Incrementar el contador de caballos
        return caballo

    @staticmethod
    def crearLeon(nombre, edad, genero):
        # Crear un Mamífero de tipo León con valores predeterminados
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1  # Incrementar el contador de leones
        return leon

