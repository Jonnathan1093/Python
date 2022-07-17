colores = ("verde","amarillo","rojo","azul")
print(type(colores))
print(colores)

# Indices de una tupla
print(colores[:2])

# Tupla vacia
tupla =()
print(tupla)
print(type(tupla))

# print(colores[4]) "Cuidado con indices inexistentes"
# colores[2] = "rosa" #No podemos asignar valores a una tupla ya creada 

# Longitud de una tupla
print(len(colores))

# Crear una tupla unitaria
tuplaUnitaria =(50,) #Debemos poner una coma para indicar que es una tupla
print(type(tuplaUnitaria))
print(len(tuplaUnitaria))
 
# Empaquetado de tuplas
a = 10
b = "Jose"
c = 22.34
tuplas = a,b,c
print(tuplas)
print(type(tuplas))

# desempaquetado
a, b, c = tuplas
print(a)
print(b)
print(c)
 