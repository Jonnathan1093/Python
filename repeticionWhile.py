
#Tabla de multiplicar
tabla = int(input("Que tabla quieres multiplicar "))

#Creamos variable contador
contador = 1
print(f"Tabla del {tabla}") 

#Repeticion
while (contador < 11):
    resultado = tabla * contador
    #Mostramos la tabla
    print(f"{tabla} por {contador} es igual a {resultado}\n")
    #Comprobamos si vale 4 y salimos
    # if contador == 4:
    #     print ("El contador llego a 4 no continuo")
    #     break    
    #Incremento del contador
    contador = contador + 1
print ("Fin de la tabla")









