'''crear un programa que pida numeros positivos al usuario, y vaya calculando
la suma de todos ellos (terminará cuando se teclea un número negativo o cero)
'''

num = int(input("Ingrese un número positivo o (0 para terminar): "))
suma = num
while num != 0 and num > 0:
  num = int(input("Ingrese otro numero positivo o (0 para terminar): "))
  if num < 0 or num == 0:
    continue
  suma += num
  print(suma)


  
  