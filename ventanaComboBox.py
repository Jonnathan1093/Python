from tkinter import *
from tkinter import messagebox

def mostrar():
    messagebox.showinfo("Mensaje", "El valor seleccionado es : " + valor.get())

ventana = Tk()
ventana.geometry("200x140")

valor = StringVar() #Para asignar al combo

etiqueta = Label(ventana, text="Spinbox").place(x=20, y=20)
# Se hace un conteo desde el 1 al 10
combo = Spinbox(ventana, from_=1, to=10, textvariable=valor).place(x=20, y=60)
# Se añade el boton para verifical el numero
boton = Button(ventana, text="Valor ", command=mostrar).place(x=20, y=100)

ventana.mainloop()


