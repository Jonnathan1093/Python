# Contar las vocales de una palabra o texto pasado por parametro
texto = input('Ingrese un texto: ')

def cuentaVocales(texto):
    vocales = 'aeiou' # Esto nos servira para la comparacion
    contador = 0    
    longitud = len(texto) # Longitud del texto pasado
    for i in range(longitud):
        letra = texto.lower()[i] # Pasara el texto a minuscula
        # print(letra)
        if letra in vocales:
            contador += 1 # contador = contador +1
    return contador

contador = cuentaVocales(texto) # Parametro que pasamos
print(f"El numero de vocales de la cadena {texto} es igual a {contador}")

