import sys
from PyQt5.QtWidgets import QApplication
from controlador.controllerContador import controllerContador
from vista.vistaCalles import vistaCalles


def main():
    app = QApplication(sys.argv)
    ventana = vistaCalles()
    ventana.show()
    cContador = controllerContador(ventana)
    cContador.start_timer()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
