import smtplib

def enviarEmail(remitente, destinatario, mensaje):
    usuario = remitente
    password = 'eqclmzgtivjunkhk' #Colocamos clave generada en google puse otra ya que genere nuevamente
    try:
        conexion = smtplib.SMTP('smtp.gmail.com', 587)#Correo saliente desde google con dicho puerto
        conexion.starttls()
        conexion.login(usuario, password)
        print("Login correcto")
        conexion.sendmail(remitente, destinatario, mensaje)
        print("Email enviado correctamente")
        conexion.quit()
    except smtplib.SMTPAuthenticationError: #Control de autenticacion
        print("Error de autenticacion")

if __name__ == "__main__": #Para ejecutar del mismo script
    # Aqui va el como remitente y destinatario 
    enviar("retrogeeksla@gmail.com", "jonnathan1093@gmail.com",
           "Hola, prueba desde Python")
    