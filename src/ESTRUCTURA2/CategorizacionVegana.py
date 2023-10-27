
import random
import csv
class Tree_Node:
    def __init__(self, Peso, Pregunta):
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
            
def Categorizacion(nodo:Triage_tree):#clasificacion

    if not nodo:  # preguntar nodo actual
        return 0 #posible excepcion porque deberia haber un arbol, revisar
    else:
      RND = random.randint(0,1)
      if RND == 1: #si
        print("Esta ", nodo.Root.Pregunta)
        return nodo.Root.Peso + Categorizacion_recur(nodo.Root.Right)
      else: #no
        print("No esta", nodo.Root.Pregunta)
        return nodo.Root.Peso + Categorizacion_recur(nodo.Root.Left)
          
    
def Categorizacion_recur(Nodo: Tree_Node):
    if not Nodo:
        return 0
    else:
      RND = random.randint(0,1)
      if RND == 1: #si
        return Nodo.Peso + Categorizacion_recur(Nodo.Right)
      else: #no
        return Nodo.Peso + Categorizacion_recur(Nodo.Left)
      
def leer_sintomas():
    condiciones_arch = []
    with open(r"Archivos\Sintomas_nuevos.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            condiciones_arch.append(row)

    return condiciones_arch

def inicilizacion_Arbol():

    Arbol_binario = Triage_tree()

    condiciones_arch = leer_sintomas()
    for i in range(0, len(condiciones_arch)):
        Nuevo_Nodo= Tree_Node(condiciones_arch[i][1],condiciones_arch[i][0])
        Arbol_binario.Recur_Insert(Arbol_binario.Recur_Insert, Nuevo_Nodo)
    return Arbol_binario