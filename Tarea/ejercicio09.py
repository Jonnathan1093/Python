# AREA DE UN TRIANGULO
def areaTriangulo(base, altura):
    area = (base * altura)/2
    return area
#Float, ya que el usuairo introduce una cadena
base = float(input("Dime la base del triangulo: "))
altura = float(input("Dime la altura del triangulo: "))
area = areaTriangulo(base, altura)
print(f"El area del triangulo con base {base} y altura {altura} es {area}")


