InvestigadoresPrincipales = 0
InvestigadoresAsistentes = 0
registrocientifico = 0
ListaregistroID = []

print("--- Bienvenido al sistema de registro de Cientificos. ---")
registrocientifico = int(input("Cuantos cientificos desea ingresar?: "))
for cientifico in range (registrocientifico):
    publicaciones = int(input("Ingrese la cantidad de publicaciones del cientifico: "))
    if publicaciones <= 0:
        print("“¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.”")
    elif publicaciones > 12:
        print("Cientifico registrado como: Investigador Principal.")
        InvestigadoresPrincipales = InvestigadoresPrincipales + 1
    else:
        print("Cientifico registrado como: Investigador Asistente.")
        InvestigadoresAsistentes = InvestigadoresAsistentes + 1
         
print(f"Numero total de Investigadores Principales: {InvestigadoresPrincipales}")
print(f"Numero total de Investigadores Asistentes: {InvestigadoresAsistentes}")

while len(ListaregistroID) < registrocientifico:
    registroID = input("Ingrese el ID del cientifico: ").upper()
    if " " in registroID:
        print("El registro de ID no debe contener espacios.")
    elif registroID.strip() == "":
        print("El registro de ID no contener espacios en blanco.")
    elif len(registroID) < 12:
        print("EL registro debe tener al menos 12 caracteres.")
                
    else:
        ListaregistroID.append(registroID)
        print("Registro exitoso.")


print(f"ID's registradas exitosamente: {ListaregistroID}")
print(f"“¡El instituto cuenta con {InvestigadoresPrincipales} Investigadores Principales y {InvestigadoresAsistentes} Investigadores Asistentes! ¡Ciencia en marcha!” ")

