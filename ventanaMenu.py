from tkinter import *
from tkinter import messagebox

def salir():
    opcion = messagebox.askquestion("Salir", "Quieres salir de la ventana")
    # print(opcion)
    if opcion == "yes":
        ventana.destroy()

ventana = Tk()
ventana.geometry("200x140")

barraMenu = Menu(ventana) #Lo asignamoa a ventana

ventana.config(menu=barraMenu)
# Barra de menu, opcion Archivo y dentro de esta esta un submenu
menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Abrir") #Ponermos la opcion para abrir
menuArchivo.add_separator() # Con esto desplegamos
menuArchivo.add_command(label="Salir", command=salir) #Ponemos la opcion salir y esta enlazado a la funcion 
# Barra de menu, opcion Ayuda, y un sub menu
menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de")
# Aqui esta las opciones para Archivo y Ayuda
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

ventana.mainloop()





