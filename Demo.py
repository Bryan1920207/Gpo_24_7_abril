class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
        
    def area(self):
        return self.lado*self.lado

##################################################
lado = int(input("Introduzca lado del cuadrado: "))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.area()
print(f"Mi area es {r}")