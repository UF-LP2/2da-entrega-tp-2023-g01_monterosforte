import random
from src.ESTRUCTURA2.Categorizacion import Triage_tree, Tree_Node, Categorizacion, inicilizacion_Arbol, leer_sintomas, TriageArbol
from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera
from src.ESTRUCTURA2.cPaciente import read_nombre, cPaciente
from src.ESTRUCTURA2.cSala import cSala
from src.ESTRUCTURA2.Exceptions import ExcepcionListaVacia


def main() -> None:

  # variables auxiliares

  cont = 0

  iRojo = iNaranja = iAmarillo = iVerde = iAzul = 0

  Posibles_Nombres = read_nombre()
  pacientes_entrantes = []

  Arbolito = inicilizacion_Arbol()
  
  NSalas = 4 ###
  listaSalas = []
  for i in range(0, NSalas): ###
    sala = cSala(True)
    listaSalas.append(sala)

  flag = 1

  LimSalaEspera = 30
  lista_sala_espera = []
  cant_enfermeros = [2, 5, 1, 3]
  turno_Actual = 0
  while(flag == 1):

     #Raro que en cada while cambie. vuelta de while = un turno distinto. Como q pasa muy rapido el tiempo
    if cont == 1000:    #simulamos que cada 1000 iteraciones del while, cambia el turno
      print("Cambio de turnos")
      if turno_Actual == 3:
        turno_Actual = 0
      else:
        turno_Actual += 1
      cont=0


    for i in range(0, random.randint(0,cant_enfermeros[turno_Actual])):
      nuevo = cPaciente(random.choice(Posibles_Nombres))
      pacientes_entrantes.append(nuevo)

    i = 0

    while(len(pacientes_entrantes) > i and i != cant_enfermeros[turno_Actual]):
      TriageArbol(pacientes_entrantes[i], Arbolito)
      if pacientes_entrantes[i].categoria == "rojo":
        iRojo +=1
      elif pacientes_entrantes[i].categoria == "naranja":
        iNaranja +=1
      elif pacientes_entrantes[i].categoria == "amarillo":
        iAmarillo +=1
      elif pacientes_entrantes[i].categoria == "verde":
        iVerde +=1
      else:
        iAzul +=1
      i+=1
    try:
      Sala_De_Espera(pacientes_entrantes[0:cant_enfermeros[turno_Actual]],lista_sala_espera, listaSalas)
    except ExcepcionListaVacia as e:
        print(str(e))
    
    SimulacionTiempo(lista_sala_espera, listaSalas)

    pacientes_entrantes = pacientes_entrantes[cant_enfermeros[turno_Actual]: len(pacientes_entrantes)]

    if len(lista_sala_espera) == LimSalaEspera:
      print("Sala ociosa/supera el limite")
      raise Exception

def SimulacionTiempo(listaSalaEspera:list[cPaciente], listaSalas: list[cSala]):

  for i in range(0,len(listaSalaEspera)):
    paciente = listaSalaEspera[i]
    paciente.tiempoEspera -= 2
    if paciente.tiempoEspera < 0:
      print("Se le acabo el tiempo. Categoria: ", paciente.categoria)

  for i in range(0, len(listaSalas)):
    if listaSalas[i].disponible == False:
      listaSalas[i].tiempoOcupado -= 2
      if listaSalas[i].tiempoOcupado == 0:
        listaSalas[i].disponible = True



if __name__ == "__main__":
  main()