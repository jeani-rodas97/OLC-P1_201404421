from Token import Tkn
from Error import ERROR

listaLex = []
class RMT:
    
    def __init__(self, TextoRMT):
        self.TextoRMT = TextoRMT
        estado = 0
        lexema = ""
        fila = 1
        columna = 0 

        i = 0
        while i < len(TextoRMT):
            caracter = TextoRMT[i]
            if (estado == 0):
                lexema = ""
                if ((caracter == '*')|(caracter == '/')|(caracter == '+')|(caracter == '-')|(caracter == '(')|(caracter == ')')):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 5
                elif (caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                elif (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 1
                elif (caracter == '\n'):
                    columna = 0
                    fila +=1
                    i+=1
                    estado = 0
                elif (caracter.isspace()):
                    lexema += caracter
                    columna += 1 
                    i+=1
                    estado = 0 
                else:
                    lexema += caracter
                    columna += 1
                    ERROR(lexema, "Caracter desconocido", fila, columna)
                    i+=1
                    estado = 0
            
            elif (estado == 1):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 1
                elif (caracter == '.'):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 2
                else:
                    listaLex.append("Numero")
                    Tkn(1, lexema, "Numero", fila, columna)
                    estado = 0
                

            elif (estado == 2):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    ERROR(lexema, "Error sintactico, falto numero despues del punto.", fila, columna)
                    estado = 0

            elif (estado == 3):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    listaLex.append("Numero")
                    Tkn(1, lexema, "Numero", fila, columna)
                    estado = 0 

            elif (estado == 4):
                if (caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                elif (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                elif (caracter == '_'):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                else:
                    listaLex.append("Variable")
                    Tkn(4, lexema, "Variable", fila, columna)
                    estado = 0

            elif (estado == 5):
                listaLex.append(lexema)
                Tkn(5, lexema, "Signo", fila, columna)
                estado = 0

            else: 
                print("Nose que hacer")
                Tkn.MostrarTK(self)

        
        #self.AnalizadorSintac()
        self.Path(TextoRMT)
        ERROR.MostrarError(self)

    def Parentesis(self, cont):
        correcto = False

        if(listaLex[cont] == ")"):
            correcto = True

        return correcto


    def AnalizadorSintac(self):
        i = 0
        ParA = 0
        ParC = 0
        correcto = False
        while (i < len(listaLex)):
            if (listaLex[i] == "("):
                ParA += 1
                i = i+1
                correcto = self.Parentesis(i)
            if (listaLex[i]) == ")":
                ParC += 1
                i = i+1
        
        if(ParA != ParC):
            ERROR(")", "Error sintactico, falto parentesis cerrado )", 0, 0)


    def Path(self, texto):
        ruta = "/js/"
        Tkn.ReporteToken(self, ruta )
        ERROR.ReporteError(self, ruta )
