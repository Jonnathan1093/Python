# BLUCLES, NUMEROS IMPARES
inicio = int(input("Dime el primer numero: "))
fin = int(input("Dime el ultimo numero: "))
print("Aqui estan los numero impares\n")
for i in range(inicio, fin + 1):
    if i %2 != 0: #Comprobar si el numero es impar
        print(i)
        
        
