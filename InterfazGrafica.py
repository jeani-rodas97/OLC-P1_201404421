from tkinter import *
from tkinter import filedialog, scrolledtext, Canvas, messagebox
from AnalizadorHTML import HTML
from AnalizadorCSS import CSS
from AnalizadorJS import JS
from AnalizadorRMT import RMT
from Token import Tkn
from Error import ERROR

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
        '''
        self.editor.tag_add("start", "3.0", "3.1")
        self.editor.tag_config("start", background="black", foreground="yellow")
        editor1 = self.editor
        self.editor.tag_add("start1", "3.1", "3.5")
        editor1.tag_config("start1", background="green", foreground="red")
        '''
        Ruta = self.Archivo 
        extension = Ruta.split(".")
        mensaje = messagebox.showinfo("Tipo Archivo", "Es un archivo "+ extension[1])
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
        self.Color()
        self.EscribirConsola()
        self.EscribirEstados()

    def Color(self):
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
                elif(c[item+3] == "Cadena"):
                    color = "yellow"
                elif(c[item+3] == "Reservada"):
                    color = "red"
                elif(c[item+3] == "Comentario"):
                    color = "gray"
                elif((c[item+3] == "Numero")|(c[item+3] == "Porcentaje")):
                    color = "blue"
                elif(c[item+3] == "Variable"):
                    color = "green"
                else:
                    color = "white"

                self.editor.tag_add(f"start{i}", f"{c[item]}.{c[item+1]}", f"{c[item]}.{c[item+2]}")
                #print("start", f"{c[item]}.{c[item+1]}", f"{c[item]}.{c[item+2]}")
                self.editor.tag_config(f"start{i}", background= color)
                i +=1 


                
        #self.editor.tag_add("start", f"{fila}.{inicio}", f"{fila}.{fin}")
        #self.editor.tag_add("start", "1.8", "1.13")
        #self.editor.tag_config("start", foreground=f"{color}")
        #self.editor.tag_config("start", background="black", foreground="yellow")


    def OpSalir(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value :
            ventana.destroy()


if __name__ == "__main__":
    ventana = Tk()
    app = Interfaz(ventana)
    Interfaz(ventana).editor.focus()
    ventana.mainloop()