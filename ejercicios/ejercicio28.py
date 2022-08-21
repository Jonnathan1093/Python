# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos y atributos, para mostrar los datos y un mensaje con el resultado de la nota

class Alumno(): # Clase reservada
    def __init__(self, nombre, nota): # Inicio del constructor de la clase
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def valoracion(self):
        if self.nota < 5:
            print(f"{self.nombre} ha suspendido")
        else:
            print(f"{self.nombre} ha aprobado")

if __name__ == "__main__":
    # Creamos los objetos de la clase
    alumno1 = Alumno("Lucia", 7)
    alumno2 = Alumno("Eva", 8)
    alumno3 = Alumno("Maria", 4)
    alumno1.mostrar()
    alumno1.valoracion()
    alumno2.mostrar()
    alumno2.valoracion()
    alumno3.mostrar()
    alumno3.valoracion()
    
    
    