import sys
from PyQt6.QtWidgets import QApplication
from src.ESTRUCTURA2.InterfazGrafica.cHospitalApp import cHospitalApp 

def main():
    app = QApplication(sys.argv)
    ventana = cHospitalApp()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()