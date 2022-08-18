# 06. Muestra, suma y cuenta los numeros que son multiplos de 2 y 3 a la vez, que esten entre 1 y el valor que de el usuario.

n1 = 1 # Sera el numero que iremos recorriendo
cuenta = 0 #Indicara cuantod cumplen la condicion
maximo = int(input("Numero maximo ? ")) #Sera lo que pone el usuario
suma = 0
while True:
    if((3*n1) > maximo): 
        break
    if((3*n1) % 2 == 0): 
        print(3*n1)
        cuenta = cuenta + 1
        suma = suma + (3*n1) 
    n1 = n1 + 1
print(f"Hay {cuenta} multiplos de 3 y 2")
print(f"La suma es {suma}")