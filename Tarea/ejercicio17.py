# LISTA
listaUsuario = input("Dame una lista de colorrs sepadado por comas: ")
# Lo que se hace primero es separar todas la palabras que contenga la lista con la coma, y covirtiendo en un cinjunto
listaUsuario = set(listaUsuario.split(","))
listaColores = []
for color in listaUsuario:
    listaColores.append(color)
listaColores.sort() #Sort para odenar
print(listaColores)