import pandas as pd
import numpy as np

""" # Crear una serie de pandas
etiqueta = ["a", "b","c","d","e"]
# Datos del 4 al 8
datos = np.arange(4,9)
# Serie
serie = pd.Series(datos, index=etiqueta)
print(serie)

# Acceder a un valor 
print(serie["c"])

# Datos de distintos tipos
datos = ["Jose", 49,"Juan", 85]
serie = pd.Series(datos)
print(serie)

# Datos directos
serie = pd.Series([1000,500,1200,700], ['Emp01', 'Emp02','Emp03','Emp04'])
print(serie)

# Operaciones de suma de series
serie1 = pd.Series([1000,500,1200,700], ['Emp01', 'Emp02','Emp03','Emp04'])
serie2 = pd.Series([1000,1500,2200,900], ['Emp01', 'Emp02','Emp03','Emp04'])
serie3 = serie1 + serie2
print(serie3)
 """
# DATAFRAMES
filas = ["tienda1", "tienda2", "tienda3", "tienda4"]
columnas = ["articulo1", "articulo2", "articulo3"]
datos = [[np.nan, 100, 200], [np.nan, 100,300],[300,np.nan,400],[400,100,500]]
# np.nan es para agregar valores nulos 

dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)

# Para seleccionar una fila de dataframe
# Usamos loc, porque no queremos usar el indice
print(dataframe.loc["tienda2"])
# Si quieieramos mostrar dos se pone doble corchete
print(dataframe.loc[["tienda2", "tienda3"]])

# Seleccion por columnas
print(dataframe["articulo3"])

# Valor concreto
print(dataframe.loc["tienda2", "articulo3"])

# Añadir una nueva columna
dataframe["articulo4"] = 25
print(dataframe)

# Total - suma de articulos
dataframe["total"] = dataframe["articulo1"]+dataframe["articulo2"] + dataframe["articulo3"]+dataframe["articulo4"]
print(dataframe)

# Eliminar una 
# dataframe = dataframe.drop(["total"], axis=1)
print(dataframe.drop(["total"], axis=1, inplace=True))# axis=1 para que sepa que es una columna axis=0 hara borrado por fila
print(dataframe)

# Mostrar parte del dataframe con una condicion
condicion = dataframe > 200
print(dataframe[condicion])

# Condicion de acuerdo a si es mayor o menor que cierto numero
condicion = (dataframe["articulo1"] >= 200) & (dataframe["articulo2"] >= 100)
print(dataframe[condicion])

# Crear una columna y convertir en indice
nuevaColumna = "1 2 3 4".split() #Split nos corta por espacio y nos devuelve una lista
dataframe["indice"] = nuevaColumna
print(dataframe)
# Pasar la columa ahora como indice
dataframe = dataframe.set_index("indice")
print(dataframe)

# Eliminar valores nulos
# axis = 0 "para fila" / axis = 1 "para columna"
# Implace = True para que el dataframe se quede guardado
# dataframe.dropna(axis=1, inplace=True)
print(dataframe)

# Rellenar con valores que se considere oportunos
# dataframe.fillna(value=90, inplace=True)
# print(dataframe)

# Tambien podemos llenarlo con la media
media = dataframe.mean()
print(f"La media es igual a {media}")
dataframe.fillna(value=media, inplace=True)
print(dataframe)

# Union de dataframes
data1 = dataframe.copy()
data2 = dataframe.copy()
print(data1)
print(data2)
dataTotal = pd.concat([data1,data2])
print(dataTotal)

# Para ver valores unicos
print(dataframe["articulo4"].unique())

# Contar cuantas veces se repite un valor
print(dataframe["articulo4"].value_counts())

# Multiplicacion a todos los valores
# Apply para aplicar una funcion
dataTotal = dataTotal.apply(lambda x: x*3)
print(dataTotal)

# Obtener las columnas del dataframe
print(dataTotal.columns)
# Obtener el indice
print(dataTotal.index)
# Ordenar por una de las columnas, iria de menor a mayor
print(dataTotal.sort_values(["articulo3"]))

# Obtener una estadistca del dataframe
print(dataTotal.describe())

# Pasar un dataframe a un fichero csv
# dataTotal.to_csv("dataTotal.csv")

# Si quiseramos cargar el archivo
dataframe = pd.read_csv("dataTotal.csv", index_col=0)
print(dataframe)





