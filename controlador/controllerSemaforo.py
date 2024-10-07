from modelo.modelSemaforo import Semaforo
from modelo.modelCalle import Calle
from modelo.modelEstado import Estado
from vista.vistaCalles import vistaCalles
from PyQt5.QtWidgets import QFrame


class controllerSemaforo:
    def __init__(self, vista: vistaCalles):
        self.vista = vista
        self.semaforoH = Semaforo(Estado.ROJO, Calle.HORIZONTAL)
        self.semaforoV = Semaforo(Estado.VERDE, Calle.VERTICAL)

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
