print ("Tipo entero")
print (type(25))

print ("Tipo decimal")
print (type(38.25))

print ("Tipo cadena")
print (type('Puede ser comilla doble o simpe'))

print ("Tipo boolean")
print (type(True))

#Ejemplo con cadenas

print ("Hola" + " amigos")
#Union de cadenas o concatenacion

print ("Palabras " * 4)
#Se multiplica la palabra 4 veces

variable = "cadena en variable"
variable = "Sumo esta " + variable
print (variable)  
variable = "Sumo esta cadena en variable"
print (variable)
print (variable[5])
print (variable[-2])
print (variable[2:6])
print (len(variable))

print ("Texto en mayuscula".upper())
print (variable.lower())
print (variable.capitalize())

cadena = "   Esta  cadena tiene  varios  es pacios"
print (cadena)
print (cadena.strip())

#Remplazar un valor
cadena = "Este es un texto sin reemplazar valor"
print (cadena)
print (cadena.replace("sin reemplazar valor", "reemplazado"))

