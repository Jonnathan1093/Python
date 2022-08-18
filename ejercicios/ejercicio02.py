# 02. Crea una calculadora basica, incluyendo menu opciones 
# y comprobando que no se intente dividir por cero.

def menu():
    print("Selecciona la operacion (1,2,3,4)")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Dividir")
    opcion = int(input())
    return opcion

def dameResultado(seleccion):
    num1 = int(input("Dime el primer numero "))
    num2 = int(input("Dime el segundo numero "))
    if (seleccion == 1):
        resultado = num1 + num2
    elif (seleccion == 2):
        resultado = num1 - num2
    elif (seleccion == 3):
        resultado = num1 * num2
    elif (seleccion == 4):
# Devemos resolver el problema del 0 con un try
        try:
            resultado = num1 / num2
        except:
            print("Error al dividir")
            resultado = 0
    else:
        print("Seleccione una opcion correcta")
    return resultado
continua = True
# Aplicamos un bucle para que se aplique indifinidamente a menos que sea lo contrario
while continua:
    seleccion = menu()
    resultado = dameResultado(seleccion)
    print(f"El resultado es: {resultado}")
    print("Quieres continuar (s/n) ")
    respuesta = input()
    if (respuesta  == "s" or respuesta == "S"):
        continua = True
    else:   
        continua = False
        print("Fin del calculo")    

    
    
    
    
   
    
    