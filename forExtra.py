#Ejemplo buscar un color
lista_colores = ["amarillo","azul","rojo","blanco"]
mi_color = "rosa"
for color in lista_colores:
    print (color)
    if color == mi_color:
        print ("Color encontrado")
        break #Ponemos un break para salir cuando lo encuentre
    else:
        #print ("El color indicado no esta en la lista")
        print (f"No hay el color {mi_color}")
    
# rango_largo = range (1, 15)
# print (rango_largo)
# for numero in rango_largo:
#     print (numero)
#     if numero == 22:
#         print ("Encontrado el numero ")
#         break
# else:
#     print ("No se ha encontrado el numero")
        
        
        
        
        
        
        