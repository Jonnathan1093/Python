import os
import pandas as pd
# Directorio actual
directorio_actual = os.getcwd()
print(directorio_actual)
# directorio datos
directorio_datos = os.path.join(directorio_actual, "rutas", "datos" )
# Join es usado para unir y buscar los directorios mas facil
print(directorio_datos)
# Para comprobar si existe el directorio
print("Existe el directorio ?")
print(os.path.exists(directorio_datos))
print("Es una carpeta o directorio ?")
print(os.path.isdir(directorio_datos))
# Listar lo que tenemos dentro la carpeta datos 
listado = [os.path.join(directorio_datos, item)
           for item in os.listdir(directorio_datos)]
print(listado)
print(os.listdir(directorio_datos))

# Crear carpeta
try:
    carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "rutas", "datos","nueva"))
    print(carpeta_nueva)
except FileExistsError:
    print("La carpeta ya existe")
    
# Abrir un fichero fuera de la carpeta
# para ello usamos pandas
fichero_exterior =  os.path.join(directorio_actual, "rutas", "datos.csv")
df_exterior = pd.read_csv(fichero_exterior)
print("Mostramos fichero exterior")
print(df_exterior)
    
# Abrir un fichero dento
fichero_interior =  os.path.join(directorio_datos, "datos.csv")
df_interior = pd.read_csv(fichero_interior)
print("Mostramos fichero interior")
print(df_interior)

# Abrir sin indicar ruta
fichero = "datos.csv"
df = pd.read_csv(fichero)
print("Ficheri sin indicar ruta")
print(df)









