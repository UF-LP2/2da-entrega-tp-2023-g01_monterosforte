from src.ESTRUCTURA2.cPaciente import cPaciente
import random
class Tree_Node:
    def __init__(self, valor, Pregunta):
        self.Pregunta = Pregunta
        self.valor = valor
        self.Left = None
        self.Right = None


class Triage_tree:

    def __init__(self, Root:Tree_Node = None):
        self.Root = Root

    def Recur_Insert(self, node:Tree_Node, node_i:Tree_Node):

        if not self.Root:
            self.Root = node_i
        elif node_i.valor < node.valor:
            if node.Left:
                self.Recur_Insert(node.Left, node_i)
            else:
                node.Left = node_i
        else:
            if node.Right:
                self.Recur_Insert(node.Right, node_i)
            else:
                node.Right = node_i
            
def Categorizacion(nodo:Triage_tree, paciente: cPaciente):#clasificacion

    if not nodo.Root.Left and not nodo.Root.Right:# preguntar nodo actual
        if nodo.Root.valor == 20 or nodo.Root.valor == 30:
            paciente.categoria = "rojo"
        if nodo.Root.valor == 40 or nodo.Root.valor == 55 or nodo.Root.valor == 65:
            paciente.categoria == "naranja"
        if nodo.Root.valor == 70 or nodo.Root.valor == 80: 
            paciente.categoria == "amarillo"
        if nodo.Root.valor == 95: 
            paciente.categoria == "verde"
        if nodo.Root.valor == 105: 
            paciente.categoria == "azul"

    RND = random.randint(0,1)
    if RND == 1: # Si
        return Categorizacion(nodo.Root.Right, paciente)
    else: # No
        return Categorizacion(nodo.Root.Left, paciente)
    