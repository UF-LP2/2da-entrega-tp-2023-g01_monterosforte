from src.ESTRUCTURA2.cPaciente import cPaciente
from src.ESTRUCTURA2.cSala import cSala
from src.ESTRUCTURA2.Exceptions import ExcepcionListaVacia


import random


def Sala_De_Espera(listaPacientes:list[cPaciente], Pac_En_Cola: list[cPaciente], listaSalas:list, PuntitosSEspera:list, PuntitosSMedico: list):

    if not listaSalas:
        raise ExcepcionListaVacia
    
    i=0

    while(i != len(listaPacientes)):
        Pac_En_Cola.append(listaPacientes[i])

        i+=1

    i = 0

    while(i<len(listaSalas) and len(Pac_En_Cola) > 0):
        listita = []
        if listaSalas[i][0].disponible == True:
            try:
                Paciente = Atender(Pac_En_Cola)
                aux = Pac_En_Cola.index(Paciente)
                
                x = listaSalas[i][1] # X #al atender al paciente se mueve el puntito a adentro
                y = listaSalas[i][2] # Y #de la sala de espera correspondiente
                color = PuntitosSEspera[aux][2]
                enSala = i
                listita.append(x)
                listita.append(y)
                listita.append(color)
                listita.append(enSala)

                PuntitosSMedico.append(listita.copy())
                PuntitosSEspera.remove(PuntitosSEspera[aux])
                Pac_En_Cola.remove(Paciente)
            except ValueError:
                print("Error: No se encuentra el paciente en la sala de espera")
            except ExcepcionListaVacia as e:
                print(str(e))

            listaSalas[i][0].disponible = False
            listaSalas[i][0].tiempoOcupado = 4
        i += 1
    


    if len(Pac_En_Cola) >= 1:
        SimulacionEmpeoramiento(Pac_En_Cola, PuntitosSEspera)
        SimulacionAzules(Pac_En_Cola, PuntitosSEspera)



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
        
def SimulacionEmpeoramiento(Pac_En_Cola: list[cPaciente], PuntitosSEspera):
    
    #paciente = random.choice(Pac_En_Cola)
    i = random.randint(0, len(Pac_En_Cola)-1)

    if Pac_En_Cola[i].categoria == "azul":
        probabilidad = random.randint(0,100)
        if probabilidad == 50:
            Pac_En_Cola[i].categoria == "verde"
            PuntitosSEspera[i][2] = (0, 255, 0)
            

    if Pac_En_Cola[i].categoria == "verde":
        probabilidad = random.randint(0,70)
        if probabilidad == 35:
            Pac_En_Cola[i].categoria == "amarillo"
            PuntitosSEspera[i][2] = (255, 255, 0)       

    if Pac_En_Cola[i].categoria == "amarillo":
        probabilidad = random.randint(0,40)
        if probabilidad == 20:
            Pac_En_Cola[i].categoria == "naranja"
            PuntitosSEspera[i][2] = (255, 128, 0)
                    
    if Pac_En_Cola[i].categoria == "naranja":
        probabilidad = random.randint(0,10)
        if probabilidad == 5:
            Pac_En_Cola[i].categoria == "rojo"
            PuntitosSEspera[i][2] = (255, 0, 0)
    
def SimulacionAzules(Pac_En_Cola: list[cPaciente], PuntitosSEspera:list):
    if len(Pac_En_Cola) >= 25:
        i= 0
        cont = 0
        RND = random.randint(1,2)
        while(i < len(Pac_En_Cola) and cont != RND):
            if Pac_En_Cola[i].categoria == "azul":
                Pac_En_Cola.pop(i)
                PuntitosSEspera.pop(i)
                cont += 1
            i+=1
