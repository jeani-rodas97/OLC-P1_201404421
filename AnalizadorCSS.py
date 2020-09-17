from Token import Tkn
from Error import ERROR

ListaEstados = []



class CSS:
    def __init__(self, TextoCSS):
        self.TextoCSS = TextoCSS
        estado = 0
        lexema = ""
        fila = 1
        columna = 0 
        colorear = 0

        i = 0
        while i < len(TextoCSS):
            caracter = TextoCSS[i]
            if (estado == 0):
                lexema = ""
                #Para validar todos los signos permitidos 
                if ((caracter == '{')|(caracter == '}')|(caracter == ':')|(caracter == ';')|(caracter == '(')|(caracter == ')')|(caracter == '*')|(caracter == '.')|(caracter == '#')|(caracter == ',')):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 8
                elif(caracter == '/'):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 1
                #Reconozco las comillas para la cadena 
                elif((caracter == '"')|(caracter == '”')|(caracter == '“')):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 14
                elif(caracter == '-'):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 12
                elif (caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 5
                elif (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 9
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
                if(caracter == "*"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 2
                else:
                    estado = 0

            elif (estado == 2):
                if(caracter == "*"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 3
                elif (caracter == '\n'):
                    columna = 0
                    fila +=1
                    colorear += 1
                    i+=1
                    estado = 2
                elif (caracter.isspace()):
                    lexema += caracter
                    colorear+=1
                    columna += 1 
                    i+=1
                    estado = 2
                else:
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 2

            elif (estado == 3):
                if(caracter == "/"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 4
                else:
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 2
            
            elif (estado == 4):
                Tkn(1, lexema, "Comentario", fila, columna)
                self.esta2(lexema, estado)
                estado = 0

            elif (estado == 5):
                if(caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 5
                elif(caracter == "-"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 6
                else:
                    if(self.Reservadas(lexema) == 2):
                        self.esta2(lexema, estado)
                        Tkn(2, lexema, "Palabra", fila, columna)
                    else:
                        self.esta2(lexema, estado)
                        Tkn(self.Reservadas(lexema), lexema, "Reservada", fila, columna)
                    estado = 0

            elif(estado == 6):
                if(caracter.isalpha()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 7
                else: 
                    estado = 0

            elif(estado == 7):
                if(caracter.isalpha()):
                    columna+=1  
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 7
                else:
                    if(self.Reservadas(lexema) == 2):
                        self.esta2(lexema, estado)
                        Tkn(2, lexema, "Palabra", fila, columna)
                    else:
                        self.esta2(lexema, estado)
                        Tkn(self.Reservadas(lexema), lexema, "Reservada", fila, columna)
                    estado = 0

            elif (estado == 8):
                self.esta2(lexema, estado)
                Tkn(1, lexema, "Signo", fila, columna)
                estado = 0

            elif (estado == 9):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 9
                elif(caracter == "."):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 10
                elif(caracter == "%"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 13
                    '''elif (caracter.isalpha()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 16 '''
                else:
                    Tkn(4, lexema, "Numero", fila, columna)
                    estado = 0

            elif (estado == 10):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 11
                else:
                    ERROR(lexema, "Decimal no permitido", fila, columna)
                    estado = 0

            elif (estado == 11):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 11
                elif (caracter == "%"):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 13
                    '''elif (caracter.isalpha()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 16 '''
                else:
                    Tkn(4, lexema, "Numero", fila, columna)
                    estado = 0

            elif (estado == 12):
                if (caracter.isdigit()):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 9
                else:
                    estado = 0

            elif (estado == 13):
                Tkn(13, lexema, "Porcentaje", fila, columna)
                self.esta2(lexema, estado)
                estado = 0

            elif(estado == 14):
                if((caracter == '"')|(caracter == '”')|(caracter == '“')):
                    columna+=1 
                    lexema += caracter
                    self.esta2(lexema, estado)
                    i+=1
                    estado = 15
                else: 
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 14
                    
            elif (estado == 15):
                self.esta2(lexema, estado)
                Tkn(15, lexema, "Cadena", fila, columna)
                estado = 0

            else: 
                print("Nose que hacer")
                
        self.Path(TextoCSS)

    def esta2(self, lexema, estado):
        self.lexema = lexema
        self.estado = estado
        ListaEstados.append([lexema, estado])

    def estados(self):
        return ListaEstados


    def Reservadas(self, palabra):     
        #Convierto la cadena a mayusculas con el .upper()
        #Si la quiero todas en minusculas uso el .lower()
        id = 2
        if ((palabra.upper() == "COLOR")|(palabra.upper() == "BORDER")|(palabra.upper() == "BACKGROUND-COLOR")|(palabra.upper() == "OPACITY")):
            id = 3
        elif ((palabra.upper() == "BACKGROUND-IMAGE")|(palabra.upper() == "BACKGROUND")|(palabra.upper() == "TEXT-ALIGN")|(palabra.upper() == "FONT-FAMILY")|(palabra.upper() == "FONT-STYLE")|(palabra.upper() == "FONT-WEIGHT")|(palabra.upper() == "FONT-SIZE")):
            id = 3
        elif((palabra.upper() == "FONT")|(palabra.upper() == "PADDING-LEFT")|(palabra.upper() == "PADDING-RIGHT")|(palabra.upper() == "PADDING-BOTTOM")|(palabra.upper() == "PADDING-TOP")|(palabra.upper() == "PADDING")):
            id = 3
        elif((palabra.upper() == "DISPLAY")|(palabra.upper() == "LINE-HEIGHT")|(palabra.upper() == "MARGIN-TOP")|(palabra.upper() == "MARGIN-RIGHT")|(palabra.upper() == "MARGIN-BOTTOM")|(palabra.upper() == "MARGIN-LEFT")|(palabra.upper() == "MARGIN")):
            id = 3
        elif((palabra.upper() == "POSITION")|(palabra.upper() == "BORDER-STYLE")|(palabra.upper() == "BORDER-TOP")|(palabra.upper() == "BOTTOM")):
            id = 3
        elif((palabra.upper() == "TOP")|(palabra.upper() == "RIGHT")|(palabra.upper() == "LEFT")):
            id = 3
        elif((palabra.upper() == "FLOAT")|(palabra.upper() == "CLEAR")|(palabra.upper() == "MAX-WIDTH")):
            id = 3
        elif((palabra.upper() == "MIN-WIDTH")|(palabra.upper() == "MAX-HEIGHT")|(palabra.upper() == "MIN-HEIGHT")):
            id = 3
        elif((palabra.upper() == "PX")|(palabra.upper() == "EM")|(palabra.upper() == "VH")|(palabra.upper() == "VW")|(palabra.upper() == "IN")|(palabra.upper() == "CM")|(palabra.upper() == "MM")|(palabra.upper() == "PT")|(palabra.upper() == "PC")|(palabra.upper() == "URL")|(palabra.upper() == "CONTENT")):
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