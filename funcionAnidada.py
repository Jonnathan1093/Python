def calcular(num1, num2, operacion = "sumar"):
    def sumar(num1, num2):
        return num1 + num2
    def restar(num1, num2):
        return num1 - num2
    def multiplicar(num1, num2):
        return num1 * num2
    def dividir(num1, num2):
        return num1 / num2
    if operacion == "sumar":
        print(f"{num1} + {num2} = {sumar(num1, num2) }")
    elif operacion == "restar":
        print(f"{num1} - {num2} = {restar(num1, num2) }")
    elif operacion == "multiplicar":
        print(f"{num1} * {num2} = {multiplicar(num1, num2) }")
    elif operacion == "dividir":
        print(f"{num1} / {num2} = {dividir(num1, num2) }")  
    return "Resultado devuelto"

print(calcular(3,4))
print(calcular(3,7, "sumar"))
print(calcular(3,4, "restar"))
print(calcular(3,4, "multiplicar"))
print(calcular(3,4, "dividir"))



