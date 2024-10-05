import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class vistaCalles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 700, 500, 500)
        self.setWindowTitle('Gestión Semáforos')
        self.center()

    def center(self):
        # Obtiene el rectángulo de la pantalla y lo usa para mover la ventana al centro
        centroPantalla = QDesktopWidget().availableGeometry().center()
        vistaC = self.frameGeometry()
        vistaC.moveCenter(centroPantalla)
        self.move(vistaC.topLeft()) 
    
    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawCalle(painter)
        self.drawSemaforo(painter)
        painter.end()

    def drawCalle(self, painter):
        painter.setPen(Qt.NoPen)
        # Dibujar las calles (rectángulos grises)
        painter.setBrush(QBrush(Qt.gray))  # Color gris para las calles
        painter.drawRect(200, -10, 100, 510)  # Calle vertical
        painter.drawRect(-10, 200, 510, 100) # Calle horizontal

    def drawSemaforo(self, painter):
        # Dibujar los semáforos
        painter.setBrush(QBrush(Qt.black)) 
        painter.drawRect(130, 210, 60, 20)
        painter.drawRect(210, 315, 20, 60)

        painter.setBrush(QBrush(Qt.gray))
        # Dibujamos las luces de los semaforos
        painter.drawEllipse(175, 214, 10, 10)
        painter.drawEllipse(155, 214, 10, 10)
        painter.drawEllipse(135, 214, 10, 10)

        painter.drawEllipse(215, 320, 10, 10)
        painter.drawEllipse(215, 340, 10, 10)
        painter.drawEllipse(215, 360, 10, 10)


