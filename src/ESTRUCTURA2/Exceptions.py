class ExcepcionListaVacia(Exception):

    def __init__(self, mensaje = "Error: La lista se encuentra vacia."):
        super().__init__(mensaje)
