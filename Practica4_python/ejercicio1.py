'''
Un programa que pida al usuario 4 números, los memorice (utilizando una coleccion), 
calcule su media aritmética y después muestre en pantalla la media y los datos ingresado.
'''

numeros = []
for x in range(4):
  ingresar = int(input("Ingresa un numero: "))
  numeros.append(ingresar)

media_aritmetica = round((numeros[0]+numeros[1]+numeros[2]+numeros[3])/4)

print("\nLa media aritmética es:",media_aritmetica)
print("\nLos datos ingresados son:")
print(numeros)

