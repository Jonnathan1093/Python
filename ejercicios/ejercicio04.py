# 03. Descomponer una cadena en sus caracteres.

# Nos va indicar cuantos son los numeros pares    
cuenta = 0
print("Numeros Pares ")
for i in range(1, 51):
    if(i % 2 == 0): #Moludo para verificar si es par
        print(i)
        cuenta = cuenta + 1
print(f"Tenemos {cuenta} numeros pares")


