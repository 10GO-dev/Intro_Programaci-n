import os 
import pandas as pd

os.system('cls')


class contacto:
    #Constructor
    def __init__(self):
        self.contactos = {"Nombre":[],"Telefono":[],"Mail":[],"Direccion":[]}
        self.cantidad_contactos = 0
    
    #funcion Crear contacto
    def crearContacto(self):
        os.system('cls')
        print("\n---------------------------------------")
        print(" Ingresa los datos del nuevo contacto  ")
        print("---------------------------------------") 
        self.contactos["Nombre"].append(input("Ingresa el nombre: "))          
        self.contactos["Telefono"].append(int(input("Ingresa el telefono: ")))
        self.contactos["Mail"].append(input("Ingresa el Email: "))     
        self.contactos["Direccion"].append(input("Ingresa la direccion: "))
        os.system('cls') 
        print("----------------------------------------\n")
        print("    El contacto se agregó correctamente   ")
        print("----------------------------------------\n")
        self.cantidad_contactos += 1

    #funcion lista contactos
    def listaContactos(self):
        self.Contact_list = pd.DataFrame(self.contactos)
        os.system('cls')
        print("======================================================================")
        print(self.Contact_list)
        print("======================================================================")
        
    #funcion buscar contacto
    def buscarContacto(self):
        global error
        error = 0
        nom = input("| Ingresa el nombre del contacto: ")
        for x in range(len(self.contactos["Nombre"])):
            if nom in self.contactos["Nombre"][x]:
                Buscar = pd.DataFrame(self.contactos)
                os.system('cls')
                print("=========================================================================")
                print(Buscar.loc[x])
                print("=========================================================================")
            else: 
                os.system('cls')
                print("\n-------------------------------------------------------")
                print("\nNo existe un contacto con ese nombre intentalo de nuevo")
                error +=1 

    #funcion modificar contacto
    def modificarContacto(self):
        print("============================================================================")
        print(self.Contact_list)
        print("============================================================================\n")
        
        selectContacto = int(input("Ingresa el numero referente al contacto: "))
        for b in range(self.cantidad_contactos):
             if b == selectContacto:
                os.system('cls')
                print("\n---------------------------------------------------------")
                print("|                   Modificar contacto                   |")
                print("|--------------------------------------------------------|")
                print("|1. Modificar telefono                                   |")
                print("|2. Modificar mail                                       |")
                print("|3. Modificar dirección                                  |")
                print("|4. Cancelar                                             |")
                print("----------------------------------------------------------\n")
                opcion = int(input("Elige el dato a modificar: "))
                if opcion == 1:
                    print("Su telfono actual es: ",self.contactos["Telefono"][b],"\n")
                    self.contactos["Telefono"][b] = int(input("Ingresa el nuevo numero: "))
                    os.system('cls')
                    print("\n------------------------------------------------------")
                    print("        El telefono se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 2:
                    print("Su mail actual es: ",self.contactos["Mail"][b],"\n")
                    self.contactos["Mail"][b] = input("Ingresa el nuevo mail: ")
                    os.system('cls')
                    print("\n------------------------------------------------------")
                    print("        El mail se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 3:
                    print("Su direccion actual es: ",self.contactos["Direccion"][b],"\n")
                    self.contactos["Direcccion"][b] = input("Ingresa la nueva direccion: ")
                    os.system('cls')
                    print("\n------------------------------------------------------")
                    print("        La direccion se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 4:
                    os.system('cls')
                    print("\nHas cancelado la operacion")
        
    #funcion Menu principal
    def Menu(self):
        print("\n====================================================================")
        print("|                           Menu Agenda                            |")   
        print("====================================================================")
        print("| 1. Crear contacto en la agenda.                                  |")
        print("| 2. Listado de contactos.                                         |")
        print("| 3. Buscar contactos.                                             |")
        print("| 4. Modificar contacto.                                           |")
        print("| 5. Finalizar programa.                                           |")
        print("====================================================================\n")

        opcion = int(input("Elige una opcion: "))

        while opcion != 5:
            if opcion == 1:
               os.system('cls')
               self.crearContacto()
               self.Menu()
               break;
            elif opcion == 2:
                os.system('cls')
                self.listaContactos()
                self.Menu()
                break;
            elif opcion == 3:
                os.system('cls')
                print("\n--------------------------------------------------")
                print("                 Buscar contactos                 ")
                print("--------------------------------------------------\n")
                self.buscarContacto()
                if error == self.cantidad_contactos:
                    self.buscarContacto()
                self.Menu()
                break;
            elif opcion == 4:
                os.system('cls')
                self.modificarContacto()
                self.Menu()
                break;
        else:
            os.system('cls')
            print("Programa Finalizado")


#--------------------------BLOQUE PRINCIPAL DEL PROGRAMA---------------------------------------
Agenda = contacto()
Agenda.Menu()