# ARCHIVO DE TEXTO
def guardaTexto(nombre_archivo, texto):
    try:
        fichero = open(nombre_archivo+'.txt', 'w')
        fichero.write(texto)
        print('Texto guardado')
        return True
    except Exception:
        print('Ha ocurrido un error')
    finally:
        fichero.close()

def leeTexto(nombre_archivo):
    try:
        fichero = open(nombre_archivo+'.txt', 'r')
        texto = fichero.read()
        return texto
    except Exception:
        print('Ha ocurrido un error')
    finally:
        fichero.close()

texto = input('Pon aqui el texto a guardar : ')
archivo = input('Indicame el nombre del archivo : ')
guardaTexto(archivo, texto)
texto = leeTexto(archivo)
print("Este es el texto guardado")
print(texto)




