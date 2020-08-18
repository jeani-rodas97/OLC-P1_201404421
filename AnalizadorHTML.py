from Token import Tk
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
                    columna += 1
                    ERROR(lexema, "Caracter desconocido", fila, columna)
                    i+=1
                    estado = 0

            elif (estado == 1):
                Tk(1, lexema, "Signo", fila, columna)
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
                    Tk(2, lexema, "Palabra", fila, columna)
                    estado = 0

            elif (estado == 3):
                if (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 3
                else:
                    Tk(3, lexema, "Palabra", fila, columna)
                    estado = 0

            elif (estado == 4):
                if (caracter.isdigit()):
                    columna+=1 
                    colorear+=1 
                    lexema += caracter
                    i+=1
                    estado = 4
                else:
                    Tk(4, lexema, "Numero", fila, columna)
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
                Tk(6, lexema, "Cadena", fila, columna)
                estado = 0

            else: 
                print("NOse que hacer")
                Tk.MostrarTK(self)

        Tk.MostrarTK(self)


        #self.Reservadas("hTml")

    def Reservadas(self, palabra):     
        #Convierto la cadena a mayusculas con el .upper()
        #Si la quiero todas en minusculas uso el .lower()
        if (palabra.upper() == "HTML"):
            print("Es reservada y a colorear")



''' Codigo para pruebas de la clase
if __name__ == "__main__":
    Analizador = HTML("buscar en el texto")
    #Analizador.Reservadas("HTML")
'''