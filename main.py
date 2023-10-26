import random
from ESTRUCTURA2.CategorizacionVegana import Triage_tree, Tree_Node, Categorizacion
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera
from src.ESTRUCTURA2.cPaciente import cPaciente, read_sintomas, read_nombre


def main() -> None:

  turno = [2, 5, 1, 3]
  Posibles_Nombres = read_nombre()
  posibles_sintomas = read_sintomas()
  pacientes_entrantes = []

# variables auxiliares ESTRUCTURA2
  Primer_Nodo1 =Tree_Node(50, "consciente?")
  Primer_Nodo2 =Tree_Node(25, "respira?")
  Primer_Nodo3 =Tree_Node(15, "Tras abrir via?")
  Primer_Nodo4 =Tree_Node(20, "rojo")
  Primer_Nodo5 =Tree_Node(35, "Hemorragia grave")
  Primer_Nodo6 =Tree_Node(30, "rojo")
  Primer_Nodo7 =Tree_Node(40, "naranja")
  Primer_Nodo8 =Tree_Node(75, "camina?")
  Primer_Nodo9 =Tree_Node(60, "entiende?")
  Primer_Nodo10 =Tree_Node(55, "naranja")
  Primer_Nodo11 =Tree_Node(67, "traumatismo grave")
  Primer_Nodo12 =Tree_Node(65, "naranja")
  Primer_Nodo13 =Tree_Node(70, "amarillo")
  Primer_Nodo14 =Tree_Node(90, "dolor severo")
  Primer_Nodo15 =Tree_Node(80, "amarillo")
  Primer_Nodo16 =Tree_Node(100, "dolor leve")
  Primer_Nodo17 =Tree_Node(95, "verde")
  Primer_Nodo18 =Tree_Node(105, "azul")
  Arbolito = Triage_tree()
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo1)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo2)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo3)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo4)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo5)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo6)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo7)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo8)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo9)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo10)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo11)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo12)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo13)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo14)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo15)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo16)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo17)
  Arbolito.Recur_Insert(Arbolito.Root, Primer_Nodo18)

  flag = 1
    
  while(flag == 1):
    
    flag = 1
    lista_sala_espera = []

    while(flag == 1):

      for i in range(0, random.randint(0,5)):
        k = random.randint(1,5)
        nuevo = cPaciente(random.choice(Posibles_Nombres), random.sample(posibles_sintomas, k))
        pacientes_entrantes.append(nuevo)

      cant_enfermeros = random.choice(turno)
      i = 0
      while((len(pacientes_entrantes) > i) and (i != cant_enfermeros)):
        Categorizacion(Arbolito, pacientes_entrantes[i])
        i+=1
      Sala_De_Espera(pacientes_entrantes[0:cant_enfermeros],lista_sala_espera)
        

      pacientes_entrantes= pacientes_entrantes[cant_enfermeros+1: len(pacientes_entrantes)-1]


if __name__ == "__main__":
  main()