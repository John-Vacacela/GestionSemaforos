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
        painter.end()

    def drawCalle(self, painter):
        painter.setPen(Qt.NoPen)
        # Dibujar las calles (rectángulos grises)
        painter.setBrush(QBrush(QColor(128, 128, 128)))  # Color gris para las calles
        painter.drawRect(200, -10, 100, 510)  # Calle vertical
        painter.drawRect(-10, 200, 510, 100) # Calle horizontal

    def drawSemaforo(self, painter):
        painter.setPen(Qt.NoPen)
        # Dibujar los semáforos
    
