from modelo.modelSemaforo import Semaforo
from modelo.modelCalle import Calle
from modelo.modelEstado import Estado
from vista.vistaCalles import vistaCalles
from modelo.modelVehiculo import Vehiculo


# from controlador.controllerVehiculo import controllerVehiculo
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QTimer


class controllerVehiculos:
    def __init__(self, vista: vistaCalles):
        self.vista = vista
        self.timer_horizontal = QTimer()  # Temporizador para vehículos horizontales
        self.timer_vertical = QTimer()  # Temporizador para vehículos verticales

        # Conectar los temporizadores a sus respectivos métodos de movimiento continuo
        self.timer_horizontal.timeout.connect(self.mover_carros_horizontales)
        self.timer_vertical.timeout.connect(self.mover_carros_verticales)

        # Crear instancias de Vehiculo para los carros horizontales y verticales

        self.vehiculos_horizontales = [Vehiculo(100, 240, 5, "horizontal"), Vehiculo(30, 240, 5, "horizontal")]
        self.vehiculos_verticales = [Vehiculo(240, 420, 5, "vertical"), Vehiculo(240, 330, 5, "vertical")]

    def iniciar_movimiento(self, direccion, time):
        if direccion == "horizontal":
            self.timer_horizontal.start(
                time
            )  # Iniciar el temporizador para los vehículos horizontales
        elif direccion == "vertical":
            self.timer_vertical.start(
                time
            )  # Iniciar el temporizador para los vehículos verticales


    def detener_movimiento(self, direccion):
        if direccion == "horizontal":
            self.timer_horizontal.stop()  # Detener el temporizador de los vehículos horizontales
        elif direccion == "vertical":
            self.timer_vertical.stop()  # Detener el temporizador de los vehículos verticales

    def mover_carros_horizontales(self):
        for vehiculo in self.vehiculos_horizontales:
            vehiculo.mover()  # Actualiza la posición del vehículo horizontal

            self.vista.carros_horizontales = [vehiculo.x for vehiculo in self.vehiculos_horizontales]  # Actualiza las posiciones en la vista

            self.vista.carros_horizontales = [
                vehiculo.x for vehiculo in self.vehiculos_horizontales
            ]  # Actualiza las posiciones en la vista
        self.vista.update()  # Forzar redibujado para actualizar las posiciones

    def mover_carros_verticales(self):
        for vehiculo in self.vehiculos_verticales:
            vehiculo.mover()  # Actualiza la posición del vehículo vertical
            self.vista.carros_verticales = [vehiculo.y for vehiculo in self.vehiculos_verticales]  # Actualiza las posiciones en la vista
        self.vista.update()  # Forzar redibujado para actualizar las posiciones
