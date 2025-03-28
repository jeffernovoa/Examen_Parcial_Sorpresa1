import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "I"
        elif self.x < 0 and self.y > 0:
            return "II"
        elif self.x < 0 and self.y < 0:
            return "III"
        elif self.x > 0 and self.y < 0:
            return "IV"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.y == 0 and self.x != 0:
            return "Eje X"
        else:
            return "Origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)