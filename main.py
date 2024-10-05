import sys
from PyQt5.QtWidgets import QApplication
from vista.vistaCalles import vistaCalles 

def main():
    app = QApplication(sys.argv)  
    ventana = vistaCalles()        
    ventana.show()                 
    sys.exit(app.exec_())          

if __name__ == '__main__':
    main()  