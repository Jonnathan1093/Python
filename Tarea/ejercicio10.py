# FUNCION NUMEROS PRIMOS
# Definicion numero primo
# Si el número es divisible por otro número menor que él, no es primo.
# Si sólo es divisible por sí mismo o por el uno, es primo.
def numPrimo(numero):
#Empezamos desde el numero 2 porque el 1 no lo vamos a considerar
    for i in range(2, numero):
        if numero % i == 0:
            # print(f"El numero {numero} no es primo, {i} es divisible")
            return False
        elif numero % numero == 0 and numero % 1 ==0:     
            # print(f"El numero {numero} no es primo, {i} es divisible")
            return True
        
print(numPrimo(142))            
print(numPrimo(256))
print(numPrimo(1303))

numPrimo = numPrimo(1303)
if numPrimo:
    print(f"El numero 1303 es primo")
else:
    print(f"No es primo")

