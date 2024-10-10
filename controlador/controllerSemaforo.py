from modelo.modelSemaforo import Semaforo
from modelo.modelCalle import Calle
from modelo.modelEstado import Estado
from vista.vistaCalles import vistaCalles
from controlador.controllerVehiculo import controllerVehiculos

# from controlador.controllerVehiculo import controllerVehiculo
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QTimer


class controllerSemaforo:
    def __init__(self, vista: vistaCalles):
        self.vista = vista
        self.semaforoH = Semaforo(Estado.ROJO, Calle.HORIZONTAL)
        self.semaforoV = Semaforo(
            Estado.VERDE, Calle.VERTICAL
        )  # Controlador de vehículos
        self.cVehiculos = controllerVehiculos(self.vista)

        # Crear un temporizador para actualizar el estado de los vehículos y semáforos
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_vehiculos)
        self.timer.start(200)  # Actualiza el estado cada segundo (ajustable)

    def mover_vehiculos(self):
        # Verifica si el semáforo horizontal está en verde
        if (
            self.semaforoH.estado == Estado.VERDE
            or self.semaforoH.estado == Estado.AMARILLO
        ):
            self.cVehiculos.iniciar_movimiento(
                "horizontal", 45
            )  # Iniciar movimiento horizontal
        elif (
            self.semaforoH.estado == Estado.ROJO
            and 95 <= self.cVehiculos.vehiculos_horizontales[0].x <= 130
        ):
            self.cVehiculos.detener_movimiento("horizontal")
        else:
            self.cVehiculos.iniciar_movimiento("horizontal", 20)

        # Verifica si el semáforo vertical está en verde
        if (
            self.semaforoV.estado == Estado.VERDE
            or self.semaforoV.estado == Estado.AMARILLO
        ):
            self.cVehiculos.iniciar_movimiento("vertical", 45)
        elif (
            self.semaforoV.estado == Estado.ROJO
            and 395 <= self.cVehiculos.vehiculos_verticales[0].y <= 430
        ):
            self.cVehiculos.detener_movimiento("vertical")
        else:
            self.cVehiculos.iniciar_movimiento("vertical", 20)

    def cambiar_colores(self):
        if self.semaforoH.estado == Estado.VERDE:
            self.semaforoH.cambiar_estado()
            return

        if self.semaforoV.estado == Estado.VERDE:
            self.semaforoV.cambiar_estado()
            return

        self.semaforoH.cambiar_estado()
        self.semaforoV.cambiar_estado()

    def establecer_colores(self):
        self.resetear_colores()

        if self.semaforoH.estado == Estado.ROJO:
            self.establecer_rojo(self.vista.luzRojoH)
        elif self.semaforoH.estado == Estado.AMARILLO:
            self.establecer_amarillo(self.vista.luzAmarilloH)
        else:
            self.establecer_verde(self.vista.luzVerdeH)

        if self.semaforoV.estado == Estado.ROJO:
            self.establecer_rojo(self.vista.luzRojoV)
        elif self.semaforoV.estado == Estado.AMARILLO:
            self.establecer_amarillo(self.vista.luzAmarilloV)
        else:
            self.establecer_verde(self.vista.luzVerdeV)

    def resetear_colores(self):
        self.vista.luzRojoH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 0, 0);"
        )
        self.vista.luzAmarilloH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 128, 0);"
        )
        self.vista.luzVerdeH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(0, 128, 0);"
        )

        self.vista.luzRojoV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 0, 0);"
        )
        self.vista.luzAmarilloV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 128, 0);"
        )
        self.vista.luzVerdeV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(0, 128, 0);"
        )

    def establecer_rojo(self, luz):
        luz.setStyleSheet(
            f"border-radius: 5px; background-color: {Estado.RGB.get(Estado.ROJO)};"
        )

    def establecer_amarillo(self, luz):
        luz.setStyleSheet(
            f"border-radius: 5px; background-color: {Estado.RGB.get(Estado.AMARILLO)};"
        )

    def establecer_verde(self, luz):
        luz.setStyleSheet(
            f"border-radius: 5px; background-color: {Estado.RGB.get(Estado.VERDE)};"
        )
