# Guardar datos o archivos
# abrimos el archivo

escritura = open("archivo.txt","w")
# "w" write o modo de escritura
escritura.write("Esto se escribe en el archivo \n esto en la linea siguiente \n\t\t\t Y esta es una linea tabulada")
# Nunca debemos olvidarnos cerrar el archivo
escritura.close() 

# lectura de fichero
lectura = open("archivo.txt", "r")
# Leemos una linea
leeLinea = lectura.readline()
print("Leyendo una linea \n" + leeLinea)
lectura.close()

# leemos todo el fichero
lectura = open("archivo.txt", "r")
# "r" read para leer 
leetodo = lectura.read() # Podemos usar "readlines" que devuelve una lista con cada linea
# print(type(leetodo))
print("leemos todo \n" + leetodo)
lectura.close()




