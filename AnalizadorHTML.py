from Token import Tkn
from Error import ERROR

class HTML:
    def __init__(self, TextoHTML):
        self.TextoHTML = TextoHTML
        #print("Lee bien el texto \n " + TextoHTML)
        estado = 0
        lexema = ""
        fila = 1
        columna = 0 
        colorear = 0
        #En este for vamos a leer caracater por caracter de la cadena, ahora hay que enviarlo al estado 
        #Cambiaremos a while porque el for siempre avanza y necesitamos retroceder una iteración 
        i = 0
        while i < len(TextoHTML):
            caracter = TextoHTML[i]
            if (estado == 0):
                lexema = ""
                if ((caracter == '<')|(caracter == '>')|(caracter == '/')|(caracter == '=')|(caracter == '(')|(caracter == ')')|(caracter == ':')|(caracter == '.')|(caracter == ';')|(caracter == '-')|(caracter == ',')):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 1
                elif((caracter == '"')|(caracter == '\'')|(caracter == '”')):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 5
                elif (caracter.isalpha()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 2
                elif (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                elif (caracter == '\n'):
                    columna = 0
                    fila +=1
                    colorear += 1
                    i+=1
                    estado = 0
                elif (caracter.isspace()):
                    lexema += caracter
                    colorear+=1
                    columna += 1 
                    i+=1
                    estado = 0 
                else:
                    lexema += caracter
                    columna += 1
                    colorear += 1
                    ERROR(lexema, "Caracter desconocido", fila, columna)
                    i+=1
                    estado = 0

            elif (estado == 1):
                Tkn(1, lexema, "Signo", fila, columna)
                estado = 0

            elif (estado == 2):
                if(caracter.isalpha()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 2
                elif (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    if(self.Reservadas(lexema) == 2):
                        Tkn(2, lexema, "Palabra", fila, columna)
                    else:
                        Tkn(self.Reservadas(lexema), lexema, "Reservada", fila, columna)
                    estado = 0

            elif (estado == 3):
                if (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    if(self.Reservadas(lexema) == 2):
                        Tkn(2, lexema, "Palabra", fila, columna)
                    else:
                        Tkn(self.Reservadas(lexema), lexema, "Reservada", fila, columna)
                    estado = 0

            elif (estado == 4):
                if (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                else:
                    Tkn(4, lexema, "Numero", fila, columna)
                    estado = 0

            elif (estado == 5):
                if((caracter == '"')|(caracter == '\'')|(caracter == '”')):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 6
                else:
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 5

            elif (estado == 6):
                Tkn(6, lexema, "Cadena", fila, columna)
                estado = 0

            else: 
                print("Nose que hacer")
                Tkn.MostrarTK(self)

        Tkn.MostrarTK(self)
        self.Path(TextoHTML)        
        ERROR.MostrarError(self)
        #Tkn.MostrarColor(self)
        #Interfaz.Color(1, 1.8, 1.13, "red")


        #self.Reservadas("hTml")


    def Reservadas(self, palabra):     
        #Convierto la cadena a mayusculas con el .upper()
        #Si la quiero todas en minusculas uso el .lower()
        id = 2
        if ((palabra.upper() == "HTML")|(palabra.upper() == "HEAD")|(palabra.upper() == "TITLE")|(palabra.upper() == "BODY")):
            id = 3
        elif ((palabra.upper() == "H1")|(palabra.upper() == "H2")|(palabra.upper() == "H3")|(palabra.upper() == "H4")|(palabra.upper() == "H5")|(palabra.upper() == "H6")|(palabra.upper() == "P")):
            id = 3
        elif((palabra.upper() == "IMG")|(palabra.upper() == "SRC")|(palabra.upper() == "STYLE")):
            id = 3
        elif((palabra.upper() == "A")|(palabra.upper() == "HREF")|(palabra.upper() == "UL")|(palabra.upper() == "LI")):
            id = 3
        elif((palabra.upper() == "TABLE")|(palabra.upper() == "BORDER")|(palabra.upper() == "CAPTION")):
            id = 3
        elif((palabra.upper() == "TR")|(palabra.upper() == "TH")|(palabra.upper() == "TD")):
            id = 3
        elif((palabra.upper() == "COLGROUP")|(palabra.upper() == "COL")|(palabra.upper() == "THEAD")|(palabra.upper() == "TBODY")|(palabra.upper() == "TFOOT")):
            id = 3
        else:
            id = 2

        return id

    def Path(self, texto):
        linea = texto.split("\n")
        salida = linea[0].split("output")
        print(salida[1])
        Tkn.ReporteToken(self, salida[1])
        ERROR.ReporteError(self, salida[1])
    



''' Codigo para pruebas de la clase
if __name__ == "__main__":
    Analizador = HTML("buscar en el texto")
    #Analizador.Reservadas("HTML")
'''