from tkinter import *

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("ANALIZADOR")
        self.ventana.configure(background = "LightPink1")

if __name__ == "__main__":
    ventana = Tk()
    app = Interfaz(ventana)
    ventana.mainloop()