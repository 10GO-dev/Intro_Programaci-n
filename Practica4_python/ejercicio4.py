Lista_principal = [[5,3,8,7,1],[14,3,4,20,13],[25,19,7,19,34]]
lista1 = 0 
lista2 = 0
lista3 = 0

for x in range(len(Lista_principal)):
  for i in range(len(Lista_principal[x])):
    if x == 0:
      lista1 += int(Lista_principal[x][i])
    elif x == 1:
      lista2 += int(Lista_principal[x][i])
    elif x == 2: 
      lista3 += int(Lista_principal[x][i])

print("\nLa suma de la lista del primer elemento es igual a",lista1)
print("\nLa suma de la lista del segundo elemento es igual a",lista2)
print("\nSuma de la lista del tercer elemento es igual a",lista3)

