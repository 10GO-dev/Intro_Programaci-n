'''
7.	Crear una lista y almacenar 20 enteros pedidos por teclado.
Eliminar todos los elementos que sean pares.
 '''

enteros = []


for x in range(20):
   num = int(input("Ingresa un valor entero: "))
   enteros.append(num)

print("\nEstos son los valores ingresados")
print(enteros)     

for k in enteros:
  if int(k) % 2 == 0:
    enteros.remove(k)
  
print("\nLa lista con los pares eliminados:")
print(enteros)