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