import pandas as pd
import numpy as np

# Crear una serie de pandas
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





