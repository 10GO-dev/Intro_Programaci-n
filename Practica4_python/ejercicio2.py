''' 2.	Crear y cargar una lista con 10 enteros por teclado. 
Crear un programa que identifique el valor mas pequeño de la lista y
 la posición donde se encuentra. Mostrar en pantalla el resultado.'''

numeros = []
valor_menor = 0

for x in range(10):
  valor = int(input("Ingresa un numero entero: "))
  numeros.append(valor)

valor_menor= min(numeros)

for i in range (len(numeros)):
      if numeros[i] == valor_menor:
        print("\nEl valor mas pequeño de la lista es", valor_menor,
        "y se en cuentra en la posición",i,"de la lista")    
