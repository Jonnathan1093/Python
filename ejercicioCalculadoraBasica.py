#Funcion menu
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("0. Salir")
#Devolver la funcion usuario
    opcion = int(input("Digita una opcion "))
    return opcion
#Funcion para solicitat datos al usuario
def solicitaDatos():
    num1 = int(input("Primer numero "))
    num2 = int(input("Segundo numero "))
    if num2 ==0:
        print("El numero no puede ser 0")
        num2 = int(input("Segundo numero "))
    return num1, num2
#Funcion para realizar calculos
def operacion(operador, num1, num2):
#Dentro de esta funcion vamos a comparar
    if operador == "Suma":
        resultado = num1 + num2
    elif operador == "Resta":
        resultado = num1 - num2
    elif operador == "Multiplica":
        resultado = num1 * num2
    elif operador == "Dividir":
        resultado = num1 / num2
    return  resultado
#En este while mientras no se pulse 0 para salir nos mantendremos en un bucle
while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} + {num2} es = ")
        print(operacion("Suma", num1, num2))
    elif opcion == 2:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} - {num2} es = ")
        print(operacion("Resta", num1, num2))
    elif opcion == 3:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} * {num2} es = ")
        print(operacion("Multiplica", num1, num2))
    elif opcion == 4:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} / {num2} es = ")
        print(operacion("Dividir", num1, num2))
    elif opcion == 0:
        break
    else:
        print("Introduzca una opcion valida")
    print("\n")
print("Salimos")














