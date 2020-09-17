from tkinter import *
from tkinter import filedialog, scrolledtext, Canvas, messagebox
from AnalizadorHTML import HTML
from AnalizadorCSS import CSS
from AnalizadorJS import JS
from AnalizadorRMT import RMT
from Token import Tkn
from Error import ERROR
import os

class Interfaz:
    def __init__(self, ventana):
        self.Archivo = " "
        self.ventana = ventana
        self.ventana.title("ANALIZADOR")
        self.ventana.configure(background = "LightPink1")
        MenuSup = Menu(ventana)
        self.ventana.config(menu = MenuSup, width = 1000, height = 600)
        Pantalla = LabelFrame(self.ventana, text = '')
        Pantalla.grid(row=0,column=0,columnspan=20,pady=20)

        
        #Editor de la entrada donde se va a cargar el archivo 
        Label(Pantalla,text='Archivo de Entrada:').grid(row=2,column=5)
        self.editor = scrolledtext.ScrolledText(Pantalla, undo = True, height=25, width=60)
        self.editor.grid(row=4,column=5)

        #Consola de salida 
        Label(Pantalla,text='Recorrido:').grid(row=2, column=16)
        self.recorrido = scrolledtext.ScrolledText(Pantalla, undo = True, height=25, width=40)
        self.recorrido.grid(row = 4,column= 16)

        Label(Pantalla,text='      ').grid(row=4,column=15)

        #Recorrido de estados 
        Label(Pantalla,text='Errores: ').grid(row = 5, column=16)
        self.consola = scrolledtext.ScrolledText(Pantalla, undo = True, height=11, width=40)
        self.consola.grid(row = 6, column= 16)

        Label(Pantalla,text='      ').grid(row=3,column=20)
        #Menu de barra 
        MenuOpArch = Menu(MenuSup, tearoff=0)
        MenuOpArch.add_command(label = "Nuevo", command = self.MenuNuevo)
        MenuOpArch.add_command(label = "Abrir", command = self.MenuAbrir)
        MenuOpArch.add_command(label = "Guardar", command = self.ArchGuardar)
        MenuOpArch.add_command(label = "Guardar Como", command = self.ArchGuardarComo)

        MenuSup.add_cascade(label = "Archivo", menu = MenuOpArch)
        MenuSup.add_cascade(label = "Analizar", command = self.Analizar)
        MenuSup.add_cascade(label = "Salir", command = self.OpSalir)

    def MenuNuevo(self):
        self.editor.delete(1.0, END)
        #Interfaz.editor.delete(1.0, END)
        self.Archivo = " "

    def MenuAbrir(self):
        self.Archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/Users/Jeany/Documents/Compi1")
        ArchEntrada = open(self.Archivo)
        Texto = ArchEntrada.read()
        self.editor.delete(1.0, END)
        self.editor.insert(INSERT, Texto)
        ArchEntrada.close()


    def ArchGuardar(self):
        if (self.Archivo == " "):
            self.ArchGuardarComo
        else:
            GuardarArch = open(self.Archivo, 'w')
            texto = self.editor.get(1.0, END)
            GuardarArch.write(texto)
            GuardarArch.close()

    def ArchGuardarComo(self):
        self.Archivo = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/Users/Jeany/Documents/Compi1")
        ArchivoGuardarC = open(self.Archivo, 'w+')
        texto = self.editor.get(1.0, END)
        ArchivoGuardarC.write(texto)
        ArchivoGuardarC.close()
        #Archivo = GuardarDoc

    def EscribirConsola(self):
        LError = []
        LError = ERROR.ErroresList(self)
        self.consola.delete(1.0, END)
        for er in LError:
            self.consola.insert(INSERT, er)
            self.consola.insert(INSERT, "\n")

    def EscribirEstados(self):
        LEstados = []
        LEstados = CSS.estados(self)
        self.recorrido.delete(1.0, END)
        for est in LEstados:
            self.recorrido.insert(INSERT, est)
            self.recorrido.insert(INSERT, "\n")

    def Analizar(self):
        Tkn.LimpiarHTML(self)
        ERROR.LimpiarErrores(self)
        
        self.consola.delete(1.0, END)
        self.recorrido.delete(1.0, END)
        '''
        self.editor.tag_add("start", "3.0", "3.1")
        self.editor.tag_config("start", background="black", foreground="yellow")
        editor1 = self.editor
        self.editor.tag_add("start1", "3.1", "3.5")
        editor1.tag_config("start1", background="green", foreground="red")
        '''
        Ruta = self.Archivo 
        extension = Ruta.split(".")
        mensaje = messagebox.showinfo("Tipo Archivo", "Es un archivo " + extension[1])
        if (extension[1] == "html"):
            HTML(self.editor.get(1.0, END))
        elif (extension[1] == "css"):
            CSS(self.editor.get(1.0, END))
        elif (extension[1] == "js"):
            JS(self.editor.get(1.0, END))
        elif (extension[1] == "rmt"):
            RMT(self.editor.get(1.0, END))
        else:
            messagebox.showerror("ERROR", "Extensión no aceptada")
        self.Color(extension[1])
        self.EscribirConsola()
        self.EscribirEstados()

    def Color(self, rutaArch):
        signo = False
        cadena = False
        palabra = False
        comentario = False
        numero = False 
        listaC = [] 
        listaC = Tkn.ConsultaColor(self)
        i=0
        #print("Llegue a la lista ")
        
        for c in listaC:
            for item in range(len(c)-3):
                #print(item)
                
                #print("leyendo la lista")
                if(c[item+3] == "Signo"):
                    color = "orange"
                    signo = True
                elif(c[item+3] == "Cadena"):
                    color = "yellow"
                    cadena = True
                elif(c[item+3] == "Reservada"):
                    color = "red"
                    palabra = True
                elif(c[item+3] == "Comentario"):
                    color = "gray"
                    comentario = True
                elif((c[item+3] == "Numero")|(c[item+3] == "Porcentaje")):
                    color = "blue"
                    numero = True
                elif(c[item+3] == "Variable"):
                    color = "green"
                    palabra = True
                else:
                    color = "white"

                self.editor.tag_add(f"start{i}", f"{c[item]}.{c[item+1]}", f"{c[item]}.{c[item+2]}")
                #print("start", f"{c[item]}.{c[item+1]}", f"{c[item]}.{c[item+2]}")
                self.editor.tag_config(f"start{i}", background= color)
                i +=1 

        if (rutaArch == "html"):
            self.grafoHTML(signo, cadena, palabra, comentario, numero)
        elif (rutaArch == "css"):
            self.grafoCSS(signo, cadena, palabra, comentario, numero)
        elif (rutaArch == "js"):
            self.grafoJS(signo, cadena, palabra, comentario, numero)
        elif (rutaArch == "rmt"):
            self.grafoRMT(signo, cadena, palabra, comentario, numero)


                
        #self.editor.tag_add("start", f"{fila}.{inicio}", f"{fila}.{fin}")
        #self.editor.tag_add("start", "1.8", "1.13")
        #self.editor.tag_config("start", foreground=f"{color}")
        #self.editor.tag_config("start", background="black", foreground="yellow")

    def grafoHTML(self, signo, cadena, palabra, comentario, numero):
        print("Entra al metodo grafoHTML")
        htmlDot = "digraph html { \n rankdir=LR; \n node [shape = circle]; \n"
        if (signo == True):
            print("Encontro el signo true")
            htmlDot += " 1 [shape = doublecircle] \n 0->1 [label = \"Signo\"] \n"
        if (palabra):
            htmlDot += "2, 3 [shape = doublecircle] \n 0->2 [label = \"L\"] \n 2->2 [label = \"L*\"] \n 2->3 [label = \"D\"] \n"
        if (numero):
            htmlDot += " 4 [shape = doublecircle] \n 0->4 [label = \"D\"] \n 4->4 [label = \"D*\"] \n"
        if (cadena):
            htmlDot += " 6 [shape = doublecircle] \n 0->5 [label = \"Comillas\"] \n 5->5 [label = \"Todo*\"] \n  5->6 [label = \"Comillas\"] \n"
        htmlDot += "}"
        grafica = open("GrafoHTML.dot", "w")
        grafica.write(htmlDot)
        grafica.close()
        os.system("dot -Tjpg GrafoHTML.dot -o GrafoHTML.jpg")
        os.system("GrafoHTML.jpg")

    def grafoCSS(self, signo, cadena, palabra, comentario, numero):
        cssDot = "digraph CSS { \n rankdir=LR; \n node [shape = circle]; \n"
        if (comentario):
            cssDot += " 1, 4 [shape = doublecircle] \n 0->1 [label = \"/\"] \n 1->2 [label = \"*\"] \n 2->2 [label = \"Todo*\"] \n  2->3 [label = \"*\"] \n 3->2 [label = \"Todo*\"] \n 3->4 [label = \"/*\"] \n "
        if (palabra):
            cssDot += "5, 7 [shape = doublecircle] \n 0->5 [label = \"L\"] \n 5->5 [label = \"L*\"] \n 5->6 [label = \"-\"] \n 6->7 [label = \"L\"] \n 7->7 [label = \"L*\"] \n"
        if (signo):
            cssDot += " 8 [shape = doublecircle] \n 0->8 [label = \"Signo\"] \n"
        if (numero):
            cssDot += " 9, 11, 13 [shape = doublecircle] \n 0->9 [label = \"D\"] \n 0->12 [label = \"-\"] \n 9->9 [label = \"D\"] \n  9->10 [label = \".\"] \n 9->13 [label = \"%\"] \n 10->11 [label = \"D\"] \n 11->11 [label = \"D\"] \n 11->13 [label = \"%\"] \n"
        if (cadena):
            cssDot += " 15 [shape = doublecircle] \n 0->14 [label = \"Comillas\"] \n 14->14 [label = \"Todo*\"] \n  14->15 [label = \"Comillas\"] \n"
        cssDot += "}"
        grafica = open("GrafoCSS.dot", "w")
        grafica.write(cssDot)
        grafica.close()
        os.system("dot -Tjpg GrafoCSS.dot -o GrafoCSS.jpg")
        os.system("GrafoCSS.jpg")

    def grafoJS(self, signo, cadena, palabra, comentario, numero):
        jsDot = "digraph JS { \n rankdir=LR; \n node [shape = circle]; \n"
        if (comentario):
            jsDot += "1, 2, 5 [shape = doublecircle] \n 0->1 [label = \"/\"] \n 1->2 [label = \"/\"] \n 2->2 [label = \"Todo*\"] \n 1->3 [label = \"*\"] \n 3->3 [label = \"Todo*\"] \n 3->4 [label = \"*\"] \n 4->3 [label = \"Todo*\"] \n 4->5 [label = \"/\"] \n"
        if (palabra):
            jsDot += "6 [shape = doublecircle] \n 0->6 [label = \"L\"] \n 6->6 [label = \"L*\"] \n"
        if (signo):
            jsDot += " 7 [shape = doublecircle] \n 0->7 [label = \"Signo\"] \n"
        if (cadena):
            jsDot += " 9 [shape = doublecircle] \n 0->8 [label = \"Comillas\"] \n 8->8 [label = \"Todo*\"] \n  8->9 [label = \"Comillas\"] \n"
        if (numero):
            jsDot += " 10 [shape = doublecircle] \n 0->10 [label = \"D\"] \n 10->10 [label = \"D*\"] \n"
        jsDot += "}"
        grafica = open("GrafoJS.dot", "w")
        grafica.write(jsDot)
        grafica.close()
        os.system("dot -Tjpg GrafoJS.dot -o GrafoJS.jpg")
        os.system("GrafoJS.jpg")

    def grafoRMT(self, signo, cadena, palabra, comentario, numero):
        rmtDot = "digraph RMT { \n rankdir=LR; \n node [shape = circle]; \n"
        if (numero):
            rmtDot += " 1, 3 [shape = doublecircle] \n 0->1 [label = \"D\"] \n 1->1 [label = \"D*\"] \n 1->2 [label = \".\"] \n 2->3 [label = \"D\"] \n 3->3 [label = \"D*\"] \n" 
        if (palabra):
            rmtDot += "4 [shape = doublecircle] \n 0->4 [label = \"L\"] \n 4->4 [label = \"(L|D|_)\"] \n"
        if (signo):
            rmtDot += " 5 [shape = doublecircle] \n 0->5 [label = \"Operador\"] \n"
        rmtDot += "}"
        grafica = open("GrafoRMT.dot", "w")
        grafica.write(rmtDot)
        grafica.close()
        os.system("dot -Tjpg GrafoRMT.dot -o GrafoRMT.jpg")
        os.system("GrafoRMT.jpg")

    def OpSalir(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value :
            ventana.destroy()


if __name__ == "__main__":
    ventana = Tk()
    app = Interfaz(ventana)
    Interfaz(ventana).editor.focus()
    ventana.mainloop()