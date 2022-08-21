# Realiza un script de python para resolver ecuaciones de segundo grado.

from math import sqrt # Sqrt es para hacer las raices cuadradas

def ecuacionSegundoGrado(a, b, c):
    # ax^2 + bx + c = 0
    x1 = 0
    x2 = 0
    parcial = (b**2) - (4*a*c) # aqui entra la ecuacion de la raiz
    if(parcial > 0): # Tiene que ser mayor a 0 o nos dara error
        x1 = (-b + sqrt(parcial))/(2*a)
        x2 = (-b - sqrt(parcial))/(2*a)
        #print("Las raices son: ", x1, x2)
        #print(f"La solucion de x1 es {x1} y la de x2 es {x2}")
        return x1, x2
    else:
        x1 = 0
        x2 = 0
        print("No se puede resolver la ecuacion")
        return x1, x2
    
# Se ingresas los datos para la ecuacion
a = int(input("Dame el valor de 'a': "))
b = int(input("Dame el valor de 'b': "))
c = int(input("Dame el valor de 'c': "))

x1, x2 = ecuacionSegundoGrado(a, b, c)
print(f"La solucion de x1 es {x1} y la de x2 es {x2}")


