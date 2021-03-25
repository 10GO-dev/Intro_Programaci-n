'''2. Crear una clase Contacto. Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion". También deberá tener
 una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos. También tendrá una función "Saludar",
que escribirá en pantalla "Hola, soy " seguido de sus datos. Crear también una clase llamada ProbarContacto. Esta clase deberá
contener sólo la función principal, que creará dos objetos de tipo Contacto, les asignará los datos del contacto y les pedirá
que saluden.'''
#-------------clase Contacto-------------
class Contacto:
  def __init__(self):
    self.nombre = ""
    self.apellido = ""
    self.telefono = ""
    self.direccion = ""
  
  def SetContacto(self):
    print("---------------------------------------")
    print("      Ingresa datos en este objeto     ")
    print("---------------------------------------")
    self.nombre = input("Ingresa el nombre: ")
    self.apellido = input("Ingresa el apellido: ")
    self.telefono = int(input("Ingresa el telefono: "))
    self.direccion = input("Ingresa la direccion: ")
    
  def Saludar(self):
    print("Hola, soy",self.nombre,self.apellido,"mi telefono es",self.telefono,"y mi direccion",self.direccion)

#------clase ProbarContacto------------------
class ProbarContacto():
  def __init__(self):
    self.objeto1 = Contacto() 
    self.objeto2 = Contacto()


#----------- Aqui ingresamos los nombres
contactos = ProbarContacto()
contactos.objeto1.SetContacto()
contactos.objeto2.SetContacto()

#-------------- Aqui el saludo
print("\n---------saludo objeto 1----------\n")
contactos.objeto1.Saludar()
print("\n---------saludo objeto 2----------\n")
contactos.objeto2.Saludar()



