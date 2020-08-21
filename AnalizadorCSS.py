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
                if ((caracter == '<')|(caracter == '>')|(caracter == '/')|(caracter == '=')|(caracter == '(')|(caracter == ')')|(caracter == ':')|(caracter == '.')|(caracter == ';')|(caracter == '-')|(caracter == ',')):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 8
                #Reconozco las comillas para la cadena 
                elif((caracter == '"')|(caracter == '”')):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 14
                elif (caracter.isalpha()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 5
                elif (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
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