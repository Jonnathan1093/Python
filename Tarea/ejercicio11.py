# FUNCION AÑO BISIESTO
def añobisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 and año % 400 == 0:
        return True
    
print(añobisiesto(2019))
print(añobisiesto(2020))
print(añobisiesto(2023))
print(añobisiesto(2025))

