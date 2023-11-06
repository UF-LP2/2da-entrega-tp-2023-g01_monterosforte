import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QSizePolicy
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt6.QtCore import Qt, QTimer
import random
from src.ESTRUCTURA2.cPaciente import cPaciente, read_nombre
from src.ESTRUCTURA2.Categorizacion import inicilizacion_Arbol, TriageArbol
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera, ExcepcionListaVacia
from src.ESTRUCTURA2.cSala import cSala

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
		self.PuntitosSMedico = []
		self.puntitosTotales = []

		### variables relacionadas a pacientes
		self.pacientesRecepcion = []
		self.seTriagearon = []
		self.Posibles_Nombres = read_nombre()
		self.Arbolito = inicilizacion_Arbol()
		self.PacEnCola = [] ### pacientes que va a manejar la sala de espera
		self.listaSalas = []



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
			self.AnchoSMedico = int((self.AnchoSEspera - 2*EspacioSEspera_SMedico)/self.cantSalasMedicos)  #DIBUJO SALAS DE MEDICOS
			self.AlturaSMedico = self.AnchoSMedico

			if self.AnchoSMedico > 70:
				self.AnchoSMedico = 70
				self.AlturaSMedico = 70

			XSMedico = XSEspera + EspacioSEspera_SMedico
			YSMedico = YSEspera - self.AlturaSMedico
			
			for i in range(0, self.cantSalasMedicos):

				self.painter.drawRect(int(XSMedico) + i*int(self.AnchoSMedico), int(YSMedico), int(self.AnchoSMedico), int(self.AlturaSMedico))
				sala = (cSala(True), int(XSMedico + (self.AnchoSMedico/2) + i*(self.AnchoSMedico)), int(YSMedico+ (self.AlturaSMedico/2)))
				if len(self.listaSalas) < self.cantSalasMedicos:
					self.listaSalas.append(sala)
			font = QFont("Arial", 12)
			font.setBold(True)
			font.setItalic(True)
			self.painter.setFont(font)
			self.painter.setPen(QColor(0,0,0))
			XContadorSE = XSEspera + self.AnchoSEspera/2
			YContadorSE = YSEspera + self.AlturaSEspera + 20
			self.painter.drawText(int(XContadorSE), int(YContadorSE), f"Cantidad en sala: {len(self.PuntitosSEspera)}")

			XContadorSR = XSRecepcion + self.AnchoSRecepcion/2
			YContadorSR = YSRecepcion + self.AlturaSRecepcion + 20
			self.painter.drawText(int(XContadorSR), int(YContadorSR), f"Cantidad en sala: {len(self.PuntitosRecepcion)}")

		if self.botonIniciarApretado:

			self.painter.setRenderHint(QPainter.RenderHint.Antialiasing)

			for i in range(0, len(self.PuntitosRecepcion)):
				XSRecepcion = int(self.width()/2 -self.AnchoPasillo - self.AnchoSRecepcion)
				YSRecepcion = int((self.height() + self.AlturaSEspera - self.AlturaSRecepcion)/2)

				XUSRecepcion = random.randint(XSRecepcion, int(XSRecepcion + self.AnchoSRecepcion)-10)
				YUSRecepcion = random.randint(YSRecepcion, int(YSRecepcion + self.AlturaSRecepcion)-10)
				
				#x, y, color = self.PuntitosRecepcion[i][0] , self.PuntitosRecepcion[i][1], self.PuntitosRecepcion[i][2]
				x, y, color = XUSRecepcion , YUSRecepcion, self.PuntitosRecepcion[i][2]
				self.painter.setBrush(QBrush(QColor(*color)))
				self.painter.drawEllipse(x, y, 10, 10)

			for i in range(0, len(self.PuntitosSEspera)):
				x, y, color = self.PuntitosSEspera[i][0], self.PuntitosSEspera[i][1], self.PuntitosSEspera[i][2]
				self.painter.setBrush(QBrush(QColor(*color)))
				self.painter.drawEllipse(x, y, 10, 10)
			
			for i in range(0, len(self.PuntitosSMedico)):
				x,y,color = self.PuntitosSMedico[i][0], self.PuntitosSMedico[i][1], self.PuntitosSMedico[i][2]
				self.painter.setBrush(QBrush(QColor(*color)))
				self.painter.drawEllipse(x, y, 10, 10)



		self.painter.end()


		
	def actualizarPacientes(self, CantEnfermeros:int):
		listita =[]

		for i in range(0, random.randint(0,CantEnfermeros)):
			listita.clear()
			nuevo = cPaciente(random.choice(self.Posibles_Nombres))
			self.pacientesRecepcion.append(nuevo)

			XSRecepcion = int(self.width()/2 -self.AnchoPasillo - self.AnchoSRecepcion)
			YSRecepcion = int((self.height() + self.AlturaSEspera - self.AlturaSRecepcion)/2)

			XUSRecepcion = random.randint(XSRecepcion, int(XSRecepcion + self.AnchoSRecepcion)-10)
			YUSRecepcion = random.randint(YSRecepcion, int(YSRecepcion + self.AlturaSRecepcion)-10)

			color = (200, 200, 200)
			listita.append(XUSRecepcion)
			listita.append(YUSRecepcion)
			listita.append(color)
			self.PuntitosRecepcion.append(listita.copy())
		

		self.update()


	def ActualizarPacientes_SalaEspera(self, CantEnfermeros):
		listita = []
		i = 0
		self.seTriagearon = []

		while(len(self.pacientesRecepcion) > i and i != CantEnfermeros):

			listita.clear()

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

			listita.append(XSEspera)
			listita.append(YSEspera)
			listita.append(color1)
			self.PuntitosSEspera.append(listita.copy())

			self.seTriagearon.append(self.pacientesRecepcion.pop(i))
			self.PuntitosRecepcion.pop(i)

			i += 1
		
		try:
			Sala_De_Espera(self.seTriagearon, self.PacEnCola, self.listaSalas, self.PuntitosSEspera, self.PuntitosSMedico)

			self.SimulacionTiempo(self.PacEnCola, self.PuntitosSEspera, self.listaSalas, self.PuntitosSMedico)
		except ExcepcionListaVacia as e:
			print(str(e))
		
		self.update()
	

	def SimulacionTiempo(self, listaSalaEspera:list[cPaciente], PuntitosSEspera: list, listaSalas: list, PuntitosSMedico: list):


		for i in range(0,len(listaSalaEspera)):
			listaSalaEspera[i].tiempoEspera -= 2
			if listaSalaEspera[i].tiempoEspera < 0:
				print("Se le acabo el tiempo. Categoria: ", listaSalaEspera[i].categoria)
				PuntitosSEspera[i][2] = (0, 0, 0)

		for i in range(0, len(listaSalas)):
			j=0
			if listaSalas[i][0].tiempoOcupado <= 0 and listaSalas[i][0].disponible == False:
				listaSalas[i][0].disponible = True
				print("Se jue")
				while( j<len(listaSalas) and j < len(PuntitosSMedico)):
					if i == PuntitosSMedico[j][3]:
						PuntitosSMedico.pop(j)
					j+=1

			elif listaSalas[i][0].disponible == False:
				listaSalas[i][0].tiempoOcupado -= 2
				
