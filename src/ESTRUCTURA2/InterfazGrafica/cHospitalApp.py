from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpinBox, QLabel, QGridLayout, QComboBox, QSizePolicy

from src.ESTRUCTURA2.InterfazGrafica.cPainter import cPainter


class cHospitalApp(QMainWindow):
    CantActualEnfermeros= 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.altura = 600
        self.ancho = 1600
        self.ejex = 100
        self.ejey = 100

        self.botonPausarApretado = False

        self.setGeometry(self.ejex, self.ejey, self.ancho, self.altura)
        self.setWindowTitle('SIMULACION')

        ###creamos los botones, labels, etc
        self.labelNumSalas = QLabel("Cantidad de salas:")
        self.labelNumSalas.setStyleSheet('background-color: rgb(173, 216, 230); color: black; font-weight: bold; font-size: 11pt;')
        self.labelNumSalas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selectorNumSalas = QSpinBox()
        self.selectorNumSalas.setMaximum(15)
        self.selectorNumSalas.setMinimum(1)
        self.selectorNumSalas.setStyleSheet('color: black; font-size: 11pt;')

        self.botonGenerarPlano = QPushButton()
        self.botonGenerarPlano.setGeometry(90, 90, 20, 15)
        self.botonGenerarPlano.setText("GENERAR PLANO DEL HOSPITAL")
        self.botonGenerarPlano.setStyleSheet('color: black; font-weight: bold; font-size: 11pt;')

        self.labelTurno = QLabel("Seleccione turno:")
        self.labelTurno.setStyleSheet('background-color: rgb(173, 216, 230); color: black; font-weight: bold; font-size: 11pt;')
        self.labelTurno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selectorTurno = QComboBox()
        self.selectorTurno.addItem("23 a 6 hs")
        self.selectorTurno.addItem("6 a 10 hs")
        self.selectorTurno.addItem("10 a 16 hs")
        self.selectorTurno.addItem("16 a 23 hs")
        self.selectorTurno.setStyleSheet('color: black; font-size: 11pt;')

        self.botonIniciar = QPushButton()
        self.botonIniciar.setGeometry(90,90,20,15)
        self.botonIniciar.setText("INICIAR")
        self.botonIniciar.setEnabled(False)
        self.botonIniciar.setStyleSheet('color: black; font-weight: bold; font-size: 11pt;')

        self.botonPausar = QPushButton()
        self.botonPausar.setGeometry(90, 90, 20, 15)
        self.botonPausar.setText("TERMINAR")
        self.botonPausar.setEnabled(False)
        self.botonPausar.setStyleSheet('color: black; font-weight: bold; font-size: 11pt;')


        self.planoHospital = cPainter()
        self.planoHospital.setMinimumSize(400,300)

        #Agregamos a layouts
        layout1 = QGridLayout()
        layout1.addWidget(self.planoHospital)

        layout2 = QVBoxLayout()

        espacio = QWidget()
        espacio.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        layout2.addWidget(espacio)

        layout2.addWidget(self.labelTurno)
        layout2.addWidget(self.selectorTurno)

        layout2.addWidget(espacio)

        layout2.addWidget(self.labelNumSalas)
        layout2.addWidget(self.selectorNumSalas)

        layout2.addWidget(espacio)


        layout2.addWidget(self.botonGenerarPlano)
        layout2.addWidget(self.botonIniciar)
        layout2.addWidget(self.botonPausar)

        layout2.addWidget(espacio)

        layoutGral = QHBoxLayout()
        layoutGral.addLayout(layout1)
        layoutGral.addLayout(layout2)

        container = QWidget()
        container.setLayout(layoutGral)

        self.setCentralWidget(container)

        # CONEXION CON FUNCIONES

        self.botonGenerarPlano.clicked.connect(self.generarPlano)
        self.botonIniciar.clicked.connect(self.generarSimulacion)
        self.botonPausar.clicked.connect(self.generarPausa)

        self.timer_EntradaPacientes = QTimer(self)
        self.timer_Triage_SalaEspera = QTimer(self)


    def generarPlano(self): #Esta funcion ocurre al apretar el boton generar plano de hospital.
        self.planoHospital.PuntitosRecepcion.clear() 
        self.planoHospital.PuntitosSEspera.clear()

        self.planoHospital.planoGenerado = True
        self.planoHospital.botonIniciarApretado = False

        self.botonIniciar.setEnabled(True)
        self.botonPausar.setEnabled(False)

        cantNSalas = self.selectorNumSalas.value()
        self.planoHospital.cantSalasMedicos = cantNSalas

        self.planoHospital.update()

    
    def generarSimulacion(self): #Esta funcion ocurre al apretar el boton iniciar.
        self.botonPausar.setEnabled(True)
        self.botonIniciar.setEnabled(False)
        self.botonGenerarPlano.setEnabled(False)

        self.planoHospital.botonIniciarApretado = True
        self.planoHospital.planoGenerado = True

        turnoString = self.selectorTurno.currentText() #Se traduce el turno a la cantidad de enfermeros.
        if turnoString == "23 a 6 hs":
            self.CantActualEnfermeros = 1
        elif turnoString == "6 a 10 hs":
            self.CantActualEnfermeros = 2
        elif turnoString == "10 a 16 hs":
            self.CantActualEnfermeros = 5
        elif turnoString == "16 a 23 hs":
            self.CantActualEnfermeros = 3

        self.timer_EntradaPacientes.timeout.connect(lambda:self.planoHospital.actualizarPacientes(self.CantActualEnfermeros))
        self.timer_EntradaPacientes.start(1000)
        
        self.timer_Triage_SalaEspera.timeout.connect(lambda:self.planoHospital.ActualizarPacientes_SalaEspera(self.CantActualEnfermeros))
        self.timer_Triage_SalaEspera.start(1000)

    def generarPausa(self):
        self.timer_EntradaPacientes.stop()  # Detener el temporizador de recepcion.
        self.timer_Triage_SalaEspera.stop() #Detener el temporizador de sala de espera.
