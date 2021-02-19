'''Crear un programa que muestre los primeros 10 números pares
   a partir del producto de (10 x 10)'''  

producto = 10 * 10
for i in range(producto + 2, producto + 21):
  if i % 2 == 0:
    print(i)