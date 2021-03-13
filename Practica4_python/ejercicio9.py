'''crear una clase que permita ingresar valores enteros por teclados y nos muestre la tabla
de multiplicar de dicho valor. finalizar el programa al ingresar -1'''
def tabla_de_multiplicar():
  multiplo = 1
  for x in range(10):
    print(entrada," x",multiplo," =",entrada*multiplo)
    multiplo +=1
  

entrada = int(input("Ingresa un numero entero: "))
 
while entrada != -1:
  tabla_de_multiplicar()
  entrada = int(input("\nIngresa un numero entero: "))

else:
  print("ha finalizado el programa")