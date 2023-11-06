
import random
import csv
from src.ESTRUCTURA2.Exceptions import ExcepcionNodoVacio
from src.ESTRUCTURA2.cPaciente import cPaciente
class Tree_Node:
    def __init__(self, Peso:int, Pregunta):
        self.Pregunta = Pregunta
        self.Peso = Peso
        self.Left = None
        self.Right = None


class Triage_tree:

    def __init__(self, Root:Tree_Node = None):
        self.Root = Root

    def Recur_Insert(self, Nodo_actual:Tree_Node, node_i:Tree_Node):

        if not self.Root:
            self.Root = node_i
        elif int(node_i.Peso) < int(Nodo_actual.Peso):
            if Nodo_actual.Left:
                self.Recur_Insert(Nodo_actual.Left, node_i)
            else:
                Nodo_actual.Left = node_i
        else:
            if Nodo_actual.Right:
                self.Recur_Insert(Nodo_actual.Right, node_i)
            else:
                Nodo_actual.Right = node_i
            
def Categorizacion(arbol:Triage_tree) -> int:#clasificacion

    RndVector = [0,1,1,1,1,1] #Aca manejamos la probabilidad (1: derecha, 0: izquierda)

    if not arbol or not arbol.Root:  # preguntar nodo actual
        raise ExcepcionNodoVacio
    else:
      RND = random.choice(RndVector)
      if RND == 1: # Derecha
        return int(arbol.Root.Peso) + int(Categorizacion_recur(arbol.Root.Right, RndVector))
      else: # Izquierda
        return Categorizacion_recur(arbol.Root.Left, RndVector)
          
    
def Categorizacion_recur(Nodo: Tree_Node, RndVector:list) -> int:
    if not Nodo:
        return 0
    else:
      RND = random.choice(RndVector)
      if RND == 1: # Derecha
        return int(Nodo.Peso) + int(Categorizacion_recur(Nodo.Right, RndVector))
      else: # Izquierda
        return Categorizacion_recur(Nodo.Left, RndVector)
      
def leer_sintomas():
    condiciones_arch = []
    with open("SIntomas_nuevos.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            condiciones_arch.append(row)

    return condiciones_arch

def inicilizacion_Arbol():

    Arbol_binario = Triage_tree()

    condiciones_arch = leer_sintomas()
    for i in range(1, len(condiciones_arch)):
        Nuevo_Nodo = Tree_Node(condiciones_arch[i][1],condiciones_arch[i][0])
        Arbol_binario.Recur_Insert(Arbol_binario.Root, Nuevo_Nodo)
    return Arbol_binario

def TriageArbol(Paciente:cPaciente, Arbol:Triage_tree):

    PesoTotal = Categorizacion(Arbol)
    
    if PesoTotal > 0 and PesoTotal <= 55:
        Paciente.categoria = "rojo"
        Paciente.tiempoEspera = 0

    elif PesoTotal > 55 and PesoTotal <=110:
        Paciente.categoria = "naranja"
        Paciente.tiempoEspera = 10
    elif PesoTotal > 110 and PesoTotal <=177:
        Paciente.categoria = "amarillo"
        Paciente.tiempoEspera = 60
    elif PesoTotal > 177 and PesoTotal <= 215:
        Paciente.categoria = "verde"
        Paciente.tiempoEspera = 120
    else:
        Paciente.categoria = "azul"
        Paciente.tiempoEspera = 240
    
    print(Paciente.categoria)
    return PesoTotal