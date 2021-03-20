numeros = []

def cargarLista():

  for x in range(10):
    num = int(input("ingresa un entero: "))
    numeros.append(num)
  
def mostrarLista():
      print(numeros)


#Programa
cargarLista()
mostrarLista()