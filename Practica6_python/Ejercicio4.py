lista1 = ["Diego","Pedro","Manuel","Miguel"]
lista2 = ["Elias","Jesus","Miguel","Richard"]

def superposicion():
  cont = 0
  for x in lista1:
    for i in lista2:
      if x == i:
        cont +=1

  if cont > 0:
    print(True)
  else: print(False) 
      
        


superposicion()