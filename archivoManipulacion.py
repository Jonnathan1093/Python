import os
# Crear carpeta o directorio
# os.makedirs("Micarpeta")
# Listar el contenido
print(os.listdir("./"))
# Mostrar directorio actual
print(os.getcwd())
# Mostrar tamaño de la carpeta que lo indiquemos
print(os.path.getsize("Micarpeta"))
# Comprobar si es archivo o carpeta
print(os.path.isfile("Micarpeta"))
# Comprobar si es directorio
print(os.path.isdir("Micarpeta"))
# Cambiar de directorio
os.chdir("Micarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())
# Renombrar
os.rename("Micarpeta", "Mi_carpeta")
# Borrar archivos
# os.remove(os.getcwd()+"/archivo.txt")
# print(os.listdir("./"))
# Borrar una carpeta
# os.rmdir("Mi_carpeta")
# os.chdir("../")
# print(os.listdir("./"))






























