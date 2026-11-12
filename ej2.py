maquinas = 25

UsoEquipo = 0
desusoequipo = 0

while(maquinas > 0):
    
    print("=== MENÚ PRINCIPAL === ")
    print("1.- Equipos disponibles. ")
    print("2.- Asignar equipo. ")
    print("3.- Liberar equipo. ")
    print("4.- Historial de usos. ")
    print("5.- Salir. ")
    opcion = int(input("Ingrese una de las opciones del menu: "))
    
    while (opcion < 1 or opcion > 5):
        
        print("Ingrese una opcion valida.")
        
        opcion = int(input("Ingrese una de las opciones del menu: "))
        
    match opcion:
        
            case 1:
                print(f"Stock diponible de equipos en el laboratorio: {maquinas}")
            case 2:
                UsoEquipo = input("Ingrese la cantidad de equipos que se va a asignar: ")
                if UsoEquipo.strip() == "":
                    print("Error, no debe dejar el espacio en blanco.")
                if " " in UsoEquipo:
                    print("Error, no debe tener espacios.")

                elif not UsoEquipo.isdigit():
                    print("Error, solo puede ingresar numeros.")
                else:
                    UsoEquipo = int(UsoEquipo)

                    if UsoEquipo <= 0:
                        print("Error, ingrese numeros mayores a 0.")
                    elif UsoEquipo > maquinas:
                        print("La cantidad que se solicita es mayor al stock disponible, intentelo de nuevo.")
                    else:
                        maquinas = maquinas - UsoEquipo
            case 3:
                desusoequipo = int(input("Ingrese la cantidad de equipos que ya no usara: "))
                if desusoequipo >0:
                    maquinas = maquinas + desusoequipo
                elif UsoEquipo == 0:
                    print("Error, no se ingreso uso de equipos.")
            case 4:
                print(f"[ Equipo solicitado durante el dia: {UsoEquipo} ]")
                print(f"[ Equipo que se devolvio durante el dia: {desusoequipo} ]")
            case 5:
                print("Gracias por utilizar nuestro software, hasta la próxima." )
                break
            case _:
                print("Error, ingrese una opcion valida del menu.")