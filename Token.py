from os import remove
listaTK = []

listaCol = []

class Tkn:
    
    def __init__(self, id, lex, tipo, fila, col):
        self.id = id
        self.lex = lex
        self.tipo = tipo
        self.fila = fila 
        self.col = col
        listaTK.append([id, lex, tipo, fila, col])  
        listaCol.append([fila, col - len(lex), col , tipo])   

    def MostrarTK(self):
        for tok in listaTK:
            print(tok)

    def MostrarColor(self):
        for col in listaCol:
            print(col)

    def ConsultaColor(self):
        return listaCol

    def ConsultarTok(self):
        return listaTK
            
        '''for i in range(len(listaTK)-4):
            fila, inicio, fin, color
            print(f"id : {listaTK[i]} lex: {listaTK[i+1]} tipo: {listaTK[i+2]} fila: {listaTK[i+3]} columna: {listaTK[i+4]}")
            i = i+4 '''

    def ReporteToken(self, ruta):
        Arch = "C:/Users/Jeany/Documents"+ruta +"ReporteTk.html"
        archivo = open(Arch, "w")
        archivo.writelines("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />" + "\n" + "\n")
        archivo.writelines("<HTML><HEAD><TITLE>COMPILADORES 1</TITLE></HEAD>" + "\n" + "\n")
        archivo.writelines("<H1><CENTER><B><FONT SIZE=\"12\" COLOR=\"PINK\">LISTADO DE TOKENS</FONT></B><BR></H1>" + "\n" + "\n")
        archivo.writelines("<HR>" + "\n" + "\n")
        archivo.writelines("<BR><CENTER><TABLE BORDER=1>\n")
        archivo.writelines("	<TR>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>No.</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Id Token</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Lexema</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Tipo</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Fila</B></FONT></TD>\n")
        archivo.writelines("	<TD ALIGN=\"CENTER\"><FONT COLOR=\"PURPLE\"><B>Columna</B></FONT></TD>\n")
        i=1
        for t in listaTK:
            for item in range(len(t)-4):

                archivo.writelines("	<TR>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"RED\"><B> {i} </B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item]}</B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+1]}</B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+2]} </B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+3]}</B></FONT></TD>\n")
                archivo.writelines(f"	<TD ALIGN=\"CENTER\"><FONT COLOR=\"BLACK\"><B> {t[item+4]}</B></FONT></TD>\n")
                
                i +=1 
        
        archivo.write("</TABLE>" + "\n")
        archivo.close()

    def LimpiarHTML(self):
        #remove("C:/Users/Jeany/Documents/Archivos_Python/Compi_Proy1/ReporteTk.html")
        del listaCol[:]
        del listaTK[:]
