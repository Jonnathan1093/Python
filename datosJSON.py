import json
from urllib import request #Para obtener informacion de la web

url = 'https://my.api.mockaroo.com/personas.json?key=3475eaf0'
respuesta = request.urlopen(url)

contenido = respuesta.read()
# print(contenido) # de esta manera podemos ver que obtenermos los datos
json_obtenido = json.loads(contenido.decode("utf-8")) #Decodificamos para obtener caracteres de nuestro idioma
# print(json_obtenido) 
for persona in json_obtenido:
    print(f"Nombre: {persona ['first_name']}")
    print(f"Apellido: {persona ['last_name']}")
    print(f"Email: {persona ['email']}") 
    print(f"Genero: {persona ['gender']}")
    print("\n")
    
    
    
