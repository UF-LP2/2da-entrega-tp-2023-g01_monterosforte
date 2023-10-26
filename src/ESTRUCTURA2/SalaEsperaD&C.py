from src.ESTRUCTURA2.cPaciente import cPaciente
import random

NSALAS = 20 
PROB_EMPEORAR = 10 

def Sala_De_Espera(listaPacientes, Pac_En_Cola:list[cPaciente]):

    Aux_Salas_Libres = random.randint(0, NSALAS)
    Pac_En_Cola.append(listaPacientes)

    for i in range(0, Aux_Salas_Libres):
        Paciente = Atender(Pac_En_Cola)
        Pac_En_Cola - Paciente
    
     ### Simulación de empeoramiento. T(n) = --
    i = random.randint(0, len(Pac_En_Cola)-1)
    if Pac_En_Cola[i].categoria == "azul":
        probabilidad = random.randint(0,100)
        if probabilidad == 50:
            Pac_En_Cola[i].categoria == "verde"

    if Pac_En_Cola[i].categoria == "verde":
        probabilidad = random.randint(0,70)
        if probabilidad == 35:
            Pac_En_Cola[i].categoria == "amarillo"       

    if Pac_En_Cola[i].categoria == "amarillo":
        probabilidad = random.randint(0,40)
        if probabilidad == 20:
            Pac_En_Cola[i].categoria == "naranja"
                    
    if Pac_En_Cola[i].categoria == "naranja":
        probabilidad = random.randint(0,10)
        if probabilidad == 5:
            Pac_En_Cola[i].categoria == "rojo"
    ###
    
def Atender(Pac_En_Cola:cPaciente):
    if len(Pac_En_Cola) == 0:
        algo = 0
    elif len(Pac_En_Cola) == 1:
        return Pac_En_Cola
    elif len(Pac_En_Cola) == 2:
        return Max_prioridad(Pac_En_Cola[0], Pac_En_Cola[1])
    else:
        return Max_prioridad(Atender(Pac_En_Cola[0:len(Pac_En_Cola)/2]) , Atender(Pac_En_Cola[len(Pac_En_Cola)/2+1:len(Pac_En_Cola)-1]))



def Max_prioridad(Primer_pac:cPaciente, Segundo_pac:cPaciente): #esta funcion devuelve el paciente con mayor prioridad
    
    if Primer_pac.categoria == "rojo" and Segundo_pac.categoria != "rojo":
        return Primer_pac
    elif Primer_pac.categoria != "rojo" and Segundo_pac.categoria == "rojo":
        return Segundo_pac
    else:
        if Primer_pac.tiempoEspera > Segundo_pac.tiempoEspera: #consideramos el tiempo que han estado esperando los pacientes como un criterio
                                                               
            return Segundo_pac
        else:
            return Primer_pac #aca tambien esta considerado que si tienen el mismo tiempo de espera restante se elije arbitrariamente uno de los dos