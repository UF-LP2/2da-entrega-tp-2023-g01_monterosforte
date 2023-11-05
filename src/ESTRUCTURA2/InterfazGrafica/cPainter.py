from PyQt6.QtWidgets import QWidget, QSizePolicy
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush
from PyQt6.QtCore import Qt, QTimer
import random
from src.ESTRUCTURA2.cPaciente import cPaciente, read_nombre
from src.ESTRUCTURA2.Categorizacion import inicilizacion_Arbol, TriageArbol
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera, ExcepcionListaVacia

class cPainter(QWidget): #Va a dibujar el plano

	def __init__(self):
		super().__init__()

		### decidimos como funciona el tamanio de lo que dibujamos (salas)
		self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
		self.painter = QPainter()

		###creamos e inicializamos las variables que usaremos a continuacion

		self.planoGenerado = False
		self.botonIniciarApretado = False
		self.cantSalasMedicos = 0
		
		self.AlturaSEspera = 0
		self.AnchoSEspera = 0

		self.AlturaSMedico = 0 
		self.AnchoSMedico = 0

		self.AlturaSRecepcion = 0
		self.AnchoSRecepcion = 0

		self.AlturaPasillo = 0
		self.AnchoSRecepcion = 0

		self.PuntitosRecepcion = []
		self.PuntitosSEspera = []
		self.puntitosTotales = []

		### variables relacionadas a pacientes
		self.pacientesRecepcion = []
		self.Posibles_Nombres = read_nombre()
		self.Arbolito = inicilizacion_Arbol()
		LimSalaEspera = 30
		self.pacientesSEspera = [] ### pacientes que va a manejar la sala de espera
		CantidadEnfermeros = 0 # esto tiene que cambiar segun el ingreso de la Spinbox



	def paintEvent(self, event):

		self.painter.begin(self)
		self.painter.setPen(QPen(QColor(0,0,0), 1))
		self.painter.drawRect(0, 0, self.width()-10, self.height()-10)
		
		self.AlturaSEspera = self.height()/3 #QUINTA PARTE DEL WIDGET
		self.AnchoSEspera = self.width()/3

		self.AlturaSMedico = self.AnchoSEspera/15 #CUADRADO
		self.AnchoSMedico = self.AnchoSEspera/15

		self.AlturaSRecepcion = self.height()/4 
		self.AnchoSRecepcion = self.width()/4

		self.AlturaPasillo = self.height()/10
		self.AnchoPasillo = self.width()/10

		if self.planoGenerado:

			XSEspera = self.width()/2
			YSEspera = self.height()/2

			self.painter.drawRect(int(XSEspera), int(YSEspera), int(self.AnchoSEspera), int(self.AlturaSEspera)) #DIBUJO SALA DE ESPERA

			XPasillo = self.width()/2 - self.AnchoPasillo
			YPasillo = (self.height() + self.AlturaSEspera - self.AlturaPasillo)/2

			self.painter.drawRect(int(XPasillo), int(YPasillo), int(self.AnchoPasillo), int(self.AlturaPasillo)) #DIBUJO PASILLO

			XSRecepcion = XPasillo - self.AnchoSRecepcion
			YSRecepcion = (self.height() + self.AlturaSEspera - self.AlturaSRecepcion)/2

			self.painter.drawRect(int(XSRecepcion), int(YSRecepcion), int(self.AnchoSRecepcion), int(self.AlturaSRecepcion)) #DIBUJO SALA DE RECEPCION

			EspacioSEspera_SMedico = 15
			self.AnchoSMedico = int((self.AnchoSEspera - 2*EspacioSEspera_SMedico)/self.cantSalasMedicos)
			self.AlturaSMedico = self.AnchoSMedico

			if self.AnchoSMedico > 70:
				self.AnchoSMedico = 70
				self.AlturaSMedico = 70

			XSMedico = XSEspera + EspacioSEspera_SMedico
			YSMedico = YSEspera - self.AlturaSMedico
			
			for i in range(0, self.cantSalasMedicos):
				self.painter.drawRect(int(XSMedico) + i*int(self.AnchoSMedico), int(YSMedico), int(self.AnchoSMedico), int(self.AlturaSMedico))

		if self.botonIniciarApretado:

			self.painter.setRenderHint(QPainter.RenderHint.Antialiasing)

			for i in range(0, len(self.PuntitosRecepcion)):
				x, y, color = self.PuntitosRecepcion[i]
				self.painter.setBrush(QBrush(QColor(*color)))
				self.painter.drawEllipse(x, y, 10, 10)

			for i in range(0, len(self.PuntitosSEspera)):
				x, y, color = self.PuntitosSEspera[i]
				self.painter.setBrush(QBrush(QColor(*color)))
				self.painter.drawEllipse(x, y, 10, 10)



		self.painter.end()

	def actualizarPacientes(self, CantEnfermeros:int):

		for i in range(0, random.randint(0,CantEnfermeros)):
			nuevo = cPaciente(random.choice(self.Posibles_Nombres))
			self.pacientesRecepcion.append(nuevo)

			XSRecepcion = int(self.width()/2 -self.AnchoPasillo - self.AnchoSRecepcion)
			YSRecepcion = int((self.height() + self.AlturaSEspera - self.AlturaSRecepcion)/2)

			XUSRecepcion = random.randint(XSRecepcion, int(XSRecepcion + self.AnchoSRecepcion)-10)
			YUSRecepcion = random.randint(YSRecepcion, int(YSRecepcion + self.AlturaSRecepcion)-10)

			color = (200, 200, 200)
			self.PuntitosRecepcion.append((XUSRecepcion, YUSRecepcion, color))
		

		self.update()
	
	def ActualizarPacientes_SalaEspera(self, CantEnfermeros):

		i = 0
		while(len(self.pacientesRecepcion) > i and i != CantEnfermeros):
			TriageArbol(self.pacientesRecepcion[i], self.Arbolito)

			XSEspera = random.randint(int(self.width()/2), int(self.width()/2 + self.AnchoSEspera)-10)
			YSEspera = random.randint(int(self.height()/2), int(self.height()/2 + self.AlturaSEspera) -10)

			if self.pacientesRecepcion[i].categoria == "rojo":
				color1 = (255, 0, 0)
			elif self.pacientesRecepcion[i].categoria == "naranja":
				color1 = (255, 128, 0)
			elif self.pacientesRecepcion[i].categoria == "amarillo":
				color1 = (255, 255, 0)
			elif self.pacientesRecepcion[i].categoria == "verde":
				color1 = (0, 255, 0)
			elif self.pacientesRecepcion[i].categoria == "azul":
				color1 = (0, 0, 255)

			self.PuntitosSEspera.append((XSEspera, YSEspera, color1))

			if len(self.PuntitosRecepcion) > 0:
				self.PuntitosRecepcion.pop()

			i += 1
		
		self.update()
	
	def ActualizacionSEsepera_2(self, CantEnfermeros):
		try:
			Sala_De_Espera(self.pacientesRecepcion[0:CantEnfermeros],self.pacientesSEspera, listaSalas)
		except ExcepcionListaVacia as e:
			print(str(e))