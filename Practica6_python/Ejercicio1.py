'''1. Crear una clase Persona que tenga como atributos el "cedula, nombre, apellido y la edad (definir las propiedades
para poder acceder a dichos atributos)". Definir como responsabilidad una cuncion para mostrar ó imprimir. Crear una
segunda clase Profesor que herede de la clase Persona. Añadir un atributo sueldo ( y su propiedad) y en la función para 
imprimir su sueldo. Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. También crear un objeto 
de la clase Profesor y llamar a sus funciones y propiedades.
'''
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