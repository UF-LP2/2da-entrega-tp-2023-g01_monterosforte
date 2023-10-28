from src.ESTRUCTURA2.Categorizacion import Categorizacion, Categorizacion_recur, Tree_Node, Triage_tree, inicilizacion_Arbol, leer_sintomas
from src.ESTRUCTURA2.cPaciente import read_nombre

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