from cPaciente import cPaciente
import random
class Tree_Node:
    def __init__(self, valor):
        self.valor = valor
        self.Left = None
        self.Right = None


class Triage_tree:

    def __init__(self, Root:Tree_Node = None):
        self.Root = Root

    def Recur_Insert(self, node:Tree_Node, value):

        if not self.Root:
            self.Root = Tree_Node(value)
        elif value < node.valor:
            if node.Left:
                self.Recur_Insert(node.Left, value)
            else:
                node.Left = Tree_Node(value)
        else:
            if node.Right:
                self.Recur_Insert(node.Right, value)
            else:
                node.Right = Tree_Node(value)
            
def TriageArbol(nodo:Triage_tree, paciente: cPaciente):

    if not nodo.Root.Left and not nodo.Root.Right:
        if nodo.Root.valor == 50: # Arreglar
            paciente.categoria = "rojo"
            return
        if nodo.Root.valor == 34: # Arreglar
            paciente.categoria == "naranja"
        if nodo.Root.valor == 34: # Arreglar
            paciente.categoria == "amarillo"
        if nodo.Root.valor == 34: # Arreglar
            paciente.categoria == "verde"
        if nodo.Root.valor == 34: # Arreglar
            paciente.categoria == "azul"


    RND = random.randint(0,1)
    if RND == 1: # Si
        return TriageArbol(nodo.Root.Right, paciente)
    else: # No
        return TriageArbol(nodo.Root.Left, paciente)
    


