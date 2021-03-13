from os import error


class Cliente:
  User = [
  [4386265817658813,"Marcos Antonio",2578,10000.00,"001-0482267-5","Los Molinos, Sto. Do. Este","05/07/1999"],
  [4706622888055985,"José Hernández",9314,45000.00,"038-3215463-8","Alma rosa I, Sto. Do. Este","03/11/1995"],
  [4894380501711011,"Diego Peralta",2427,150000.00,"402-1933423-7","Los Mameyes, Sto. Do. Este","12/08/2002"],
  [4134586712345568,"Elvis Guillermo",2427,300.00,"402-2257713-1","Manoguayabo, Sto. Do. Sur","31/12/2001"]]
  cuenta_suspendidas = [User[0],User[3]]

clientes = Cliente.User
suspendidas = Cliente.cuenta_suspendidas
#----------------------------------------------------------------------------------------------------------
def info():
  print("\n----------------------------------------------\n")
  print("Codigo usuario =", clientes.index(usuario))
  print("Cuenta:",usuario[0])
  print("Balance:",usuario[3])
  print("Nombre:",usuario[1])
  print("Cedula:",usuario[4])
  print("Direccion:",usuario[5])
  print("Fecha de nacimiento:",usuario[6])
#----------------------------------------------------------------------------------------------------------
def informacion_cuenta():
  if not usuario in suspendidas:
    info()
  else:
    info()
#----------------------------------------------------------------------------------------------------------
def depositar():
  monto = float(input("\nDigite el monto a depositar: "))
  usuario[3] += monto
  print("\nSu nuevo balance es: ")
  print(usuario[3])
#----------------------------------------------------------------------------------------------------------  
def retirar():
  monto = float(input("\nDigite el monto a retirar: "))
  if monto > usuario[3]:
    print("\nNo tienes fondos suficientes")
  else:
    print("\nMonto retirado: ",monto)
    usuario[3]= usuario[3] - monto
    print("\nSu nuevo balance es: ")
    print(usuario[3])   
#----------------------------------------------------------------------------------------------------------
def Banco():
  global usuario
  error = 0
  print("\n-----------------------------------------------------------------")
  print ("\n..:Bienvenido al banco internacional YourMoneyISafe")
  
  while True: 
    cuenta = int(input("\nIngrese el numero de su targeta o (0 PARA FINALIZAR):"))
    if not cuenta == 0:
      for k in range (len(clientes)):
          if cuenta == clientes[k][0]:
              contraseña = int(input("\nIngrese su contraseña:"))
              if contraseña == clientes[k][2]:
                  print("\n--------------------------------------------")
                  print("|        Bienvenido ", clientes[k][1],"       |")
                  print("|__________________________________________|")
                  print("| 1. Informacion de la cuenta              |")
                  print("| 2. Deposito                              |")
                  print("| 3. Retiro de efectivo                    |")
                  print("| 4. Cancelar                              |")
                  print("--------------------------------------------\n")
                  opcion = int(input("\nDigite su opción: "))
                  if not opcion <1 and cuenta >4:
                    if opcion == 1:
                      usuario = clientes[k]
                      informacion_cuenta()
                    if opcion == 2:
                      usuario = clientes[k]
                      if not usuario in suspendidas:
                        depositar()
                        break;
                      else: 
                        print("\n Lo sentimos, su cuenta esta inhabilitada por favor acuda al centro de atencion mas cercano")
                    if opcion == 3:
                      usuario = clientes[k]
                      if not usuario in suspendidas:
                        retirar()
                        break;
                      else: 
                        print("\n Lo sentimos, su cuenta esta inhabilitada por favor acuda al centro de atencion mas cercano")        
                    if opcion == 4:
                      print("Has finalizado el programa")
                      break;
                  else:
                    print("no has ingresado ninguna de las opciones")
              else: 
                  print("\nContraseña incorrecta")
              break;                
          elif cuenta != clientes[0][0] and cuenta != clientes[1][0] and cuenta != clientes[2][0] :
            error +=1
      if error == 4:
        print("no hay cuenta asociada a ese codigo")
    if cuenta == 0:
      print("Has finalizado el programa")
      break;

Banco()