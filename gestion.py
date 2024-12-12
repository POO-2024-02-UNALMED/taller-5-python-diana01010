# gestion.py

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregar_zonas(self, zona):
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        total = 0
        for zona in self.zonas:
            total += zona.cantidad_animales()
        return total

    # Métodos getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_zonas(self):
        return self.zonas


class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregar_animales(self, animal):
        self.animales.append(animal)

    def cantidad_animales(self):
        return len(self.animales)

    # Métodos getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_zoo(self):
        return self.zoo

    def set_zoo(self, zoo):
        self.zoo = zoo

    def get_animales(self):
        return self.animales
