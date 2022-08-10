import tkinter as tk
import time

class Ventana():
    def __init__(self):
        self.ventana = tk.Tk() 
        self.ventana.geometry("340x140")
        self.ventana.resizable(0, 0) #Para indicar que no queremos redimencionar ni en ancho y alto
        self.ventana.title("Reloj")
        self.ventana.config(background="blue")
        self.etiqueta = tk.Label(text="", font=("Arial", 40), 
                                 fg="blue", bg="white", 
                                 pady=15, padx=15)
        self.etiqueta.place(x=50, y=20)#Ubicacion del reloj
        self.actualizacion()
        self.ventana.mainloop()

    def actualizacion(self):
        hora = time.strftime("%H:%M:%S")#Para dar formato de hora
        self.etiqueta.configure(text=hora)
        self.ventana.after(1000, self.actualizacion)#Para que se ejecute cada segundo

# Esto nos permite ver si el archivo se esta ejecutando directamente o desde otro
if __name__ == "__main__":
    main = Ventana()
    
    