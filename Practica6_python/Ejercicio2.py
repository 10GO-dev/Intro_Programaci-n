#-------------clase Contacto-------------
class Contacto:
  def __init__(self):
    self.nombre = None
    self.apellido = None
    self.telefono = None
    self.direccion = None
  
  def SetContacto(self):
    print("---------------------------------------")
    print("      Ingresa datos en este objeto     ")
    print("---------------------------------------")
    self.nombre = input("Ingresa el nombre: ")
    self.apellido = input("Ingresa el apellido: ")
    self.telefono = int(input("Ingresa el telefono: "))
    self.direccion = input("Ingresa la direccion: ")
    
  def Saludar(self):
    print("Hola, soy",self.nombre," ",self.apellido," mi telefono es",self.telefono," y mi direccion",self.direccion)

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



