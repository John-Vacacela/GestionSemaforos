class Vehiculo:
    def __init__(self, calle, x=0, y=0):
        self.calle = calle
        self.x = x
        self.y = y
        self.velocidad = 2

    def mover_horizontal(self):
        self.x += self.velocidad

    def mover_vertical(self):
        self.y -= self.velocidad
