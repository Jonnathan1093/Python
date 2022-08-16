import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Para leer el archivo csv
datos = pd.read_csv("datos.csv")
# Para cambiar el indice y cual queremos que lea
datos.set_index("ID", inplace=True)
print("Inicio dataframe")
print(datos.head(5))
print("Final dataframe")
print(datos.tail(5))

print(datos.info())
print(datos.describe())
print(datos.columns)
print(datos.index)

# Agrupar los datos
datosAgrupados = datos.groupby('TIENDA').TOTAL.sum()
print(datosAgrupados.head(5))

# Crear un grafico del tipo py, de los datosAgrupados

plt.pie(datosAgrupados, labels=datosAgrupados.index)
plt.show()




