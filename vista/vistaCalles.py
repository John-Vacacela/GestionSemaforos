from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QFrame
from PyQt5.QtGui import QPaintEvent, QPainter, QBrush, QColor, QRegion, QPolygon
from PyQt5.QtCore import Qt, QRect, QPoint


class vistaCalles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión Semáforos")
        self.resize(500, 500)
        self.carros_horizontales = [100, 30]  # Posiciones en x
        self.carros_verticales = [420, 330]  # Posiciones en y
        self.initUI()

    def initUI(self):
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

    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        self.drawFondo(painter)
        self.drawCalle(painter)
        self.drawVereda(painter)
        self.drawLineas(painter)
        self.drawSemaforo(painter)
        self.drawVehiculos(painter)
        painter.end()

    def drawFondo(self, painter):
        # Dibujar el fondo
        painter.setBrush(QBrush(QColor(81, 185, 72)))
        painter.drawRect(self.rect())

    def drawCalle(self, painter):
        # Dibujar las calles
        painter.setBrush(QBrush(QColor(108, 109, 111)))  # Color gris para las calles
        painter.drawRect(0, 200, 500, 100)  # Calle horizontal
        painter.drawRect(200, 0, 100, 500)  # Calle vertical

    def drawVereda(self, painter):
        # Dibujar las veredas
        painter.setBrush(QBrush(QColor(180, 181, 183)))
        painter.drawRect(0, 175, 200, 25)  # Vereda izquierda 1 calle horizontal
        painter.drawRect(0, 300, 200, 25)  # Vereda derecha 1 calle horizontal
        painter.drawRect(175, 300, 25, 200)  # Vereda izquierda 1 calle vertical
        painter.drawRect(300, 300, 25, 200)  # Vereda derecha 1 calle vertical
        painter.drawRect(300, 175, 200, 25)  # Vereda izquierda 2 calle horizontal
        painter.drawRect(300, 300, 200, 25)  # Vereda derecha 2 calle horizontal
        painter.drawRect(175, 0, 25, 200)  # Vereda izquierda 2 calle vertical
        painter.drawRect(300, 0, 25, 200)  # Vereda derecha 2 calle vertical

    def drawLineas(self, painter):
        painter.setBrush(QBrush(QColor(251, 210, 86)))
        painter.drawRect(0, 208, 212, 4)
        painter.drawRect(0, 288, 212, 4)
        painter.drawRect(208, 0, 4, 212)
        painter.drawRect(288, 0, 4, 212)
        painter.drawRect(288, 208, 212, 4)
        painter.drawRect(288, 288, 212, 4)
        painter.drawRect(208, 288, 4, 212)
        painter.drawRect(288, 288, 4, 212)

    def drawSemaforo(self, painter):
        # Dibujar los semáforos
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(130, 185, 60, 20)  # Semáforo calle horizontal
        painter.drawRect(185, 310, 20, 60)  # Semaforo calle vertical

    def drawVehiculos(self, painter):
        NEGRO = QColor(0, 0, 0)
        ROJO = QColor(255, 0, 0)
        AZUL = QColor(0, 0, 255)
        GRIS = QColor(169, 169, 169)

        # Dibujar los carros en la calle horizontal según sus posiciones actuales
        for x_pos in self.carros_horizontales:
            self.drawVehiculoHorizontal(painter, ROJO, AZUL, NEGRO, GRIS, x_pos, 240)

        # Dibujar los carros en la calle vertical según sus posiciones actuales
        for y_pos in self.carros_verticales:
            self.drawVehiculoVertical(painter, ROJO, AZUL, NEGRO, GRIS, 240, y_pos)

    def drawVehiculoHorizontal(
        self,
        painter,
        color_cuerpo,
        color_techo,
        color_ruedas,
        color_detalle_ruedas,
        x,
        y,
    ):
        # Cuerpo del carro (horizontal)
        painter.setBrush(QBrush(color_cuerpo))
        painter.drawRect(x, y, 50, 20)

        # Techo del carro
        polygon = QPolygon(
            [
                QPoint(x + 5, y),
                QPoint(x + 20, y - 15),
                QPoint(x + 30, y - 15),
                QPoint(x + 45, y),
            ]
        )
        painter.setBrush(QBrush(color_techo))
        painter.drawPolygon(polygon)

        # Ruedas
        painter.setBrush(QBrush(color_ruedas))
        painter.drawEllipse(QPoint(x + 10, y + 20), 5, 5)
        painter.drawEllipse(QPoint(x + 40, y + 20), 5, 5)

        # Detalles de las ruedas
        painter.setBrush(QBrush(color_detalle_ruedas))
        painter.drawEllipse(QPoint(x + 10, y + 20), 2, 2)
        painter.drawEllipse(QPoint(x + 40, y + 20), 2, 2)

    def drawVehiculoVertical(
        self,
        painter,
        color_cuerpo,
        color_techo,
        color_ruedas,
        color_detalle_ruedas,
        x,
        y,
    ):
        # Cuerpo del carro (vertical)
        painter.setBrush(QBrush(color_cuerpo))
        painter.drawRect(x, y, 20, 50)

        # Techo del carro (vertical)
        polygon = QPolygon(
            [
                QPoint(x, y + 5),
                QPoint(x - 15, y + 20),
                QPoint(x - 15, y + 30),
                QPoint(x, y + 45),
            ]
        )
        painter.setBrush(QBrush(color_techo))
        painter.drawPolygon(polygon)

        # Ruedas (vertical)
        painter.setBrush(QBrush(color_ruedas))
        painter.drawEllipse(QPoint(x + 20, y + 10), 5, 5)
        painter.drawEllipse(QPoint(x + 20, y + 40), 5, 5)

        # Detalles de las ruedas
        painter.setBrush(QBrush(color_detalle_ruedas))
        painter.drawEllipse(QPoint(x + 20, y + 10), 2, 2)
        painter.drawEllipse(QPoint(x + 20, y + 40), 2, 2)
