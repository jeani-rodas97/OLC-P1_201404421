listaERROR = []

class ERROR:
    def __init__(self, error, descripcion, fila, col):
        self.error = error
        self.descripcion = descripcion
        self.fila = fila 
        self.col = col 
        listaERROR.append([error, descripcion, fila, col])
        print("Llega a lista de errores")

    def MostrarError(self):
        for Error in listaERROR:
            print(Error)

    def ReporteError(self):
        archivo = open("C:/Users/Jeany/Documents/Archivos_Python/Compi_Proy1/ReporteERROR.html", "w")
        archivo.writelines("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />" + "\n" + "\n")
        archivo.writelines("<HTML><HEAD><TITLE>COMPILADORES 1</TITLE></HEAD>" + "\n" + "\n")
        archivo.writelines("<H1><CENTER><B><FONT SIZE=\"12\" COLOR=\"PINK\">LISTADO DE ERRORES</FONT></B><BR></H1>" + "\n" + "\n")
        archivo.writelines("<HR>" + "\n" + "\n")
        archivo.writelines("<BR><CENTER><TABLE BORDER=1>\n")
        archivo.writelines("	<TR>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>No.</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Error</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Descripcion</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Fila</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Columna</B></FONT></TD>\n")
        i=1
        for t in listaERROR:
            for item in range(len(t)-3):

                archivo.writelines("	<TR>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"RED\"><B> {i} </B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item]}</B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+1]}</B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+2]} </B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+3]}</B></FONT></TD>\n")
                
                i +=1 
        
        archivo.write("</TABLE>" + "\n")
        archivo.close()

    def LimpiarErrores(self):
        del listaERROR[:]