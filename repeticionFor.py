
#Tabla de multiplicar con For
tabla = int(input("Que tabla quieres ver "))
print(f"Tabla del {tabla}") 

#Repetir mientras sea menor que 11
for contador in range (1, 11):
    resultado = tabla * contador
    print (f"{tabla} por {contador} es igual a {resultado}")
print ("Fin de la tabla")

#Ejemplo For con nombres

nombres =["Carlos", "Maria", "Jose", "Nino"]
for nombre in nombres:
    print (f"Hola {nombre}")
    
#Mostrar 100 numeros
for numero in range (100):
    print(numero + 1)
    
    
    
    
