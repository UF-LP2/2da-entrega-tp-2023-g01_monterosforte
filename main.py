import random
from ESTRUCTURA2.CategorizacionVegana import Triage_tree, Tree_Node, Categorizacion, inicilizacion_Arbol
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera
from src.ESTRUCTURA2.cPaciente import cPaciente, read_sintomas, read_nombre


def main() -> None:

  # variables auxiliares
  turno = [2, 5, 1, 3]
  Posibles_Nombres = read_nombre()
  posibles_sintomas = read_sintomas()
  pacientes_entrantes = []
  Arbolito = inicilizacion_Arbol()
  flag = 1
  #comienza el ciclo, tal vez habria que agregar una forma de pararlo
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