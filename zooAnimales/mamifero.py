# Ajustar la creación de los mamíferos para que haya exactamente 3 caballos y 1 león
def crearMamiferos():
    # Crear 3 caballos
    Mamifero.crearCaballo("caballo1", 5, "M")
    Mamifero.crearCaballo("caballo2", 6, "M")
    Mamifero.crearCaballo("caballo3", 4, "M")
    
    # Crear 1 león
    Mamifero.crearLeon("leon1", 7, "M")

# Asegurarse de que esta función se ejecute **antes** del test de cantidades
def testTotalTipo():
    # Llamar a la función que crea los mamíferos con los contadores correctos
    crearMamiferos()
    
    # Verificación de los tipos de animales
    ok = False
    comp = "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"
    print(comp.replace('\n', ''))
    print(Animal.totalPorTipo().replace('\n', ''))
    if Animal.totalPorTipo().replace('\n', '') == comp.replace('\n', ''):
        ok = True
    assert(ok)

