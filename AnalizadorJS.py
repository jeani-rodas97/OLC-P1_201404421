from Token import Tkn
from Error import ERROR

class JS:
    def __init__(self, TextoJS):
        self.TextoJS = TextoJS

        estado = 0
        lexema = ""
        fila = 1
        columna = 0 
        colorear = 0

        i = 0
        while i < len(TextoJS):
            caracter = TextoJS[i]
            if (estado == 0):
                lexema = ""
                if ((caracter == '<')|(caracter == '>')|(caracter == '*')|(caracter == '=')|(caracter == '(')|(caracter == ')')|(caracter == ':')|(caracter == '.')|(caracter == ';')|(caracter == '-')|(caracter == ',')|(caracter == '{')|(caracter == '}')|(caracter == '+')|(caracter == '&')|(caracter == '|')|(caracter == '!')):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 7
                elif (caracter == "/"):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 1
                elif((caracter == '"')|(caracter == '\'')|(caracter == '”')):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 8
                elif (caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 6
                elif (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 10
                elif (caracter == '\n'):
                    columna = 0
                    fila +=1
                    colorear += 1
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
                if(caracter == "/"):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 2
                elif (caracter == "*"):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    Tkn(1, lexema, "Signo", fila, columna)
                    estado = 0

            elif (estado == 2):
                if(caracter == "\n"):
                    Tkn(2, lexema, "Comentario", fila, columna)
                    estado = 0
                else:
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 2

            elif (estado == 3):
                if (caracter == "*"):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                elif (caracter == '\n'):
                    columna = 0
                    fila +=1
                    colorear += 1
                    i+=1
                    estado = 3
                elif (caracter.isspace()):
                    lexema += caracter
                    colorear+=1
                    columna += 1 
                    i+=1
                    estado = 3
                else:
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
            

            elif (estado == 4):
                if (caracter == "/"):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 5
                else:
                    ERROR(lexema, "Falto un /", fila, columna)
                    estado = 0

            elif (estado == 5):
                Tkn(5, lexema, "Comentario", fila, columna)
                estado = 0

            elif (estado == 6):
                if(caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 6
                else:
                    if(self.Reservadas(lexema) == 6):
                        Tkn(6, lexema, "Variable", fila, columna)
                    else:
                        Tkn(self.Reservadas(lexema), lexema, "Reservada", fila, columna)
                    estado = 0

            elif (estado == 7):
                Tkn(7, lexema, "Signo", fila, columna)
                estado = 0

            elif (estado == 8):
                if((caracter == '"')|(caracter == '\'')|(caracter == '”')):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 9
                else:
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 8

            elif (estado == 9):
                Tkn(9, lexema, "Cadena", fila, columna)
                estado = 0

            elif (estado == 10):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    i+=1
                    estado = 10
                else:
                    Tkn(10, lexema, "Numero", fila, columna)
                    estado = 0

            else: 
                print("Nose que hacer")
                Tkn.MostrarTK(self)

        Tkn.MostrarTK(self)
        Tkn.ReporteToken(self)
        ERROR.MostrarError(self)
        ERROR.ReporteError(self)
        #Tkn.MostrarColor(self)
        #Interfaz.Color(1, 1.8, 1.13, "red")


        #self.Reservadas("hTml")


    def Reservadas(self, palabra):     
        #Convierto la cadena a mayusculas con el .upper()
        #Si la quiero todas en minusculas uso el .lower()
        id = 6
        if ((palabra.upper() == "VAR")|(palabra.upper() == "INT")|(palabra.upper() == "STRING")|(palabra.upper() == "CHAR")):
            id = 3
        elif ((palabra.upper() == "BOOLEAN")|(palabra.upper() == "IF")|(palabra.upper() == "ELSE")|(palabra.upper() == "FOR")|(palabra.upper() == "WHILE")|(palabra.upper() == "DO")|(palabra.upper() == "BREAK")):
            id = 3
        elif((palabra.upper() == "RETURN")|(palabra.upper() == "CONSTRUCTOR")|(palabra.upper() == "CLASS")):
            id = 3
        elif((palabra.upper() == "MATH")|(palabra.upper() == "POW")|(palabra.upper() == "SQUARE")|(palabra.upper() == "LI")):
            id = 3
        elif((palabra.upper() == "TABLE")|(palabra.upper() == "BORDER")|(palabra.upper() == "CAPTION")):
            id = 3
        elif((palabra.upper() == "TR")|(palabra.upper() == "TH")|(palabra.upper() == "TD")):
            id = 3
        elif((palabra.upper() == "COLGROUP")|(palabra.upper() == "COL")|(palabra.upper() == "THEAD")|(palabra.upper() == "TBODY")|(palabra.upper() == "TFOOT")):
            id = 3
        else:
            id = 6

        return id     