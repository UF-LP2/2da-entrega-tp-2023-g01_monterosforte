class ExcepcionListaVacia(Exception):

    def __init__(self, mensaje = "Error: La lista se encuentra vacia."):
        super().__init__(mensaje)

class ExcepcionNodoVacio(Exception):
    def __init__(self, mensaje= "Error: No se recibio ningun nodo raiz."):
        super().__init__(mensaje)
