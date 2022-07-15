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
os.rename("CAPTURAS INFORME - copia (2).rar","Captura informe.zip")































