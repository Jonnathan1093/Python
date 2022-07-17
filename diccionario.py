diccionario = {"nombre": "Jose", "apellidos": "Ojeda", "tutoriales":["Python", "JavaScript","Php"]}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
print(diccionario["tutoriales"])
print(diccionario["tutoriales"][1]) 

# Recorrer todo el diccinario
for clave in diccionario:
    print(clave, ": ", diccionario[clave])
    
# Metodos para los diccionarios
personas = dict(nombre = "Paul", apellido = "Heras", edad = 29)
print(personas)
print(type(personas))

#Diccionario con zip 
diccionario2 = dict(zip("aeiou", [1,2,3,4,5]))
print(diccionario2) 
print(type(diccionario2))

#Items, si lo usamos los elementos que tiene el diccionario nos pasara
# tuplas y cada par es una tupla con su clave valor
print(diccionario2.items()) 

#  Lista con clave de nuestro diccionario
print(diccionario2.keys())
# Muestra los valores del diccuinario
print(diccionario2.values())

""" # Limpiar o eliminar los valores del diccionario
diccionario2.clear()
print(diccionario2) """

#Copia de un diccionario 
copiaDiccionario = diccionario2.copy()
print(copiaDiccionario)

# Asignar a cada clave un valor especifico
diccionario3 = dict.fromkeys(["a","e", "i", "o", "u"], 34)
print(diccionario3)

# Obtener un valor del diccionario
print(diccionario.get("nombre"))
print(diccionario.get("amigo"))
 
# Borrar una clave especifica
borrado = diccionario.pop("nombre")
print(borrado)
print(diccionario)

# Pasar un diccionario a otro
diccionario2 = {"provincia": "Azuay", "nombre": "Paul"}
print(diccionario)
diccionario.update(diccionario2)
print(diccionario)


