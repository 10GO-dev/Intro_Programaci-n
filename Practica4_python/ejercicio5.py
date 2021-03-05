'''
Crear una aplicación que se ingrese por teclado el nombre de 5 empleados, 
sueldo cobrado por cada empleado en los ultimos 3 meses.
Mostrar en pantalla el total pagado a cada empleado en los
ultimos 3 meses obtener y mostrar cual fue el empleado de mayor ingreso."
'''

Empleados = []
Sueldo = []

def sueldo_mayor():
    if max(Sueldo) == Sueldo[0]:
        print("\nEl empleado de mayor ingreso fue",Empleados[0])
        
    if max(Sueldo) == Sueldo[1]:
        print("\nEl empleado de mayor ingreso fue",Empleados[1])
        
    if max(Sueldo) == Sueldo[2]:
        print("\nEl empleado de mayor ingreso fue",Empleados[2])
        
    if max(Sueldo) == Sueldo[3]:
        print("\nEl empleado de mayor ingreso fue",Empleados[3])
        
    if max(Sueldo) == Sueldo[4]:
        print("\nEl empleado de mayor ingreso fue",Empleados[4])

for x in range(5):
    print("\n------------------------------------------------------------------\n")
    nombre_empleado = input("Ingresa el nombre de un empleado: ")
    sueldo_empleado = int(input("Ingresa el sueldo cobrado en los ultimos 3 meses: "))
    Empleados.append(nombre_empleado)
    Sueldo.append(sueldo_empleado)
sueldo_mayor()
        






