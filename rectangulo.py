class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1  # Primer punto (esquina inferior izquierda)
        self.punto2 = punto2  # Segundo punto (esquina superior derecha)

    def base(self):
        # La base es la diferencia en las coordenadas x
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        # La altura es la diferencia en las coordenadas y
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        # El área es base * altura
        return self.base() * self.altura()