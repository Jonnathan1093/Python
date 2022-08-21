# Crea un script de pyhon donde se pregunte, mediante un menu, si se quiere convertir de euros a dolares o de dolares a euros.
DOLAREURO = 0.90

def cambiarDolar(dolares):
    euros = dolares * DOLAREURO
    return euros
def cambiarEuros(euros):
    dolares = euros / DOLAREURO
    return dolares
def solicitarCantidad(tipo):
    cantidad = float(input(f"Cuanta cantidad de {tipo} vas a cambiar? "))
    return cantidad

# Lo ponemos para comprobar si lo esta llamando desde un mismo script
if __name__ == '__main__':
    menu = """
        Cambio de monedas
        Selecciona una opcion
        1. Cambio a Euros
        2. Cambio a Dolares
        3. Salir
    """
# Se ejecutara un bucle em la que solo podremos salir con la tercera opcion
    while True:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = solicitarCantidad("dolares")
            euros = round(cambiarDolar(cantidad), 2) # Round para redondear valores y lo que esta fuera del partentesos 2 decimales
            print(f"El resultado de cambiar {cantidad} dolares es de {euros} euros")
        elif opcion == 2:
            cantidad = solicitarCantidad("euros")
            dolares = round(cambiarEuros(cantidad), 2)
            print(
                f"El resultado de cambiar {cantidad} euros es de {dolares} dolares")
        else:
            print("Adios!!!")
            break
        
        
        
        
        
        
        
        