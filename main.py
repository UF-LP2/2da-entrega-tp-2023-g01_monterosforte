import random
from src.ESTRUCTURA2.Categorizacion import Triage_tree, Tree_Node, Categorizacion, inicilizacion_Arbol, leer_sintomas
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera
from src.ESTRUCTURA2.cPaciente import read_nombre, cPaciente
from src.ESTRUCTURA2.cSala import cSala


def main() -> None:

  # variables auxiliares

  turno = [2, 5, 1, 3]

  Posibles_Nombres = read_nombre()
  pacientes_entrantes = []

  Arbolito = inicilizacion_Arbol()
  
  NSalas = 10 #Así podemos cambiarlo más fácil
  listaSalas = []
  for i in range(0, NSalas): #Cargo la lista de salas. Inicialmente todas disponibles.
    sala = cSala(True)
    listaSalas.append(sala)

  flag = 1

  LimSalaEspera = 30
  lista_sala_espera = []

  while(flag == 1):

    for i in range(0, random.randint(0,5)):
      nuevo = cPaciente(random.choice(Posibles_Nombres))
      pacientes_entrantes.append(nuevo)

    cant_enfermeros = random.choice(turno) #Raro que en cada while cambie. vuelta de while = un turno distinto. Como q pasa muy rapido el tiempo
    i = 0

    while(len(pacientes_entrantes) > i and i != cant_enfermeros):
      PesoTotal = Categorizacion(Arbolito)

      #Aca iria el TRIAGE.

      i+=1

    Sala_De_Espera(pacientes_entrantes[0:cant_enfermeros],lista_sala_espera, listaSalas)
        
    SimulacionTiempo(lista_sala_espera)

    pacientes_entrantes = pacientes_entrantes[cant_enfermeros: len(pacientes_entrantes)]

    if len(lista_sala_espera) == LimSalaEspera:
      print("Sala ociosa/supera el limite")

def SimulacionTiempo(listaSalaEspera:list[cPaciente]):

  for i in range(0,len(listaSalaEspera)):
    listaSalaEspera[i].tiempoEspera -= 2
    if listaSalaEspera[i].tiempoEspera < 0:
      print("Se le acabo el tiempo. Categoria: ", listaSalaEspera[i].categoria)



if __name__ == "__main__":
  main()