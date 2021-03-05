'''Crear un programa que pida al usuario ingresar un número del 0 al 9 
  y muestre en pantalla el número en letra'''

num = [[0,"cero"],[1,"uno"],[2,"dos"],[3,"tres"],
      [4,"cuatro"],[5,"cinco"],[6,"seis"],[7,"siete"],[8,"ocho"],[9,"nueve"]]

numero = int(input( "Ingrese un numero: "))

if numero >= 0 and numero <= 9:
  for x in range(len(num)):
    if numero == num[x][0]:
      print(num[x][1])
else: 
  print("Tienes que ingresar un numero del 1 al 9")

   

  