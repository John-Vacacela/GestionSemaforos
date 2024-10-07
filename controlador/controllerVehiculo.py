from modelo.modelSemaforo import Semaforo
from modelo.modelCalle import Calle
from modelo.modelEstado import Estado
from vista.vistaCalles import vistaCalles
#from controlador.controllerVehiculo import controllerVehiculo
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QTimer

class controllerVehiculos:
    def __init__(self, vista: vistaCalles):
        self.vista = vista
        self.timer = QTimer()  # Crear un temporizador para el movimiento de los vehículos
        self.timer.timeout.connect(self.mover_carros_continuo)  # Conectar el temporizador al método de movimiento continuo
        self.direccion_actual = None  # Variable para almacenar la dirección actual de movimiento

    def iniciar_movimiento(self, direccion):
        
        self.direccion_actual = direccion  # Establecer la dirección actual de movimiento
        self.timer.start(50)  # Iniciar el temporizador con un intervalo de 100 ms (ajusta según la velocidad deseada)

    def detener_movimiento(self):
        
        self.timer.stop()  # Detener el temporizador

    def mover_carros_continuo(self):
    
        if self.direccion_actual == "horizontal":
            # Mover los carros hacia la derecha en la calle horizontal
            for i in range(len(self.vista.carros_horizontales)):
                self.vista.carros_horizontales[i] += 5  # Ajusta el incremento según la velocidad que desees
                if self.vista.carros_horizontales[i] > 500:  # Si el carro sale del borde, lo reseteas
                    self.vista.carros_horizontales[i] = -50
        elif self.direccion_actual == "vertical":
            # Mover los carros hacia abajo en la calle vertical
            for i in range(len(self.vista.carros_verticales)):
                self.vista.carros_verticales[i] -= 5  # Ajusta el incremento según la velocidad
                if self.vista.carros_verticales[i] < -50:  # Si el carro sale del borde, lo reseteas
                    self.vista.carros_verticales[i] = 500

        self.vista.update()  # Forzar redibujado para actualizar las posiciones



    
    
    