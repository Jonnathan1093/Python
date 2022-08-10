# Este script se va a encargar de llamar al otro y realizar el envio del email
from tkinter import *
from tkinter import messagebox # Para poder enviar mensajes
from enviarEmail import enviarEmail

def borrar():
    destinatario.set("")
    txtMensaje.delete(1.0, END)

def enviar():
    remitente = "retrogeeksla@gmail.com"
    mensaje = txtMensaje.get(1.0, END)  #Para que capture el cuadro de texto
    enviarEmail(remitente, destinatario.get(), mensaje)
    borrar()
    mostrarMensaje("Aviso", "Email enviado") #Mostrar un aviso

# Aqui esta la funcion para mostrar el aviso
def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

ventana = Tk()
ventana.geometry("600x520")
ventana.resizable(0, 0)
ventana.title("Email")
ventana.config(bg="blue")

destinatario = StringVar()
lblDestinatario = Label(ventana, text="Destinatario:", font=(
    "Arial", 12), bg="white", fg="blue", pady=5, padx=5)

lblDestinatario.place(x=10, y=10, width=100)
txtDestinatario = Entry(ventana, textvariable = destinatario).place(
    x=120, y=10, width=400)

lblMensaje = Label(ventana, text="Mensaje:", font=(
    "Arial", 12), bg="white", fg="blue", pady=5, padx=5)
lblMensaje.place(x=10, y=50, width=100)
txtMensaje = Text(ventana)
txtMensaje.place(x=120, y=50, width=400)

# Botones para envio y borrar 
btnEnviar = Button(ventana, text="Enviar", command=enviar).place(x=95, y=480)
btnBorrar = Button(ventana, text="Borrar", command=borrar).place(x=495, y=480)

ventana.mainloop()









