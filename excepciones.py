import os
# # Error de la divicion x 0
# numero1 = 45
# numero2 = 0
# try:
#     resultado = numero1 / numero2
#     print(resultado)
# except:
#     resultado = 0
#     print("Ha ocurrido un error")
# finally:
#     print(resultado)
#     print("Esto se ejecuta siempre") 
try:
    os.remove(os.getcwd()+"/archivo10.txt")
except FileNotFoundError:
    print("El archivo no se encuentra en el directorio")
finally:
    print("Fin de la ejecucion")
    