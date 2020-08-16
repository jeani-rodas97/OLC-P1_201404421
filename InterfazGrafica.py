from tkinter import *
from tkinter import filedialog, scrolledtext, Canvas


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
        self.editor = scrolledtext.ScrolledText(Pantalla, undo = True, height=30, width=60)
        self.editor.grid(row=4,column=5)

        #Menu de barra 
        MenuOpArch = Menu(MenuSup, tearoff=0)
        MenuOpArch.add_command(label = "Nuevo", command = self.MenuNuevo)
        MenuOpArch.add_command(label = "Abrir", command = self.MenuAbrir)
        MenuOpArch.add_command(label = "Guardar", command = self.ArchGuardar)
        MenuOpArch.add_command(label = "Guardar Como", command = self.ArchGuardarComo)

        MenuSup.add_cascade(label = "Archivo", menu = MenuOpArch)

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




def OpSalir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value :
        Interfaz(ventana).destroy()


if __name__ == "__main__":
    ventana = Tk()
    app = Interfaz(ventana)
    Interfaz(ventana).editor.focus()
    ventana.mainloop()