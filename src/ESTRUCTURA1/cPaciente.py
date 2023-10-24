import random
import csv

def read_nombre():
    nombres = []
    with open(r".\Nombres.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            nombres.append(row)
    return nombres

def read_sintomas():
    sintomas = []
    with open(r".\Sintomas.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            sintomas.append(row)
    return sintomas


class cPaciente:
    
    def __init__(self, nombre, lista_sintomas, Fecha_nac = random.randint(1923, 2023), DNI=random.randint(11111111, 99999999), tiempoEspera = 0): #La lista de sintomas tendria el mas importante primero
        self.Fecha_nac = Fecha_nac
        self.nombre = nombre
        self.lista_sintomas = lista_sintomas
        self.categoria = "blanco"
        self.DNI = DNI
        self.tiempoEspera = tiempoEspera

  