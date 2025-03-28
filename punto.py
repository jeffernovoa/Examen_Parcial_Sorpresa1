import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        if self.x == 0:
            return "El punto está sobre el eje Y."
        if self.y == 0:
            return "El punto está sobre el eje X."
        if self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        if self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        if self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        return otro_punto.x - self.x, otro_punto.y - self.y

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
