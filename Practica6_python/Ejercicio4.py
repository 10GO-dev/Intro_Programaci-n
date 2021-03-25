'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común
 o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.'''

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