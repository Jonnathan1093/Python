#Funcion Map
import functools

lista = [23,85,8,4,52,86,2,47,12]
print (list(map((lambda valor:valor * valor), lista)))

#Funcion Filter
print(list(filter((lambda valor: valor % 2 == 0), lista)))

#Funcion reduce
print (str(functools.reduce((lambda x, resultado: x + resultado), lista)))



