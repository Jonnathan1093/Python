# BUCLE NUMEROS PARES EN ORDEN INVERSO
inicio = int(input("Dime el numero inicial: "))
fin = int(input("Dime el ultimo numero: "))
print("Te muestro los numeros pares en orden inverso")

for i in range(fin, inicio -1, -1 ): #Le ponemos -1 para que disminuya
    if i %2 == 0:
        print(i)
        
        