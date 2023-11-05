from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpinBox, QLabel, QGridLayout, QComboBox, QSizePolicy

from src.ESTRUCTURA2.InterfazGrafica.cPainter import cPainter
from src.ESTRUCTURA2.cPaciente import cPaciente, read_nombre
from src.ESTRUCTURA2.Categorizacion import inicilizacion_Arbol

class cHospitalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.altura = 600
        self.ancho = 1600
        self.ejex = 100
        self.ejey = 100


        ######## Inicializacion de variables de Triage

        self.turnoString =""
        self.Posibles_Nombres = read_nombre()
        #self.pacientesRecepcion = []
        self.Arbolito = inicilizacion_Arbol()
        LimSalaEspera = 30
        lista_sala_espera = [] ### pacientes que va a manejar la sala de espera
        CantidadEnfermeros = 0 # esto tiene que cambiar segun el ingreso de la Spinbox
        self.cantNSalas = 0  # aqui se almacenan la cantidad de salas para usar en funcion SalaEsperaDyC, se le carga el valor de la spinbox al apretar [generar plano]

        ########

        self.setGeometry(self.ejex, self.ejey, self.ancho, self.altura)
        self.setWindowTitle('Salas de Espera')

        ###creamos los botones, labels, etc
        self.labelNumSalas = QLabel("Cantidad de salas:")
        self.selectorNumSalas = QSpinBox()
        self.selectorNumSalas.setMaximum(15)
        self.selectorNumSalas.setMinimum(1)

        self.botonGenerarPlano = QPushButton()
        self.botonGenerarPlano.setGeometry(90, 90, 20, 15)
        self.botonGenerarPlano.setText("GENERAR PLANO DEL HOSPITAL")

        self.labelTurno = QLabel("Seleccione turno:")
        self.selectorTurno = QComboBox()
        self.selectorTurno.addItem("23 a 6 hs")
        self.selectorTurno.addItem("6 a 10 hs")
        self.selectorTurno.addItem("10 a 16 hs")
        self.selectorTurno.addItem("16 a 23 hs")

        self.botonIniciar = QPushButton()
        self.botonIniciar.setGeometry(90,90,20,15)
        self.botonIniciar.setText("INICIAR")
        self.botonIniciar.setEnabled(False)

        self.botonPausar = QPushButton()
        self.botonPausar.setGeometry(90, 90, 20, 15)
        self.botonPausar.setText("PAUSAR")
        self.botonPausar.setEnabled(False)


        self.planoHospital = cPainter()

        layout1 = QGridLayout()
        layout1.addWidget(self.planoHospital)

        ###


        # Agregamos botones y labels
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

        self.timer1 = QTimer(self)


    def generarPlano(self):

        self.planoHospital.planoGenerado = True
        self.planoHospital.botonIniciarApretado = False

        self.botonIniciar.setEnabled(True)
        self.botonPausar.setEnabled(False)

        self.cantNSalas = self.selectorNumSalas.value()
        self.planoHospital.cantSalasMedicos = self.cantNSalas
        self.turnoString = self.selectorTurno.currentText()
        

        self.planoHospital.update()

    
    def generarSimulacion(self):

        self.planoHospital.puntitos.clear() 
        self.botonPausar.setEnabled(True)

        self.planoHospital.botonIniciarApretado = True
        self.planoHospital.planoGenerado = True















        self.timer1.timeout.connect(self.planoHospital.actualizarPacientes)
        self.timer1.start(1000)

    def generarPausa(self):
        self.timer1.stop()  # Detener el temporizador anterior
        self.planoHospital.puntitos.clear() 