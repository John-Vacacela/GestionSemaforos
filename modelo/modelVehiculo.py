# modelo/modelVehiculo.py
class Vehiculo:
    def __init__(self, x, y, velocidad, direccion):
        self.x = x  # Posición inicial en x
        self.y = y  # Posición inicial en y
        self.velocidad = velocidad  # Velocidad del vehículo
        self.direccion = (
            direccion  # Dirección del movimiento ("horizontal" o "vertical")
        )

    def mover(self):
        if self.direccion == "horizontal":
            self.x += self.velocidad
            if self.x > 500:  # Reiniciar si sale por la derecha
                self.x = -50
        elif self.direccion == "vertical":
            self.y -= self.velocidad
            if self.y < -50:  # Reiniciar si sale por la parte superior
                self.y = 500
