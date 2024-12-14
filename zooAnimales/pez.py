from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        # Llamada al constructor de la clase base Animal
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas  # Asigna el color de las escamas
        self.cantidadAletas = cantidadAletas  # Asigna el número de aletas

        # Incrementar el contador de salmones o bacalaos según el nombre
        if nombre.lower() == "salmon":
            Pez.salmones += 1
        elif nombre.lower() == "bacalao":
            Pez.bacalaos += 1

    @staticmethod
    def cantidadPeces():
        # Retorna la cantidad total de peces creados
        return Pez.salmones + Pez.bacalaos

    # Métodos getters y setters
    def getColorEscamas(self):
        return self.colorEscamas  # Devuelve el color de las escamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas  # Asigna un nuevo color a las escamas

    def getCantidadAletas(self):
        return self.cantidadAletas  # Devuelve el número de aletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas  # Asigna un nuevo número de aletas

    # Métodos estáticos para crear salmones y bacalaos
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        # Crea un nuevo Salmon con valores predeterminados para color y aletas
        pez = Pez(nombre, edad, "océano", genero, "rojo", 2)
        Pez.salmones += 1  # Incrementa el contador de salmones
        return pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        # Crea un nuevo Bacalao con valores predeterminados para color y aletas
        pez = Pez(nombre, edad, "mar profundo", genero, "plateado", 3)
        Pez.bacalaos += 1  # Incrementa el contador de bacalaos
        return pez








