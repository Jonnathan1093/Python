# MODULO DATETIME
from datetime import datetime

actual = datetime.now().time()
print(actual)
horaSalida = 19
minutoSalida = 30

if ((horaSalida == actual.hour) and (minutoSalida == actual.minute)):
    print("Ya puedes salir")
elif ((horaSalida < actual.hour) and (minutoSalida < actual.minute)):
    print("Ya se ha pasado la hora, vete ya!")
else:
    faltanHoras = horaSalida - actual.hour
    faltanMinutos = minutoSalida -actual.minute
    if faltanMinutos < 0:
        faltanHoras = faltanHoras -1
        faltanMinutos = (-1 * faltanMinutos) + 30
    print(f"Quedan {faltanHoras} horas y {faltanMinutos} minutos")
    
    
    