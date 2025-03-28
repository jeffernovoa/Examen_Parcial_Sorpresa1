import math

class Rectangulo:
    def __init__(self, punto_inicial=(0, 0), punto_final=(0, 0)):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final[0] - self.punto_inicial[0])

    def altura(self):
        return abs(self.punto_final[1] - self.punto_inicial[1])

    def area(self):
        return self.base() * self.altura()

# Ejemplo de uso
if __name__ == "__main__":
    rect = Rectangulo((1, 2), (4, 6))
    print("Base:", rect.base())
    print("Altura:", rect.altura())
    print("Área:", rect.area())