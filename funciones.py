def esPar(numero):
    if numero % 2 == 0:
        #print("El numero es par")
        return True
    else:
        #print("El numero no es impar")
        return False
    
numero=int(input("Dime un numero y te dire si es par o impar "))#Llamamos al usuario
resultado = esPar(numero) #Llamamos a la funcion
if resultado:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")








