# Animal.py

class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales += 1
        self.zona = None

    @staticmethod
    def getTotalAnimales():
        return Animal.totalAnimales

    def __str__(self):
        info = f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}"
        if self.zona:
            info += f", la zona en la que me ubico es {self.zona.getNombre()}, en el {self.zona.getZoo().getNombre()}."
        return info

    def movimiento(self):
        return "desplazarse"


