#  Definir funcion que muestre una cadena al reves.

def cadenaReves(palabra):
    alRevez = ""
    contador = len(palabra) # Para que recorra todos los caracteres
    indice = -1 # Para que inicie desde el final
    while contador >= 1:
        alRevez += palabra[indice] # Ira recogiendo al revez
        indice = indice + (-1) # para que recoja al revez
        contador -= 1 # contador = contador -1
    return alRevez

print(cadenaReves("Hola soy una frase al derecho"))
        
        
        