from tkinter import *

# Funcion evento click
def click():
    cadena ="Tu color es "
    if(color01.get()):
        cadena +="Rojo "
        ventana.config(bg="red")
    if(color02.get()):
        cadena +="Azul "
        ventana.config(bg="blue")
    if(color03.get()):
        cadena +="Amarillo "
        ventana.config(bg="yellow")
    etiqueta.config(text = cadena)
    # Para controlar en caso no se selccione
    if(not color01.get() and not color02.get() and not color03.get()):
        cadena = "No hay nada seleccionado"
        ventana.config(bg="black")
        
ventana =Tk()
ventana.title("Option Button")
ventana.geometry("600x300")

frame = Frame()
frame.pack()

color01 = IntVar()
color02 = IntVar()
color03 = IntVar()

# Check
chkRojo = Checkbutton(frame, text="Rojo", variable = color01, onvalue = 1, offvalue=0, command = click)
chkRojo.grid(column=1, row=2)

chkAzul = Checkbutton(frame, text="Azul", variable = color02, onvalue = 1, offvalue=0, command = click)
chkAzul.grid(column=1, row=3)

chkAmarillo = Checkbutton(frame, text="Rojo", variable = color03, onvalue = 1, offvalue=0, command = click)
chkAmarillo.grid(column=1, row=4)

etiqueta = Label(frame, text="Selecciona la opcion")
etiqueta.grid(column=1, row=6)

ventana.mainloop()