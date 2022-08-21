#  Solicitar una lista al usuario, ordenarla e indicar con otras listas los numeros pares e impares.

def solicitar():
    lista = [] # Creo una lista vacia
    num = None 
    while num != 0: # != distinto de 0
        num = int(input("Dime un numero: (0 para terminar) "))
        if num > 0:
            lista.append(num) # Agregamos numero
        elif num == 0:
            break
        else:
            print("El numero debe ser mayor que 0")
    return lista

def ordenar(lista):
    lista.sort() # Para ordenar
    pares = [] # Creamos lista vacia de pares
    impares = [] # Creamos lista vacia de impares
    for i in lista:
        if i % 2 == 0: # Modulo para par
            pares.append(i) # Agregamos a la lista de pares
        else:
            impares.append(i) # Agregamos a la lista de impares
    return pares, impares

# print(solicitar())
lista = solicitar() #
print("Imprimimos la lista")
print(lista)
pares, impares = ordenar(lista) # Para que muestre la lista de pares e impares
print("Imprimimos la lista de numeros pares")
print(pares)
print("Imprimimos la lista de numeros impares")
print(impares)


