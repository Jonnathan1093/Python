from random import randint as azar
continua = "s"
while(continua=="s" or continua=="S"):
    lanzaDado = azar(1,8)
    print("Haz sacado un "+str(lanzaDado))
    continua = input("Continuamos (s/n)")
print("Ya no hay mas lanzamientos")

