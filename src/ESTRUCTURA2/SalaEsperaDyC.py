from src.ESTRUCTURA2.cPaciente import cPaciente
from src.ESTRUCTURA2.cSala import cSala
from src.ESTRUCTURA2.Exceptions import ExcepcionListaVacia

import random

PROB_EMPEORAR = 10 

def Sala_De_Espera(listaPacientes, Pac_En_Cola:list[cPaciente], listaSalas:list[cSala]):


    if not listaSalas or not listaPacientes:
        raise ExcepcionListaVacia
    
    Pac_En_Cola.append(listaPacientes)

    for i in range(0, len(listaSalas)):
        if listaSalas[i].disponible:
            try:
                Paciente = Atender(Pac_En_Cola)
                Pac_En_Cola.remove(Paciente)
            except ValueError:
                print("Error: No se encuentra el paciente en la sala de espera")
            except ExcepcionListaVacia as e:
                print(str(e))
            listaSalas[i].disponible = False
    
    SimulacionEmpeoramiento(Pac_En_Cola)



def Atender(Pac_En_Cola:cPaciente) -> cPaciente:
    if len(Pac_En_Cola) == 0:
        raise ExcepcionListaVacia
    elif len(Pac_En_Cola) == 1:
        return Pac_En_Cola[0]
    elif len(Pac_En_Cola) == 2:
        return Max_prioridad(Pac_En_Cola[0], Pac_En_Cola[1])
    
    return Max_prioridad(Atender(Pac_En_Cola[0:int(len(Pac_En_Cola)/2)]), Atender(Pac_En_Cola[int(len(Pac_En_Cola)/2):int(len(Pac_En_Cola))]))



def Max_prioridad(Primer_pac:cPaciente, Segundo_pac:cPaciente) -> cPaciente: #esta funcion devuelve el paciente con mayor prioridad
    
    if Primer_pac.categoria == "rojo" and Segundo_pac.categoria != "rojo":
        return Primer_pac
    elif Primer_pac.categoria != "rojo" and Segundo_pac.categoria == "rojo":
        return Segundo_pac
    else:
        if Primer_pac.tiempoEspera > Segundo_pac.tiempoEspera:
                                                               
            return Segundo_pac
        else:
            return Primer_pac #aca tambien esta considerado que si tienen el mismo tiempo de espera restante se elije arbitrariamente uno de los dos
        
def SimulacionEmpeoramiento(Pac_En_Cola: list[cPaciente]):
    i = random.randint(0, len(Pac_En_Cola)-1)
    paciente = cPaciente(Pac_En_Cola[i])
    if paciente.categoria == "azul":
        probabilidad = random.randint(0,100)
        if probabilidad == 50:
            paciente.categoria == "verde"

    if paciente.categoria == "verde":
        probabilidad = random.randint(0,70)
        if probabilidad == 35:
            paciente.categoria == "amarillo"       

    if paciente.categoria == "amarillo":
        probabilidad = random.randint(0,40)
        if probabilidad == 20:
            paciente.categoria == "naranja"
                    
    if paciente.categoria == "naranja":
        probabilidad = random.randint(0,10)
        if probabilidad == 5:
            paciente.categoria == "rojo"