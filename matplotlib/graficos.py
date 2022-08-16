import numpy as np
import pandas as pd
# Manera de importat la libreria matplot
import matplotlib.pyplot as plt

# Desde el 1 al numero 150, con un total de 200 elementos
x = np.linspace(1,150,200)
y = x + x**2
# print(x)
# print(y) 

# Para mostrar la grafica
plt.plot(x,y,"blue")
# Para poner un titulo
plt.title("Mi grafica")
# La etiqueta que va a llevar el eje de lax x
plt.xlabel("Valores x")
plt.ylabel("Valores y")
# Simpre que terminemos de preparar la grafica necesitamos de show
plt.show()

# Subplots o dos graficas a al 
# Indicaria, fila, columna y posicion que tomaria el grafico
plt.subplot(1,2,1)
plt.plot(x,y,"orange")
plt.subplot(1,2,2)
plt.plot(x,y,"green")
plt.show()


