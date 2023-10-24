import random
from src.ESTRUCTURA1.cPaciente import cPaciente
from src.ESTRUCTURA1.cPaciente import read_nombre
from src.ESTRUCTURA1.cPaciente import read_sintomas
from src.ESTRUCTURA1.TriageVoraz import TriageVoraz 
from src.ESTRUCTURA1.SalaEsperaVoraz import SalaEsperaVoraz 

def main() -> None:
  variable = input("elija que forma desea: ")
  turno = [2, 5, 1, 3]
  posibles_sintomas = read_sintomas()
  posibles_nombres = read_nombre()
  pacientes_entrantes = []

  if variable == 1: #se decide que estructura usar
    flag = 1
    lista_sala_espera = []

    while(flag == 1):
      
      for i in range(0, random.randint(0,5)):
        nuevo = cPaciente(random.choice(posibles_nombres), random.choices(posibles_sintomas, random.randint(1,5)))
        pacientes_entrantes.append(nuevo)

      cant_enfermeros = random.choice(turno)

      for i in range(0, cant_enfermeros):
        TriageVoraz(pacientes_entrantes[i],posibles_sintomas)
        SalaEsperaVoraz(pacientes_entrantes[i], lista_sala_espera)

      pacientes_entrantes= pacientes_entrantes[cant_enfermeros+1: len(pacientes_entrantes)-1]
      

if __name__ == "__main__":
  main()

