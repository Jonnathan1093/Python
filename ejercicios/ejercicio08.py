# Mostrar el importe del IVA de un articulo con un valor de 80 junto con su precio final.
IVA = 0.12 # Constante con el porcentaje del iva
precioBase = 80
precioFinal = precioBase + (precioBase*IVA)
print(f"El precio final es de {precioFinal}")

