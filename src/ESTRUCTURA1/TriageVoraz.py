from cPaciente import cPaciente

def TriageVoraz(paciente:cPaciente, lista_sintomas):
    for i in range(0, len(lista_sintomas)):
        for j in range(0, len(paciente.lista_sintomas)):

            if i<6 and paciente.lista_sintomas[j] == lista_sintomas[i]:
                paciente.categoria = "rojo"

            elif i>=6 and i<12 and paciente.lista_sintomas[j]  == lista_sintomas[i]:
                paciente.categoria = "naranja"
                paciente.tiempoEspera = 10

            elif i>=12 and i<18 and paciente.lista_sintomas[j]  == lista_sintomas[i]:
                paciente.categoria = "amarillo"
                paciente.tiempoEspera = 60

            elif i>=18 and i<24 and paciente.lista_sintomas[j]  == lista_sintomas[i]:
                paciente.categoria = "verde"
                paciente.tiempoEspera = 120
            else:
                paciente.categoria = "azul"
                paciente.tiempoEspera = 240
