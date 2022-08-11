from array import array
import numpy as np

# Vamos a crear una lista
lista1 = [1,2,3,4,5,6,7,8,9]

# Convertimos la lista en array o matriz, usamos np, y pasamos la lista
array1 = np.array(lista1)
print(lista1)
print(type(array1))
print(array1)

# Podemos ver aquie que el array2 es una matriz
lista2 = [[1,2,3],[2,5,3],[9,4,3]]
array2 = np.array(lista2)
print(array2)

# Array con rangos comienza desde el 0 en adelante -1
array3 = np.arange(6)
print(array3)

#En caso de un intervalo
array4 = np.arange(2,15,2) 
print(array4)

# Rellenar una matriz con 0, en este caso nos da 4 filas, 5 columnas,
matrizCeros = np.zeros((4,5))
print(matrizCeros)

# Realizar una matriz con unos de 3 filas, 5 columnas
matrizUnos = np.ones((3,5))
print(matrizUnos)

# Matriz de 40 elementos con valores del 2 al 6
# Comienza desde el 2, hasta llegar al 6, mediante 40 elementos
matriz = np.linspace(2,6,40)
print(matriz)

# Matriz identidad
matrizIdentidad = np.eye(7)
print(matrizIdentidad)

# Matriz con numeros aleatoreos de 3 filas, 4 columnas,
# con numeros aleatorios entre 0 y 1
matrizAleatoria = np.random.rand(3,4)
print(matrizAleatoria)

# Matriz aleatoria de manera normal
matrizAleatoriaNormal = np.random.randn(4,3)
print(matrizAleatoriaNormal)

# Matriz aleatoria con numeros enteros, 
# con numeros dados y el numero de elementos
# en este caso del 1 al 50 con 20 elementos

matrizAleatoriaEntero =np.random.randint(1,51,20)
print(matrizAleatoriaEntero)

# Tamaño de los arrays
array = np.random.randint(1,201,30)
print(array)
matriz = array.reshape(5,6)

# Obtener valor maximos 
array = np.random.randint(1,901,200)
print(array)
maximo = array.max()
print(f"El valor maximo es {maximo}")
# Si queremos saber la pocision del valor maximo usamos
print(array.argmax()) #Posicion del array

# Obtener valor minimo
minimo = array.min()
print(f"El valor minimo es {minimo}")
print(array.argmin()) #Posicion del array

# Mostrar elmentos
array = np.arange(1,11) #Llega hasta el num 11 -1 o 10
print(array)
print(array[2]) # El indice #2 seria el 3 ya que comienza desde el 0
print(array [5:]) #Toma desde eñ 5to hasta el ultimo
print(array[:6]) #Inidcamos desde el inicio hasta el 6to

# Copiar un array
array2 = array.copy()
print(array)
print(array2)
array2[4] = 9999 #Se imprime despues de haber modificado el array 2, despues deñ indice 4
print(array)
print(array2)

# Operaciones con la matriz
print(matriz)
print(matriz[0]) #Imprimiria la primera fila
print(matriz[:2]) #Imprime las 2 primeras filas
print(matriz[1][2]) #Imprime la segunda fila y la tercera columna

print(matriz)
print(matriz + 10) #Sumamos a la matriz 10 a cada elemento
print(matriz + matriz) #Sumaria ambas matrices
print(matriz *10) #Multiplicaria po el numero designado
print(matriz*matriz) #Seria cada valor a su cuadrado
print(np.max(matriz)) #Obtener el maximo de la matriz

#Seleccionar valores de una matriz, se usa una condicion 
# las que cumple sera True y False respectivamente
condicion = matriz > 100
print(matriz)
print(condicion)
print(matriz[condicion])

# Condicion para numeros impares
condicion = (matriz %2 != 0)
print (matriz[condicion])

# Valores del 5 al 40
lista = np.arange(5,41)
print("Mostrando lista dimension 1")
print(lista)
# Redimensionamos a 2 filas, 12 columnas
print("Mostando lista dimension en matriz de 3x12")
lista= lista.reshape(3,12)
print(lista)
# Si quiserea mos obtener un valor de esa lista
print("Mostrando valor del indice 2,4")
print(lista[2,4])
# Array aleatorio que nos de una combinacion primitiva
arrayPrimitiva = np.random.randint(1,50,6)
print(f"La combinacion ganadora de la primitiva sera {arrayPrimitiva}")




