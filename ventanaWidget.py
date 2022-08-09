from tkinter import * 
# Manejo del evento click se usa una funcion
def click():
    texto = "Hola, " + entrada.get()
    etiqueta.configure(text=texto)

ventana = Tk()
ventana.title("Widget Basicos")
ventana.resizable(True, True) 
ventana.config() 

frame = Frame()
frame.pack()
frame.config()
frame.config(width = "120", height = "80")
# Manera de colocar por columna o fila
etiqueta = Label(frame, text= "Etiqueta", font=("Arial", 25))#Asignamos texto, font  y tamaño
etiqueta.grid(column=1, row=2)

entrada = Entry(frame, width="30")
entrada.grid(row=2, column=2)

boton = Button(frame, text="Pulsame", bg="red", fg="white", command=click) #Asignar boton, color back y fron, tambien command asigna la funcion click
boton.grid(column = 1, row = 4)
ventana.mainloop() 

