from punto import Punto
from rectangulo import Rectangulo

# Crear los puntos A, B, C y D
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir los puntos
print("Coordenadas de los puntos:")
print(f"  Punto A: ({A.x}, {A.y})")
print(f"  Punto B: ({B.x}, {B.y})")
print(f"  Punto C: ({C.x}, {C.y})")
print(f"  Punto D: ({D.x}, {D.y})\n")

# Consultar a qué cuadrante pertenecen los puntos A, C y D
print("Cuadrantes de los puntos:")
print(f"  Cuadrante de A: {A.cuadrante()}")
print(f"  Cuadrante de C: {C.cuadrante()}")
print(f"  Cuadrante de D: {D.cuadrante()}\n")

# Consultar los vectores AB y BA
print("Vectores entre puntos:")
print(f"  Vector AB: {A.vector(B)}")
print(f"  Vector BA: {B.vector(A)}\n")

# Consultar la distancia entre los puntos A y B, y B y A
print("Distancias entre puntos:")
print(f"  Distancia entre A y B: {A.distancia(B)}")
print(f"  Distancia entre B y A: {B.distancia(A)}\n")

# Imprimir la fórmula utilizada para calcular la distancia
print("Fórmula utilizada para calcular la distancia entre dos puntos:")
print("  distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2)\n")

# Determinar cuál de los puntos A, B o C está más lejos del origen
distancias = {
    "A": A.distancia(D),
    "B": B.distancia(D),
    "C": C.distancia(D)
}
punto_mas_lejos = max(distancias, key=distancias.get)
print(f"El punto más lejos del origen es: {punto_mas_lejos}\n")

# Crear un rectángulo utilizando los puntos A y B
rectangulo = Rectangulo(A, B)

# Consultar la base, altura y área del rectángulo
print("Propiedades del rectángulo formado por A y B:")
print(f"  Base: {rectangulo.base()}")
print(f"  Altura: {rectangulo.altura()}")
print(f"  Área: {rectangulo.area()}")
