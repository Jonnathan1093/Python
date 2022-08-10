from tkinter import *

ventana = Tk()
ventana.title("Texto caja grande")# Nombre ventana
ventana.geometry("180x140") #Dimension ventana

frame = Frame() #Es como el lienzo
frame.pack()

scrollY = Scrollbar(frame) #Scroll o barra de despliegue
scrollY.pack(side=RIGHT, fill= Y) #Posicionar la barra "Lado, y relleno vertical"

texto= Text(frame)
texto.config(width=50, height=50, bg="blue")
texto.pack(expand=YES,fill=BOTH)
texto.insert(0.0, "Texto inicial")
texto.config(yscrollcommand=scrollY.set)

scrollY.config(command= texto.yview)

ventana.mainloop()

