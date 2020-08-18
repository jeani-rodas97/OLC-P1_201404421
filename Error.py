class ERROR:
    def __init__(self, error, descripcion, fila, col):
        self.error = error
        self.descripcion = descripcion
        self.fila = fila 
        self.col = col 
        self.listaERROR = [error, descripcion, fila, col]
        print("Llega a lista de errores")