#  Definir funcion que indique si el caracter pasado es vocal o no.

def esVocal(c):
    c = c.lower() # Con esto convertimos a minuscula y evitamos evaluar
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u": # Con esto vemos si un caracter es igual a una vocal
        return True
    else:
        return False

print(esVocal("G"))






