edades_mayores = []

for x in range(7):
  edad = int(input("Ingresa una edad: "))
  if edad > 18:
    edades_mayores.append(edad)

print("Las edades mayores a 18 son:\n",edades_mayores)