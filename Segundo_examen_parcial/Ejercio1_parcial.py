class contacto:
    #Constructor
    def __init__(self):
        self.nombre = []
        self.telefono = []
        self.mail = []
        self.direccion = []
        self.cantidad_contactos = 0
    
    #funcion Crear contacto
    def crearContacto(self):
        print("\n---------------------------------------")
        print(" Ingresa los datos del nuevo contacto  ")
        print("---------------------------------------")
        self.nombre.append(input("Ingresa el nombre: "))          
        self.telefono.append(int(input("Ingresa el telefono: "))) 
        self.mail.append(input("Ingresa el Email: "))     
        self.direccion.append((input("Ingresa la direccion: ")))  
        print("----------------------------------------\n")
        print("    El contacto se agregó correctamente   ")
        print("----------------------------------------\n")
        self.cantidad_contactos += 1

    #funcion lista contactos
    def listaContactos(self): 
        print("\n___________________________________________________________________________________")
        print("|Nombre               |Telefono         |Mail                 |Direccion           |")
        print("-------------------------------------------------------------------------------------")
        for x in range(self.cantidad_contactos):
            print("|",x,"|",self.nombre[x],"   |",self.telefono[x],"   |",self.mail[x],"   |",self.direccion[x],"   ")
            print("-------------------------------------------------------------------------------------------------")

    #funcion buscar contacto
    def buscarContacto(self):
        global error;
        error = 0
        nom = input("| Ingresa el nombre del contacto: ")
        for x in range(self.cantidad_contactos):
            if self.nombre[x] == nom:
                print("\n|",self.nombre[x],"|",self.telefono[x],"|",self.mail[x],"|",self.direccion[x],"\n")
            else: 
                print("\n-------------------------------------------------------")
                print("\nNo existe un contacto con ese nombre intentalo de nuevo")
                error +=1 

    #funcion modificar contacto
    def modificarContacto(self):
        print("\n")
        for x in range(self.cantidad_contactos):
            print("|",x,"|",self.nombre[x],"   |",self.telefono[x],"   |",self.mail[x],"   |",self.direccion[x],"   ")
            print("-------------------------------------------------------------------------------------------------")
        selectContacto = int(input("Ingresa el numero referente al contacto: "))
        for b in range(self.cantidad_contactos):
             if b == selectContacto:
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
                    self.telefono[b] = int(input("Ingresa el nuevo numero: "))
                    print("\n------------------------------------------------------")
                    print("        El telefono se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 2:
                    self.mail[b] = input("Ingresa el nuevo mail: ")
                    print("\n------------------------------------------------------")
                    print("        El mail se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 3:
                    self.direccion[b] = input("Ingresa la nueva direccion: ")
                    print("\n------------------------------------------------------")
                    print("        La direccion se modifico correctamente")
                    print("\n------------------------------------------------------")
                elif opcion == 4:
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
               self.crearContacto()
               self.Menu()
               break;
            elif opcion == 2:
                self.listaContactos()
                self.Menu()
                break;
            elif opcion == 3:
                print("\n--------------------------------------------------")
                print("                 Buscar contactos                 ")
                print("--------------------------------------------------\n")
                self.buscarContacto()
                if error == self.cantidad_contactos:
                    self.buscarContacto()
                self.Menu()
                break;
            elif opcion == 4:
                self.modificarContacto()
                self.Menu()
                break;
        else:
            print("Programa Finalizado")


#--------------------------BLOQUE PRINCIPAL DEL PROGRAMA---------------------------------------
Agenda = contacto()
Agenda.Menu()