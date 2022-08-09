from tkinter import *

# Funcion evemto click
def click():
    cadena ="Tu color es "
    if(opcion.get()==1):
        cadena +="Rojo "
        ventana.config(bg="red")
    if(opcion.get()==2):
        cadena +="Azul "
        ventana.config(bg="blue")
    if(opcion.get()==3):
        cadena +="Verde "
        ventana.config(bg="green")
    etiqueta.config(text = cadena)
    
ventana =Tk()
ventana.title("Option Button")
ventana.geometry("600x300")
frame = Frame()
frame.pack()

# Para capturar la opcion 
opcion = IntVar()
# Radio Button
rbRojo = Radiobutton(frame, text="Rojo", variable = opcion, value = 1, command = click)
rbRojo.grid(column=1, row=3)

rbAzul = Radiobutton(frame, text="Azul", variable = opcion, value = 2, command = click)
rbAzul.grid(column=1, row=4)

rbVerde = Radiobutton(frame, text="Verde", variable = opcion, value = 3, command = click)
rbVerde.grid(column=1, row=5)

etiqueta = Label(frame, text="Selecciona la opcion")
etiqueta.grid(column=1, row=6)

ventana.mainloop()