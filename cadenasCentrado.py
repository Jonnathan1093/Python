texto = "Esto es un texto para el ejemplo que vamoss a realizar"
#startswith para buscar la primera palabra
print ("La cadena empieza con: ", texto.startswith("vamos"))
#endswith para buscar la ultima palabra
print ("La cadena termina con: ", texto.endswith("realizar"))
#El lower para comvertir en minuscula y hacer una comparacion en este ejemplo
print ("La cadena termina con: ", texto.lower().endswith("Realizar".lower()))

#Alinear texto centrado
print (texto.center(80, '*'))
# Para contar los caracteres
longitudCadena = len(texto)
print (longitudCadena)
print (texto.center(longitudCadena+7, '-'))

#Texto a la izquierdagit
print (texto.ljust(80, '-'))

# Texto a la derecha
print (texto.rjust(80,'*'))

# Eliminar espacios en blanco
texto = "  Esta es una oracion donde se elimina algunos espacios -l/*-/"
print (texto)
print ("Cadena sin espacios en blanco: ")
print (texto.strip())

# Sustituir caracteres
print (texto.replace("-", " hola "))
# Esta es una manera de hacerlo pero guardandolo
textoModificado = texto.replace("-", " hola ") 
print(textoModificado)
print(texto)



