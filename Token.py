listaTK = []

class Tk:
    
    def __init__(self, id, lex, tipo, fila, col):
        self.id = id
        self.lex = lex
        self.tipo = tipo
        self.fila = fila 
        self.col = col
        listaTK.append([id, lex, tipo, fila, col])     

    def MostrarTK(self):
        for tok in listaTK:
            print(tok)

        '''for i in range(len(listaTK)-4):
            print(f"id : {listaTK[i]} lex: {listaTK[i+1]} tipo: {listaTK[i+2]} fila: {listaTK[i+3]} columna: {listaTK[i+4]}")
            i = i+4 '''

