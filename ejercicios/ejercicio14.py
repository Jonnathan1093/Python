# Dada una cadena indicar si es palindromo o no.

# Palindromo es cuando una palabra se lee igual desde derecha o al revez

palabra = input("Dime una palabra: ")
palabraAlReves = palabra[::-1] #Inidcamos que vaya de principio a fin, pero desde el final
print(palabra)
print(palabraAlReves)
if(palabra == palabraAlReves):
    print("Es palindromo")
else:
    print("No es palindromo")







