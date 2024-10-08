from modelo.modelCalle import Calle
from modelo.modelEstado import Estado
from vista.vistaCalles import vistaCalles
from modelo.modelVehiculo import Vehiculo
from PyQt5.QtCore import QTimer


class controllerVehiculo:
    def __init__(self, vista: vistaCalles, semaforoH, semaforoV, timer_delay=16):
        self.vista = vista
        self.semaforoH = semaforoH
        self.semaforoV = semaforoV
        self.timer_delay = timer_delay
        self.vehiculoH1 = Vehiculo(Calle.HORIZONTAL, 140, 240)
        self.vehiculoH2 = Vehiculo(Calle.HORIZONTAL, 40, 240)
        self.vehiculoV1 = Vehiculo(Calle.VERTICAL, 240, 500)
        self.vehiculoV2 = Vehiculo(Calle.VERTICAL, 240, 600)
        self.vehiculos = [
            self.vehiculoH1,
            self.vehiculoH2,
            self.vehiculoV1,
            self.vehiculoV2,
        ]
        self.actualizar_vista()
        self.start_timer()

    def start_timer(self):
        self.timer = QTimer(self.vista)
        self.timer.timeout.connect(self.mover_carros)
        self.timer.start(self.timer_delay)

    def mover_carros(self):
        for vehiculo in self.vehiculos:
            if vehiculo.calle == Calle.HORIZONTAL:
                if (
                    self.semaforoH.estado == Estado.VERDE
                    or self.semaforoH.estado == Estado.AMARILLO
                ):
                    vehiculo.mover_horizontal()
                    self.actualizar_vista()

                    if vehiculo.x > 500:
                        vehiculo.x = -50
            else:
                if (
                    self.semaforoV.estado == Estado.VERDE
                    or self.semaforoV.estado == Estado.AMARILLO
                ):
                    vehiculo.mover_vertical()
                    self.actualizar_vista()

                    if vehiculo.y < -50:
                        vehiculo.y = 500

    def actualizar_vista(self):
        self.vista.actualizarPosiciones(
            [self.vehiculoH1.x, self.vehiculoH2.x],
            [self.vehiculoV1.y, self.vehiculoV2.y],
        )
