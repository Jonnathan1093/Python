# Cuenta palabras

def cuentaPalabras(texto):
    palabras = texto.split(" ") # Ponemos las comillas separadas para que corte el texto que se le pase por cada espacio en blanco
    palabrasContadas = {} # Diccionario vacio
    contador = 0 # Contador para el bucle
    longitud = len(palabras) 
    for i in range(0, longitud): # Un recorrido desde 0 a la longitud que tenga palabras
        primera = palabras[i] # Cogera la primera palabra de la lista
        # print(primera)
        for j in range(0, longitud): # Bucle interior
            segunda = palabras[j]
            if primera == segunda: # Comprobamos las palabras
                contador += 1  # contador = contador + 1
        palabrasContadas[primera] = contador 
        contador = 0 # Lo igualamos a 0 para que en el siguiente bucle lo vuelva a contar
    return palabrasContadas # Devolvemos el diccionario
try:
    fichero = open("D:\\VSCODE\\Curso Python\\ejercicios\\ejemploCuentaPalabras.txt", "r", encoding='utf-8') #Este fichero sera leido 
    texto = fichero.read()
    #print("Fichero correcto")
    # fichero.close()
except:
    print("No se ha podido leer el fichero")
finally:
    #print("Fichero cerrado")
    fichero.close()
# texto = input("Dime un texto para contar sus palabras repetidas : ") # En caso querramos que el usuario ponga el texto
#texto = "Esto es un texto de ejemplo donde veremos cuantas veces aparece cada palabra dentro de este texto palabra palabra texto dentro donde veremos"
cuentaPalabras = cuentaPalabras(texto)
print(cuentaPalabras)

