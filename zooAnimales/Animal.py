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
        return f"Mamíferos: {Mamifero.cantidad_mamiferos()}\n" \
               f"Aves: {Ave.cantidad_aves()}\n" \
               f"Reptiles: {Reptil.cantidad_reptiles()}\n" \
               f"Peces: {Pez.cantidad_peces()}\n" \
               f"Anfibios: {Anfibio.cantidad_anfibios()}"

    def __str__(self):
        info = f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, " \
               f"habito en {self.habitat} y mi género es {self.genero}"
        if self.zona:
            info += f", la zona en la que me ubico es {self.zona.get_nombre()}, " \
                    f"en el {self.zona.get_zoo().get_nombre()}."
        return info

    def movimiento(self):
        return "desplazarse"

    # Métodos getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_habitat(self):
        return self.habitat

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_zona(self):
        return self.zona

    def set_zona(self, zona):
        self.zona = zona
