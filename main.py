import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)


class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()


# Experimentación
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

print("\nCuadrantes:")
print(f"A: {A.cuadrante()}")
print(f"C: {C.cuadrante()}")
print(f"D: {D.cuadrante()}")

print("\nVectores:")
print(f"Vector AB: {A.vector(B)}")
print(f"Vector BA: {B.vector(A)}")

print("\nDistancias:")
print(f"Distancia A-B: {A.distancia(B)}")
print(f"Distancia B-A: {B.distancia(A)}")

print("\nPunto más lejano del origen:")
distancias = {"A": A.distancia(D), "B": B.distancia(D), "C": C.distancia(D)}
punto_mas_lejano = max(distancias, key=distancias.get)
print(f"El punto más lejano del origen es {punto_mas_lejano}")

print("\nRectángulo:")
rectangulo = Rectangulo(A, B)
print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Área: {rectangulo.area()}")





# Crear puntos fácilmente
print("\nCreación de puntos fácilmente:")
x, y = map(int, input("Introduce las coordenadas del punto separadas por un espacio (x y): ").split())
nuevo_punto = Punto(x, y)
print(f"Nuevo punto creado: {nuevo_punto}")






# Determinar el cuadrante de un punto ingresado por el usuario
print("\nDeterminar cuadrante de un punto:")
x, y = map(int, input("Introduce las coordenadas del punto separadas por un espacio (x y): ").split())
punto_usuario = Punto(x, y)
print(f"El punto {punto_usuario} está en: {punto_usuario.cuadrante()}")