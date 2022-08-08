# CLASE ALUMNO
class Alumno():
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
# Metodo que devulve el texto "str"
    def __str__(self):
        return "El alumno {}, ha sacado un {}".format(self.nombre, self.calificacion)
    
    def aprobado(self):
        if self.calificacion < 5:
            return False
        else:
            return True
        
paul = Alumno("Jose", 10)
print(paul)

aprobado = paul.aprobado()
if aprobado:
    print("Esta aprobado") 
else:
    print("Esta suspendido")       
        
        