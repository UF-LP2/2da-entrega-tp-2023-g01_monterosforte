from src.ESTRUCTURA2.SalaEsperaDyC import Sala_De_Espera, Atender, Max_prioridad
from src.ESTRUCTURA2.cPaciente import cPaciente
import Archivos

def test_Atender():
    pac1 = cPaciente("Juan", 1978, 123456, 8)
    pac1.categoria = "naranja"
    pac2 = cPaciente("a", 1975, 1234587,2)
    pac2.categoria = "naranja"
    pac3 = cPaciente("b", 1968,54568848,45)
    pac3.categoria ="azul"
    pac4 = cPaciente("c", 1989, 1231564, 0)
    pac4.categoria = "azul"

    listaPacientes:list[cPaciente] = []
    listaPacientes.append(pac1)
    listaPacientes.append(pac2)
    listaPacientes.append(pac3)
    listaPacientes.append(pac4)

    paciente = Atender(listaPacientes)

    #assert paciente == pac4
    assert paciente == pac1
    #assert paciente == pac2
    #assert paciente == pac3


