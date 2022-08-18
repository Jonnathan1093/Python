# Definir una funcion que calcule la suma y multiplicacion de una lista.

def suma(lista): # Creamos una funcion que pasaremos una lista
    suma = 0
    for i in lista:
        suma += i # Seria igual a. suma = suma +i /va añadiendo a la variable suma cada valor de i al recorrer la lista
    return suma

def multiplica (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

lista = [1,12,53,15,18,86,8,12,52]

print(suma(lista)) #Llamamos a la funcion suma y pasamos la lista
print(multiplica(lista))
        
        
        
         
        
        