lista = [1, 2.3, "Jose", [4,5], 12, 16, 16, 16]
print(type(lista))
print(lista)

print(lista[2])
print(lista[3][1])
print(lista[1:4])
print(lista[2:4:2])

# Otro medotod de mostrar una lista
for elemento in lista:
    print(elemento)

# Metodo "append" para añadir un elemento 
lista.append(10)
lista.append("Lucia")
lista.append([2,3,6,8,9]) #se agrega como un solo elemento, dentro, de esta manera podemos agregar dentro de una lista
print(lista)
lista.extend([4,5,2,4]) # lo agrega como elementos individuales
print(lista)

# Para borrar algun elemento podemos usar "remove"
lista.remove("Jose")#Lo que estamos diciendo es elimianar ese elemento, no la posicion 
print(lista)

# Nos indica en que posicion esta
print(lista.index("Lucia")) 

# Cuantas veces se repite un elemento dentro de una lista
print(lista.count(16))

# Ordenar la lista reves
lista.reverse()
print(lista)

listaCompra = ["pan", "naranjas", "kiwis"]
print(listaCompra)
print(type(listaCompra))

# Crear lista desde variables
cantidadPan = 5
precioPan =0.44
total = cantidadPan * precioPan
pedido = cantidadPan, precioPan, total
pedido2 = [3, 0.70, 3 * 0.30]
pedido3 = [4, 0.50, 4 * 0.50]
pedidos = [pedido,pedido2,pedido3]
print(pedidos)

# Lista vacia
listaVacia = []
print(listaVacia)
print(type(listaVacia))

# Agregar valores a una lista
listaCompra.append("peras")
listaCompra.insert(2,"platanos")
print(listaCompra)

# Eliminar el ultimo elemento con pop
listaCompra.pop()
print(listaCompra)

# Para ver la longitud de una lista
print(len(listaCompra))

# Añadir elementos con un bucle for

cuadrado = []
for numero in range(1,10):
    cuadrado.append(numero * numero)
print(cuadrado)

# Mostrar el minimo, maximo, y la suma de todo
print(min(cuadrado))
print(max(cuadrado))
print(sum(cuadrado))

# Ver si un elemento esta dentro de una lista
print(listaCompra)
print("manzana" in listaCompra)
print("platanos" in listaCompra)