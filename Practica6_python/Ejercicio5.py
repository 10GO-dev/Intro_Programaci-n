'''5.Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
 Usando funciones. '''

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