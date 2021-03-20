
class Persona:
    def __init__(self,cedula,nombre,apellido,edad):
      self.cedula = cedula
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad

    def mostrarDatos(Datos):
      print("Cedula:",Datos.cedula)
      print("Nombre:",Datos.nombre)
      print("Apellido:",Datos.apellido)
      print("Edad:",Datos.edad)

class Profesor(Persona):
    def __init__(self,cedula,nombre,apellido,edad,sueldo):
       super().__init__(cedula,nombre,apellido,edad)
       self.sueldo = sueldo
       
    def sueldoProfesor(self):
        Persona.mostrarDatos(self)
        print("Sueldo:",self.sueldo)


persona1 = Persona(40219334238,"Diego","Peralta",18)
profesor1 = Profesor(10140524306,"Miguel","Moreta",39,80000)

persona1.mostrarDatos()
print("---------------------------------------------")
profesor1.sueldoProfesor()