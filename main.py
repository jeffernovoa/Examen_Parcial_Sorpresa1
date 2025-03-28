import math

# Crear los puntos
A = (2, 3)
B = (5, 5)
C = (-3, -1)
D = (0, 0)

# Imprimir los puntos
print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# Función para determinar el cuadrante de un punto
def cuadrante(punto):
    x, y = punto
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    else:
        return "Eje"

# Consultar cuadrantes
print("\nCuadrantes:")
print(f"A pertenece al cuadrante: {cuadrante(A)}")
print(f"C pertenece al cuadrante: {cuadrante(C)}")
print(f"D pertenece al cuadrante: {cuadrante(D)}")

# Función para calcular un vector entre dos puntos
def vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

# Consultar vectores AB y BA
AB = vector(A, B)
BA = vector(B, A)
print("\nVectores:")
print(f"Vector AB: {AB}")
print(f"Vector BA: {BA}")

# Función para calcular la distancia entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Consultar distancias entre A y B, y B y A
dist_AB = distancia(A, B)
dist_BA = distancia(B, A)
print("\nDistancias:")
print(f"Distancia entre A y B: {dist_AB}")
print(f"Distancia entre B y A: {dist_BA}")

# Determinar el punto más lejano del origen
dist_A = distancia(A, D)
dist_B = distancia(B, D)
dist_C = distancia(C, D)
mas_lejano = max((dist_A, "A"), (dist_B, "B"), (dist_C, "C"))
print("\nPunto más lejano del origen:")
print(f"El punto más lejano del origen es {mas_lejano[1]} con una distancia de {mas_lejano[0]}")

# Crear un rectángulo utilizando los puntos A y B
base = abs(B[0] - A[0])
altura = abs(B[1] - A[1])
area = base * altura
print("\nRectángulo:")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área: {area}")