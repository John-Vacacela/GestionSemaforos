from PyQt5.QtCore import QTimer
from controlador.controllerSemaforo import controllerSemaforo
from modelo.modelContador import Contador
from vista.vistaCalles import vistaCalles


class controllerContador:
    def __init__(self, vista: vistaCalles, timer_delay=400):
        self.vista = vista
        self.timer_delay = timer_delay
        self.contador = Contador()
        self.cSemaforo = controllerSemaforo(self.vista)
        self.cSemaforo.establecer_colores()

    def start_timer(self):
        self.timer = QTimer(self.vista)
        self.timer.timeout.connect(self.timeout)
        self.timer.start(self.timer_delay)

    def timeout(self):
        self.contador.incrementar()
        self.vista.valorContador.setText(str(self.contador.valor))
        self.vista.valorContador.adjustSize()

        if self.contador.valor == 15:
            self.cSemaforo.cambiar_colores()
            self.cSemaforo.establecer_colores()
        elif self.contador.valor == 22:
            self.cSemaforo.cambiar_colores()
            self.cSemaforo.establecer_colores()
            self.contador.resetear()
