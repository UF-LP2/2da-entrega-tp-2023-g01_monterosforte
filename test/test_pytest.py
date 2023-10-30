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
    Paciente = cPaciente("a", 123, 123456)
    PesoTotal = TriageArbol(Paciente, Arbolito)

    if PesoTotal > 0 and PesoTotal <= 55:
         assert Paciente.categoria == "rojo"
         assert Paciente.tiempoEspera == 0
    elif PesoTotal > 55 and PesoTotal <=110:
         assert Paciente.categoria == "naranja"
         assert Paciente.tiempoEspera == 10
    elif PesoTotal > 110 and PesoTotal <=177:
         assert Paciente.categoria == "amarillo"
         assert Paciente.tiempoEspera == 60
    elif PesoTotal > 177 and PesoTotal <= 215:
         assert Paciente.categoria == "verde"
         assert Paciente.tiempoEspera == 120
    else:
         assert Paciente.categoria == "azul"
         assert Paciente.tiempoEspera == 240