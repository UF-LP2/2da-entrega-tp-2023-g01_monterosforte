from src.ESTRUCTURA2.Categorizacion import Categorizacion, Categorizacion_recur, Tree_Node, Triage_tree, inicilizacion_Arbol, leer_sintomas, TriageArbol
from src.ESTRUCTURA2.cPaciente import read_nombre, cPaciente
from src.ESTRUCTURA2.Exceptions import ExcepcionNodoVacio
import pytest

def test_leer_nombres():
    Posibles_nombres = read_nombre()

    assert Posibles_nombres[len(Posibles_nombres)-1] == ['Cal']
    assert Posibles_nombres[1] == ['Ferrel']

def test_leer_sintomas():
    auxiliar =leer_sintomas()
    assert auxiliar[0][0] == 'Condiciones'
    assert auxiliar[1][1] == '50'
    assert auxiliar[1][0] == 'Consciente'
    
def test_inicializacion_arbol():
    Arbolito = inicilizacion_Arbol()

    assert Arbolito

def test_categorizacion(): # Mando nodo vacio.

    nodo = Triage_tree()

    with pytest.raises(ExcepcionNodoVacio):
        Categorizacion(nodo)

def test_TriageArbol():
    Arbolito = inicilizacion_Arbol()
    pacientes = []
    for i in range(0,100):
        pac = cPaciente("")
        pacientes.append(pac)
    
    for i in range(0,100):
        PesoTotal = TriageArbol(pacientes[i], Arbolito)

        if PesoTotal > 0 and PesoTotal <= 55:
            assert pacientes[i].categoria == "rojo"
            assert pacientes[i].tiempoEspera == 1
        elif PesoTotal > 55 and PesoTotal <=110:
            assert pacientes[i].categoria == "naranja"
            assert pacientes[i].tiempoEspera == 10
        elif PesoTotal > 110 and PesoTotal <=177:
            assert pacientes[i].categoria == "amarillo"
            assert pacientes[i].tiempoEspera == 60
        elif PesoTotal > 177 and PesoTotal <= 215:
            assert pacientes[i].categoria == "verde"
            assert pacientes[i].tiempoEspera == 120
        else:
            assert pacientes[i].categoria == "azul"
            assert pacientes[i].tiempoEspera == 240