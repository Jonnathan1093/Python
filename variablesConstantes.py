#Damos valor a una variable
from re import X
from argon2 import PasswordHasher
from sqlalchemy import true


precio = 253
cantidad = 3

#Calculamos total
total = precio * cantidad

#Mostrar el resultado
print ("El resultado total es de "+ str(total))

#Borrar una variable
del precio
print (cantidad)

#Asignamos otros valores
precio =25
cantidad = 21
 
#Calculamos total
total = precio * cantidad

#Mostrar el resultado
print ("El resultado total es de "+ str(total))

#Variable constante
PASSWORD = "123456789"

#Asignar varios valores
a,b,c,d = 1,4,"Nombre",True

print (a)
print (b)
print (c)
print (d)

#Asignar mismo valor a distintas variables
x = y = z = 68

print(x)
print(z)






