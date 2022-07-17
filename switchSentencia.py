# usuario nos da el numero del mes y nosotro lo pasamos a letra
def dameMes(num):
    meses = {
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiemmbre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
        }
    return meses.get(num, "Mes no valido")
mes = int(input("Introduce un numero del 1 al 12 para optener el mes: "))
# print(dameMes(3))
print(dameMes(mes))









