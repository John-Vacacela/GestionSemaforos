import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QFrame
from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QColor, QRegion
from PyQt5.QtCore import Qt, QRect


class vistaCalles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión Semáforos")
        self.center()

        self.valorContador = QLabel("0", self)
        self.valorContador.move(20, 20)
        self.valorContador.setStyleSheet("font-size: 28px; color: white;")

        self.luzRojoH = QFrame(self)
        self.luzRojoH.setGeometry(175, 190, 10, 10)
        self.luzRojoH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 0, 0);"
        )

        self.luzAmarilloH = QFrame(self)
        self.luzAmarilloH.setGeometry(155, 190, 10, 10)
        self.luzAmarilloH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 128, 0);"
        )

        self.luzVerdeH = QFrame(self)
        self.luzVerdeH.setGeometry(135, 190, 10, 10)
        self.luzVerdeH.setStyleSheet(
            "border-radius: 5px; background-color: rgb(0, 128, 0);"
        )

        self.luzRojoV = QFrame(self)
        self.luzRojoV.setGeometry(190, 315, 10, 10)
        self.luzRojoV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 0, 0);"
        )

        self.luzAmarilloV = QFrame(self)
        self.luzAmarilloV.setGeometry(190, 335, 10, 10)
        self.luzAmarilloV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(128, 128, 0);"
        )

        self.luzVerdeV = QFrame(self)
        self.luzVerdeV.setGeometry(190, 355, 10, 10)
        self.luzVerdeV.setStyleSheet(
            "border-radius: 5px; background-color: rgb(0, 128, 0);"
        )

    def center(self):
        window_width = 500
        window_height = 500
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - window_width) // 2
        y = (screen.height() - window_height) // 2

        self.setGeometry(x, y, window_width, window_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        self.drawFondo(painter)
        self.drawCalle(painter)
        self.drawVereda(painter)
        self.drawLineas(painter)
        self.drawSemaforo(painter)
        painter.end()

    def drawFondo(self, painter):
        # Dibujar el fondo
        painter.setBrush(QBrush(QColor(0, 122, 110)))
        painter.drawRect(self.rect())

    def drawCalle(self, painter):
        # Dibujar las calles (rectángulos grises)
        painter.setBrush(QBrush(QColor(162, 161, 166)))  # Color gris para las calles
        painter.drawRect(0, 200, 500, 100)  # Calle horizontal
        painter.drawRect(200, 0, 100, 500)  # Calle vertical

    def drawVereda(self, painter):
        # Dibujar las veredas
        painter.setBrush(QBrush(QColor(219, 219, 219)))
        painter.drawRect(0, 175, 200, 25)  # Vereda izquierda 1 calle horizontal
        painter.drawRect(0, 300, 200, 25)  # Vereda derecha 1 calle horizontal
        painter.drawRect(175, 300, 25, 200)  # Vereda izquierda 1 calle vertical
        painter.drawRect(300, 300, 25, 200)  # Vereda derecha 1 calle vertical
        painter.drawRect(300, 175, 200, 25)  # Vereda izquierda 2 calle horizontal
        painter.drawRect(300, 300, 200, 25)  # Vereda derecha 2 calle horizontal
        painter.drawRect(175, 0, 25, 200)  # Vereda izquierda 2 calle vertical
        painter.drawRect(300, 0, 25, 200)  # Vereda derecha 2 calle vertical

    def drawLineas(self, painter):
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(0, 208, 212, 4)
        painter.drawRect(0, 288, 212, 4)
        painter.drawRect(208, 0, 4, 212)
        painter.drawRect(288, 0, 4, 212)
        painter.drawRect(288, 208, 212, 4)
        painter.drawRect(288, 288, 212, 4)
        painter.drawRect(208, 288, 4, 212)
        painter.drawRect(288, 288, 4, 212)

    def drawSemaforo(self, painter: QPainter):
        # Dibujar los semáforos
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(130, 185, 60, 20)  # Semáforo calle horizontal
        painter.drawRect(185, 310, 20, 60)  # Semaforo calle vertical
