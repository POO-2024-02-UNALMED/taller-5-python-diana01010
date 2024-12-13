class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)
        zona.setZoo(self)  # Asociar la zona al zoológico

    def cantidadTotalAnimales(self):
        total = sum(zona.cantidadAnimales() for zona in self.zonas)
        return total

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getZonas(self):
        return self.zonas

