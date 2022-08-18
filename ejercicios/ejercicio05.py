# 05. El ordenador piensa un numero y el usuario tiene que adivinarlo, muestra tambien el numero de intentos.

# Importamos el modulo random para los numeros al azar y ponemos un alias
from random import randint as azar
# Pasamos una funcion de un rango del a al 99
def piensaNumero():
    piensaNumero = azar(1, 100)
    return piensaNumero
# 
def solicitaNumero():
    numeroUsuario = int(input("Adivina el numero que he pensado ... "))
    return numeroUsuario

piensaNumero = piensaNumero()
numeroUsuario = solicitaNumero()

intentos = 0
continua = True
while (continua):
    if numeroUsuario < piensaNumero:
        print("El numero que he pensado es mayor")
        intentos = intentos + 1
        numeroUsuario = solicitaNumero()
    elif numeroUsuario > piensaNumero:
        print("El numero que he pensado es menor")
        intentos = intentos + 1
        numeroUsuario = solicitaNumero()
    else:
        print("Lo adivinastes")
        print("El numero de intentos es "+str(intentos)) #str ára convertir en cadena
        print("Quieres continuar (s/n)? ")
        continuar = input()
        if(continuar == "s" or continuar == "S"): #Estamos haciendo una comprobacion
            continua = True
            intentos = 0
            piensaNumero = piensaNumero()
            numeroUsuario = solicitaNumero()
        else:
            continua = False
print("Fin del juego")








