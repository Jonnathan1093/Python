from tkinter import *
from tkinter import messagebox

def info():
    
    messagebox.showinfo("Mensaje", "Mensaje desde messagebox")

def advertencia():
    messagebox.showwarning("Mensaje", "Mensaje de advertencia")

def pregunta():
    messagebox.askyesno("Mensaje", "Mensaje de pregunta")

ventana = Tk()
ventana.geometry("200x140")

boton1 = Button(ventana, text="Info", command=info).place(x=20, y=20)
boton2 = Button(ventana, text="Advertencia", command=advertencia).place(x=20, y=50)
boton3 = Button(ventana, text="Pregunta", command=pregunta).place(x=20, y=80)

ventana.mainloop()

