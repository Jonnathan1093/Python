import os
# Listar los archivos que tengo
carpeta = "D:\\PYTHON\\Curso Python\\archivos\\micarpeta"
# print(carpeta)
listado = os.listdir(carpeta)
print(listado)
print(type(listado))
# Filtrado
# for archivo in listado:
#     if archivo.endswith(".txt"):
#         print ("Fichero rar encontrado")
#         print(f"Nombre de fichero: {archivo}")

# OTRA FORMA DE FILTRADO
filtrado = [archivo for archivo in listado if archivo.endswith(".rar")]
print(type(filtrado))
print(filtrado)

# Cambio de directorio
os.chdir("D:\\PYTHON\\Curso Python\\archivos\\micarpeta")
# Como renombrar los archivos
# os.rename("CAPTURAS INFORME - copia (2).rar","Captura informe.zip")

# Eliminar o borrar un archivo
os.chdir("D:\\PYTHON\\Curso Python\\archivos\\micarpeta")
# os.remove("Captura informe.rar")
filtrado = [archivo for archivo in listado if archivo.endswith(".rar")]
print(filtrado)

""" # Renombrar varios archivos a la vez
contador = 1
listado = os.listdir(carpeta)
print(listado)
print("Fin listado inicial")
for archivo in os.listdir():
    nombre, extension = os.path.splitext(archivo)
    print(nombre)
    print(extension)
    nuevoNommbre = f'renombrado{str(contador)}_{nombre}{extension}'
    contador+= 1
    os.rename(archivo, nuevoNommbre)
listado = os.listdir(carpeta)
print("Listado renombrado")
print("\n\n")
print(listado) """

""" # Copiar contenido de un fichero a otro
try:
    fichero = open("testNoexiste.txt", "r")
    nuevoFichero = open("nuevoTest.txt", "w")
    os.chdir("D:\\PYTHON\\Curso Python\\archivos\\micarpeta")
    for linea in fichero:
        nuevoFichero.write(linea)
    fichero.close()
    nuevoFichero.close()
except FileNotFoundError:
    print("No se ha encontrado el fichero") """

# Otra forma de copiar un archivo a otro con "with"
try:
    os.chdir("D:\\PYTHON\\Curso Python\\archivos\\micarpeta")
    with open("testNoExisto.txt") as fichero:
        with open("nuevoTest.txt", "w") as nuevoFichero:
            for linea in fichero:
                nuevoFichero.write(linea)
except FileNotFoundError:
    print("Fichero no encontrado")


















