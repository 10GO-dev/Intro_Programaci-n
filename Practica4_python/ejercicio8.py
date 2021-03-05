alturas = [5.7,5.8,5.9,6.1,6.3]
personas_mas_altas = 0
personas_mas_bajas = 0
suma = 0


for x in range(len(alturas)):
  suma = suma + alturas[x]
Altura_promedio = suma/5

for i in range(len(alturas)):
  if float(alturas[i]) > Altura_promedio:
    personas_mas_altas += 1 
  elif float(alturas[i]) < Altura_promedio:
    personas_mas_bajas += 1
    
   

print("\nLa altura promedio es:",Altura_promedio)
print("\nHay",personas_mas_altas," mas altas que el promedio")
print("\nHay",personas_mas_bajas," mas bajas que el promedio")
