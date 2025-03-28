import math

# Crear los puntos
puntos = {
    "A": (2, 3),
    "B": (5, 5),
    "C": (-3, -1),
    "D": (0, 0)
}

# Imprimir los puntos
print("Puntos:")
for nombre, coordenadas in puntos.items():
    print(f"{nombre}: {coordenadas}")

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
    return "Eje"

# Consultar cuadrantes
print("\nCuadrantes:")
for nombre in ["A", "C", "D"]:
    print(f"{nombre} pertenece al cuadrante: {cuadrante(puntos[nombre])}")

# Función para calcular un vector entre dos puntos
def vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

# Consultar vectores AB y BA
AB = vector(puntos["A"], puntos["B"])
BA = vector(puntos["B"], puntos["A"])
print("\nVectores:")
print(f"Vector AB: {AB}")
print(f"Vector BA: {BA}")

# Función para calcular la distancia entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Consultar distancias entre A y B, y B y A
dist_AB = distancia(puntos["A"], puntos["B"])
print("\nDistancias:")
print(f"Distancia entre A y B: {dist_AB}")
print(f"Distancia entre B y A: {dist_AB}")  # Es la misma, no es necesario calcularla dos veces

# Determinar el punto más lejano del origen
distancias = {nombre: distancia(coord, puntos["D"]) for nombre, coord in puntos.items()}
mas_lejano = max(distancias.items(), key=lambda x: x[1])
print("\nPunto más lejano del origen:")
print(f"El punto más lejano del origen es {mas_lejano[0]} con una distancia de {mas_lejano[1]}")

# Crear un rectángulo utilizando los puntos A y B
base = abs(puntos["B"][0] - puntos["A"][0])
altura = abs(puntos["B"][1] - puntos["A"][1])
area = base * altura
print("\nRectángulo:")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área: {area}")