from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera, Atender
from src.ESTRUCTURA2.cPaciente import cPaciente
import pytest
from src.ESTRUCTURA2.Exceptions import ExcepcionListaVacia
from src.ESTRUCTURA2.cSala import cSala


def test_Atender1(): #Lista PAR.
    pac1 = cPaciente("Juan", 1978, 123456, 8)
    pac1.categoria = "naranja"
    pac2 = cPaciente("a", 1975, 1234587,2)
    pac2.categoria = "naranja"
    pac3 = cPaciente("b", 1968,54568848,45)
    pac3.categoria ="azul"
    pac4 = cPaciente("c", 1989, 1231564, 0)
    pac4.categoria = "rojo"

    listaPacientes = []
    listaPacientes.append(pac1)
    listaPacientes.append(pac2)
    listaPacientes.append(pac3)
    listaPacientes.append(pac4)

    paciente = Atender(listaPacientes)

    assert paciente == pac4

def test_Atender2(): #Lista IMPAR.

    pac1 = cPaciente("a", 1987, 123456, 0)
    pac1.categoria = "rojo"
    pac2 = cPaciente("b", 4589,12354, 1)
    pac2.categoria = "naranja"
    pac3 = cPaciente("c", 456, 132465, 2)
    pac3.categoria = "amarillo"
    pac4 = cPaciente("d", 456,4548789, 3)
    pac4.categoria = "verde"
    pac5 = cPaciente("e",123,1256465, 4)
    pac5.categoria = "azul"

    listaPacientes = []
    listaPacientes.append(pac1)
    listaPacientes.append(pac2)
    listaPacientes.append(pac3)
    listaPacientes.append(pac4)
    listaPacientes.append(pac5)

    paciente = Atender(listaPacientes)
    assert paciente == pac1

def test_SalaDeEspera1(): #Obtiene lista VACIA.

    listaPacientes = [] 
    PacEnCola = []
    listaSalas = []
    listaPuntitos1 = []
    listaPuntitos2 = []


    with pytest.raises(ExcepcionListaVacia):
        Sala_De_Espera(listaPacientes, PacEnCola, listaSalas, listaPuntitos1, listaPuntitos2)
