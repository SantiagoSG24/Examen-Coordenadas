

from punto import Punto
from rectangulo import Rectangulo

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