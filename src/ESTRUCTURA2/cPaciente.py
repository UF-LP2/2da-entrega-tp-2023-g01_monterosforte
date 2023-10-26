class cPaciente:
    
    def __init__(self, Fecha_nac, nombre, lista_sintomas, DNI, tiempoEspera = 0): #la lista de sintomas tendria el mas importante primero
        self.Fecha_nac = Fecha_nac
        self.nombre = nombre
        self.lista_sintomas = lista_sintomas
        self.categoria = "blanco"
        self.DNI = DNI
        self.tiempoEspera = tiempoEspera