from tkinter import * #Para importar todo se pone el asterisco

ventana = Tk()
ventana.title("Mi primera ventana con python")#Nombre de mi ventana
ventana.resizable(True, True) #Redimensionar la ventana
# ventana.iconbitmap("Toxity.ico") # Poner un icono
# ventana.geometry("640x160")#Ancho y alto de la ventana
ventana.config(bg ="blue") # (background = "blue") Color de la ventana

frame = Frame()
frame.pack(side="left", anchor="s")#Colocar el lugar, y su ancho "s" o sur
frame.pack()#Para empaquetar
frame.config(bg="yellow") #Asignar el color
frame.config(width = "120", height = "80")#Poner las dimensiones
ventana.mainloop() #Es como un bucle que esta continuamente actualizando la ventana
