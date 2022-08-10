from cgitb import text
from tkinter import *
from tkinter import messagebox

def mensaje():
    messagebox.showinfo("Mensaje", "Hola " + texto.get())

def borrar():
    texto.set("")
    # Set para conseguir el valor
    
# Inicio de la ventana con su tamaño
ventana = Tk()
ventana.geometry("320x140")
ventana.title("Saludo")

# Variable nombre
texto = StringVar()

# Componentes de la ventana
etiquetaNombre = Label(ventana, width = 40, text="Nombre", bg="white", fg="blue").place(x=20, y=30)
cajaNombre = Entry(ventana, width=40, bg="white", fg="red",textvariable=texto).place(x=20, y=70)

# Botones
btSaludar = Button(ventana, text="Saludar", command=mensaje).place(x=20, y=100)
btBoarrar = Button(ventana, text="Borrar", command=borrar).place(x=200, y=100)

# No olvidar 
ventana.mainloop()


