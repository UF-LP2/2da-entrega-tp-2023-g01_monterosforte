from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpinBox, QLabel, QGridLayout, QComboBox, QSizePolicy

from src.ESTRUCTURA2.InterfazGrafica.cPainter import cPainter
from src.ESTRUCTURA2.cSala import cSala

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

        ### variables auxiliares
        self.listaSalas = []


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

        self.timer_EntradaPacientes = QTimer(self) #timer de entrada de pacientes a recepcion
        self.timer_Triage_SalaEspera = QTimer(self) #timer de pasaje de recepcion a sala de espera 
        self.timer_SalaEspera = QTimer(self)



    def generarPlano(self):
        self.planoHospital.PuntitosRecepcion.clear() 
        self.planoHospital.PuntitosSEspera.clear()

        self.planoHospital.planoGenerado = True
        self.planoHospital.botonIniciarApretado = False

        self.botonIniciar.setEnabled(True)
        self.botonPausar.setEnabled(False)

        cantNSalas = self.selectorNumSalas.value()
        self.planoHospital.cantSalasMedicos = cantNSalas


        for i in range(0, cantNSalas): #se crean las salas que van a ser manejadas en SalaEspera
            sala = cSala(True)
            self.listaSalas.append(sala)

        self.planoHospital.update()

    
    def generarSimulacion(self):#esta funcion ocurre al apretar el boton iniciar

        
        self.botonPausar.setEnabled(True)
        self.botonIniciar.setEnabled(False)
        self.botonGenerarPlano.setEnabled(False)

        self.planoHospital.botonIniciarApretado = True
        self.planoHospital.planoGenerado = True








        turnoString = self.selectorTurno.currentText() #Se traduce el turno a la cantidad de enfermeros
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
        self.timer_Triage_SalaEspera.start(3000)

        self.timer_SalaEspera.timeout.connect(lambda:self.planoHospital.ActualizacionSEsepera_2(self.CantActualEnfermeros, self.listaSalas))



    def generarPausa(self):
        self.botonPausar.setEnabled(False)
        self.botonGenerarPlano.setEnabled(True)
        self.timer_EntradaPacientes.stop()  # Detener el temporizador de recepcion
        self.timer_Triage_SalaEspera.stop() #Detener el temporizador de sala de espera
