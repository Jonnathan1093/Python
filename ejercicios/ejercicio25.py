#  Escribe una lista con numeros del 10 al 20, mostarla, despues modifica los valores que estan en la posicion 3,6,7 para que su valor sea el resultado de multiplicar el valor que tenia por 4, seguidamente mostrar la lista final.

lista = list(range(10, 21)) # Rango, que comience del 10 al 20
print(lista)
lista[2] *= 4 # Valores en la 3ra posicion
lista[5] *= 4 # Valores en la 6ta posicion
lista[6] = lista[6]*4 # Valores en la 7ta posicion / Tendriamos el mismo resultado de arriba
print(lista)

