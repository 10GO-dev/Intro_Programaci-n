class ClaseA:
  def __init__(self):
      self.claseA = "Esta es la clase A"
      print(self.claseA)

class ClaseB(ClaseA):
  def __init__(self):
    super().__init__()
    self.claseB  = "Esta es la clase B"
    print(self.claseB)

class ClaseC(ClaseB): 
  def __init__(self):
    super().__init__()
    self.claseC = "Esta es la clase C"
    print(self.claseC)
    
#Objeto clase c 
Mensaje = ClaseC()

#imprimir clase C con todas sus herencias
print(Mensaje)