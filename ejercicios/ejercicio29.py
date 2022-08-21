# GENERADOR DE CONTRASEÑAS
import string
import random

caracteres = list(string.ascii_letters + string.digits + "!#@&%$()/\+")
# ascii_letters usado para las letas / digits para los numeros y caracteres epeciales
# print(caracteres) 

def dameClave():
    longitud = int(input("Que longitud le damos a la clave? "))
    # mezcla los caracteres
    random.shuffle(caracteres)
    clave = [] # Lista vacia para claves
    for i in range(longitud): # Hasta el rango que ha puesto el usuario
        clave.append(random.choice(caracteres)) # Para elegir un caracter dentro de la lisca caracters
    random.shuffle(clave)
    return ("".join(clave)) # Devolvemos una cadena con todo lo que tenga clave

if __name__ == "__main__":
    clave = dameClave()
    print(f"La clave seleccionada es: {clave}")
    
    
    