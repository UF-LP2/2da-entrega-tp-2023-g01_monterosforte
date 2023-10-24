from cPaciente import cPaciente
import random

NSalas = 5

def SalaEsperaVoraz(paciente: cPaciente, listaSalaEspera:list[cPaciente]):

    RNDCantSalasLibres = random.randint(0,NSalas)

    ### AGREGAR - Ordena directamente. T(n) = O(n^2)
    if paciente.categoria == "rojo":
        for i in len(listaSalaEspera):
            if listaSalaEspera[i].categoria == "naranja":
                listaSalaEspera.insert(i-1, paciente)  # O(n) REVISAR QUE EL INSERT FUNCIONE ASI
    else:
        for i in len(listaSalaEspera):
             if paciente.tiempoEspera < listaSalaEspera[i].tiempoEspera:
                listaSalaEspera.insert(i-1, paciente) # O(n)
    ###    

    ### Hace pasar a los pacientes. T(n) = O(n)
    if RNDCantSalasLibres < len(listaSalaEspera):
        listaSalaEspera = listaSalaEspera[RNDCantSalasLibres:(len(listaSalaEspera)-1)]
    else:
        listaSalaEspera = []
    ###

    ### Simulación de empeoramiento. T(n) = --
    RNDEmpeorar = random.randint(0, len(listaSalaEspera)-1)
    if listaSalaEspera[RNDEmpeorar].categoria == "azul":
        probabilidad = random.randint(0,100)
        if probabilidad == 50:
            listaSalaEspera[RNDEmpeorar].categoria == "verde"

    if listaSalaEspera[RNDEmpeorar].categoria == "verde":
        probabilidad = random.randint(0,70)
        if probabilidad == 35:
            listaSalaEspera[RNDEmpeorar].categoria == "amarillo"       

    if listaSalaEspera[RNDEmpeorar].categoria == "amarillo":
        probabilidad = random.randint(0,40)
        if probabilidad == 20:
            listaSalaEspera[RNDEmpeorar].categoria == "naranja"
                    
    if listaSalaEspera[RNDEmpeorar].categoria == "naranja":
        probabilidad = random.randint(0,10)
        if probabilidad == 5:
            listaSalaEspera[RNDEmpeorar].categoria == "rojo"
    ###
    
    ### Saco y vuelvo a colocar en orden al paciente que empeoró
    pacienteEmpeorado = listaSalaEspera.pop(i) # T(n) = O(1)
    
    ### AGREGAR - Ordena directamente. T(n) = O(n^2)
    if pacienteEmpeorado.categoria == "rojo":
        for i in len(listaSalaEspera):
            if listaSalaEspera[i].categoria == "naranja":
                listaSalaEspera.insert(i-1, pacienteEmpeorado)  # O(n)
    else:
        for i in len(listaSalaEspera):
             if paciente.tiempoEspera < listaSalaEspera[i].tiempoEspera:
                listaSalaEspera.insert(i-1, pacienteEmpeorado) # O(n)
    ###    
    ###
    