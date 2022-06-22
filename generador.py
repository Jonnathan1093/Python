#Generador
def impares ():
    for numero in range (1, 50, 2):
        yield numero

generador = impares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print("Terminamos datos 1 a 1 y pasamos a bucle")
for numero in generador:
    print(numero)
print(generador)

# for numero in impares():
#     print (numero)
# print (impares)

    
    
    
    
    
    
    
    