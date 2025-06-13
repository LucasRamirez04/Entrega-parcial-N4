lista_usuarios = []
def registrar_nombre(lista_usuarios):
    while True:
        nombre = input("Ingrese el nombre de usuario: ")
        nombre_ya_registrado = False
        for usuario in lista_usuarios:
            if usuario["nombre"] == nombre:
                nombre_ya_registrado = True
                break
        if nombre_ya_registrado:
            print("Ese nombre ya se encuentra registrado\nIntente nuevamente")
        else:
            print("Nombre registrado con exito✅")
        if not nombre.strip():
            print("❌ El nombre no puede estar vacío.\n")
            continue
        return nombre
def registrar_sexo():
    while True:
        lista_sexos = ["F","M"]
        sexo = input("Ingrese su sexo (F o M): ").upper().strip()
        if sexo in lista_sexos:
            print("Sexo registrado exitosamente✅")
            break
        else:
            print("Error: Intente nuevamente ingresando F o M")
    return sexo
def registrar_clave():
    while True:
        clave = input("Ingrese una clave (mínimo 8 caracteres, con al menos una letra y un número, sin espacios): ")
        if len(clave) < 8:
            print("❌ La clave debe tener al menos 8 caracteres.\n")
            continue

        if ' ' in clave:
            print("❌ La clave no debe contener espacios.\n")
            continue

        tiene_letra = any(c.isalpha() for c in clave)
        tiene_numero = any(c.isdigit() for c in clave)

        if not tiene_letra:
            print("❌ La clave debe contener al menos una letra.\n")
            continue

        if not tiene_numero:
            print("❌ La clave debe contener al menos un número.\n")
            continue

        print("Clave registrada exitosamente ✅.\n")
        return clave



while True:
    print("==========================================")
    print("BIENVENIDO AL PROGRAMA 'LISTA DE USUARIO'")
    print("==========================================\n")
    print("--- MENU DE OPCIONES ---")
    print("[1]. Ingresar usuario")
    print("[2]. Buscar usuario")
    print("[3]. Eliminar usuario")
    print("[4]. Salir del programa")
    op = input("Elija una opción (1/2/3/4): ")
    if op == "1": 
        print("REGISTRO DE USUSARIO")
        usuario = {}
        usuario["nombre"] = registrar_nombre(lista_usuarios)
        usuario["sexo"] = registrar_sexo()
        usuario["clave"] = registrar_clave()
        print(f"Se ha registrado exitosamente el usuario\n{usuario}")
        lista_usuarios.append(usuario)
        
    elif op == "2":
        print("BUSQUEDA DE USUARIO")
        usuario_buscado = input("Ingrese el nombre de usuario a buscar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario["nombre"] == usuario_buscado:
                print("Usuario encontrado✅")
                print(f"Nombre de usuario: {usuario['nombre']}")
                print(f"Sexo del usuario: {usuario['sexo']}")
                encontrado = True
        if not encontrado:
            print("No se ha encontrado ese nombre de usuario")

    elif op == "3":
        print("ELIMINAR USUARIO")
        usuario_buscado = input("Ingrese el nombre de usuario a buscar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario["nombre"] == usuario_buscado:
                print("Usuario encontrado✅")
                encontrado = True
                while True:
                    confirmacion = input(f"Estás segur@ que quieres eliminar el usuario {usuario['nombre']} (S/N): ").upper()
                    if confirmacion == "S":
                        lista_usuarios.remove(usuario)
                        print(f"Se ha elinado el usuario correctamente")
                        break
                    elif confirmacion == "N":
                        print("Cancelando eliminación, volviendo...")
                        break
                    else:
                        print("Opcion invalida, intento con S o N")
                break
        if not encontrado:
            print("No se ha encontrado ese nombre de usuario")

    elif op == "4":
        salir = False
        while True:
            confirmacion = input(f"Estás segur@ que quieres salir del sistema(S/N): ").upper()
            if confirmacion == "S":
                salir = True   
                break           
            elif confirmacion == "N":
                print("Vollviendo al menu principal...")
                break
            else:
                print("Opcion invalida, intento con S o N")
        if salir:
            print("Saliendo del sistema, Hasta pronto")
            break

    else:
        print("Error: Se ha ingresado una opción invalida, intente con (1/2/3/4)")