# zoo_animales.py

from gestion.zona import Zona


class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.total_animales += 1
        self.zona = None

    @staticmethod
    def get_total_animales():
        return Animal.total_animales

    @staticmethod
    def total_por_tipo():
        return f"Mamiferos : {Mamifero.cantidad_mamiferos()}\n" \
               f"Aves : {Ave.cantidad_aves()}\n" \
               f"Reptiles : {Reptil.cantidad_reptiles()}\n" \
               f"Peces : {Pez.cantidad_peces()}\n" \
               f"Anfibios : {Anfibio.cantidad_anfibios()}"

    def toString(self):
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, " \
               f"habito en {self.habitat} y mi genero es {self.genero}"

    def movimiento(self):
        return "desplazarse"


class Mamifero(Animal):
    cantidad_mamiferos = 0
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        if nombre.lower() == "caballo":
            Mamifero.caballos += 1
        elif nombre.lower() == "leon":
            Mamifero.leones += 1
        Mamifero.cantidad_mamiferos += 1

    @staticmethod
    def cantidad_mamiferos():
        return Mamifero.cantidad_mamiferos

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        return Mamifero(nombre, edad, "pradera", genero, False, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        return Mamifero(nombre, edad, "sabana", genero, False, 4)

    def movimiento(self):
        return "caminar o correr"


class Ave(Animal):
    cantidad_aves = 0
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        if nombre.lower() == "halcon":
            Ave.halcones += 1
        elif nombre.lower() == "aguila":
            Ave.aguilas += 1
        Ave.cantidad_aves += 1

    @staticmethod
    def cantidad_aves():
        return Ave.cantidad_aves

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        return Ave(nombre, edad, "montañas", genero, "gris")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        return Ave(nombre, edad, "bosques", genero, "blanco")

    def movimiento(self):
        return "volar"


class Reptil(Animal):
    cantidad_reptiles = 0
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        if nombre.lower() == "iguana":
            Reptil.iguanas += 1
        elif nombre.lower() == "serpiente":
            Reptil.serpientes += 1
        Reptil.cantidad_reptiles += 1

    @staticmethod
    def cantidad_reptiles():
        return Reptil.cantidad_reptiles

    @staticmethod
    def crearIguana(nombre, edad, genero):
        return Reptil(nombre, edad, "selvas", genero, "verde", 1)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        return Reptil(nombre, edad, "selvas", genero, "marron", 2)

    def movimiento(self):
        return "arrastrarse"


class Pez(Animal):
    cantidad_peces = 0
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        if nombre.lower() == "salmon":
            Pez.salmones += 1
        elif nombre.lower() == "bacalao":
            Pez.bacalaos += 1
        Pez.cantidad_peces += 1

    @staticmethod
    def cantidad_peces():
        return Pez.cantidad_peces

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        return Pez(nombre, edad, "océanos", genero, "plateado", 2)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        return Pez(nombre, edad, "océanos", genero, "amarillo", 2)

    def movimiento(self):
        return "nadar"


class Anfibio(Animal):
    cantidad_anfibios = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        if nombre.lower() == "rana":
            Anfibio.ranas += 1
        elif nombre.lower() == "salamandra":
            Anfibio.salamandras += 1
        Anfibio.cantidad_anfibios += 1

    @staticmethod
    def cantidad_anfibios():
        return Anfibio.cantidad_anfibios

    @staticmethod
    def crearRana(nombre, edad, genero):
        return Anfibio(nombre, edad, "charcos", genero, "verde", False)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        return Anfibio(nombre, edad, "bosques", genero, "negra", False)

    def movimiento(self):
        return "saltar o nadar"
