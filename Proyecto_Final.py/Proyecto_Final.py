import os #libreria para utilizar funciones del sistema. 
import pandas as pd #libreria para manejar datos mediante tablas 
from datetime import date as d #libreria de python para trabajar con las fechas

os.system('cls') #Limpiar la consola

#Estas variables son para dar formato a las tablas
Tasa = " {} %|"
Meses = " {} Meses|"
Moneda = " RD$ {}|"
Numero = " {} |"

class Prestamo: #Clase principal prestamo

    def __init__(self): #Atributos
        self.monto =""
        self.plazo_meses = ""
        self.tasa_interes = ""
        self.solicitud = 0   #Para diferenciar menus. 
        
    def Cuota_Mensual(self): #funcion para calcular la cuota y mostrar la tabla con la información correspondiente.
        '''
        ---------------------------------------------------------------------------

                        m*(i*((1 + i)^p) / (((1 + i)^p)* – 1))

                      m= Monto | i = tasa_interes | p = plazo_meses
        ---------------------------------------------------------------------------              
        '''
        #aqui aplique la formula para obtener la cuota mensual con sus respectivas variables y la tasa de interes anual mensualizada.
        self.Cuota = self.monto*(((self.tasa_interes/12)/100*(1+(self.tasa_interes/12)/100)**self.plazo_meses)/
        ((1+(self.tasa_interes/12)/100)**self.plazo_meses-1))
        #---------------------------------------------------------------
        self.Datos_Cuota = { #Diccioncio para utilizar como tabla con la libreria pandas.
            "| Monto del prestamo en RD$:":Numero.format(round(self.monto,2)),        
            "| Tasa de Porcentaje Anual:":Tasa.format(round(self.tasa_interes,2)),
            "| Plazo(meses):":Meses.format(int(self.plazo_meses)),
            "| Valor Cuota:":Moneda.format(round(self.Cuota,2)),
            }
        info_cuota = pd.Series(self.Datos_Cuota) #Aqui convierto el diccionario de arriba en una tabla tipo seria. (es como una tabla de una sola columna).
        os.system('cls') #limpio la consola 
        print("=====================--P R E S T A M O S--====================\n")
        print(info_cuota) #imprimo la tabla con la informacion de la cuota.
        print("==============================================================")
        self.Amortización() #Ejecuto la función amortización.
        
    def Amortización(self): #funcion para crear la tabla de Amortización. 
        
        self.datos_Amortizacion = { #Diccionario para crear la tabla de Amortización.
            "Pago ":[],
            "Fechas de Pago ":[],                      #|\
            "Cuota ":[],                               #| \
            "Capital ":[],                             #|  )> Estos vendrian siendo los campos 
            "Interés ":[],                             #| /
            "Balance ":[],                             #|/
        }

        #Bucle para rellenar la tabla
        fecha = d.today() #Variable con la fecha de actual.
        self.fecha_pago = d(fecha.year,fecha.month,fecha.day) #variable para asignar las fechas de pago.
        self.pago = 1 #variable para contar los pagos.
        self.interes = ((self.tasa_interes/12)/100)*self.monto #calcular interes mensual
        self.capital = (self.Cuota-self.interes) #Calcular el capital
        self.monto -= (self.Cuota-self.interes) #Caluclar el balance del prestamo

        for x in range(self.plazo_meses):#Bucle para agregar los datos a la tablas 
            self.datos_Amortizacion["Pago "].append(Numero.format(self.pago)) #Agrega los pagos
            self.datos_Amortizacion["Fechas de Pago "].append((self.fecha_pago.strftime(" %d-%b-%Y|")))#Agrega la fecha de pago
            self.datos_Amortizacion["Cuota "].append(Moneda.format(round(self.Cuota,2))) #Agrega la cuota.
            self.datos_Amortizacion["Capital "].append(Moneda.format(round(self.capital,2))) #Agrega el capital.
            self.datos_Amortizacion["Interés "].append(Moneda.format(round(self.interes,2))) #Agrega el Interés Mensual.
            self.datos_Amortizacion["Balance "].append(Moneda.format(round(self.monto,2))) #Agrega el balance.
            self.pago += 1 #incrementa la variable pago. 

            if self.fecha_pago.month == 12: #Condición para aumentar una año cada vez que el mes sea igual a 12
                self.fecha_pago = self.fecha_pago.replace(year=self.fecha_pago.year + 1,month=1)
            else: #si la condicion de arriba no se cumple solo aumenta el mes
                self.fecha_pago = self.fecha_pago.replace(month=self.fecha_pago.month + 1)

            self.interes = ((self.tasa_interes/12)/100)*self.monto #Calcula el interes nuevamente
            self.capital = self.Cuota-self.interes                 #Calcula el capital nuevamente
            self.monto -= self.capital                             #Calcula el Balance nuevamente

        tabla_amortizacion = pd.DataFrame(self.datos_Amortizacion) #convierto el diccionario de arriba en una tabla. 

        print("\n=====================--Tabla de Amortización--=============================")
        print(tabla_amortizacion.to_string(index=False,justify='center')) #imprimo la tabla de Amortizacion
        print("===========================================================================")


    def Solitar_prestamo(self): #Funcion para solicitar los datos del prestamo a calcular.
        self.monto = float(input("\nIngresa el monto del prestamo: ")) #Ingreso el monto del prestamo
        self.plazo_meses = int(input("\nIngrese el plazo en meses: ")) #ingreso el plazo en meses
        self.tasa_interes = float(input("\nIngrese la tasa de interés anual: ")) #Ingreso la tasa de interes anual
        self.Cuota_Mensual() #Ejecuta la funcion Cuota Mensual, para calcular esta.
        self.solicitud += 1 #Incrementa el valor de esta variable la cual utilizo para cambiar una opcion en el menu principal.
        self.Menu()  #Ejecuta la función Menú. 
        
    def Menu(self): #Funcion Menú principal.
        print("==============================================================")
        print("|               CALCULADORA DE PRESTAMOS                     |")       
        print("==============================================================")
        if self.solicitud == 0: #Condicion para volver a calcular un prestamo. 
            print("| 1. Calcular Prestamo.                                     |")
        else: #Si la variable solicitud es mayor a 0 la opcion 1 es diferente.    
            print("| 1. Calcular Nuevo Prestamo.                                |")
        print("| 2. Salir del Sistema.                                      |")
        print("==============================================================")
        while True: #Bucle para seleccionar una opcion
            opcion = int(input("\nSelecciona una Opción: "))  
            if opcion ==1: #opcion 1 Ejecuta la calculadora. 
                os.system('cls')#Limpiar el sistema.
                print("==============================================================")
                print("|               CALCULADORA DE PRESTAMOS                     |")       
                print("==============================================================")
                self.Solitar_prestamo() #Ejecuta la funcion Solicitar_prestamo.
                break #Finaliza el bucle.
            elif opcion == 2: #Opción 2 Finaliza el programa.
                os.system('cls')#Limpiar el sistema.
                print("Has salido del sistema!")
                break #Finaliza el bucle.
            if opcion < 1 or opcion > 2: # Si se ingresa un numero que no corresponde a ninguna opción.
                print("El numero ingresado no corresponde a una opción, Intentalo de nuevo")




Calculadora = Prestamo()
Calculadora.Menu()

