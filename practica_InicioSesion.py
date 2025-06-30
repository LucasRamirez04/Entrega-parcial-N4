def validar_clave(clave):
    tiene_mayuscula = any(c.isupper() for c in clave)
    tiene_minuscula = any(c.islower() for c in clave)
    tiene_numero = any(c.isdigit() for c in clave)
    especiales = ["+","-","*","#",",","."]
    tiene_especial = any(c in especiales for c in clave)
    largo = len(clave) >= 8 
    
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial and largo:
        return True
    else: 
        return False
usuarios = []    
print("BIENVENIDO A LA CALCULADORA PRO 5000")
while True:
    print("\n--- INICIO DE SESIÓN ---")
    print("[1]. Inicio de sesión")
    print("[2]. Registro de usuario")
    print("[3]. Salir")
    opcion = input("Elija una opción (1/2/3): ")
    match opcion:
        case "1":
            print("--- INICIO DE SESIÓN ---")
            if not usuarios:
                print("No hay usuarios registrados aún. Registre uno primero para poder iniciar sesíon")
                continue
            while True:
                nombre_usuario = input("Ingrese usuario (0 para cancelar inicio de sesión): ")
                if nombre_usuario == "0":
                    print("Cancelando operación, Volviendo al menú principal...")
                    break

                usuario_encontrado = None
                for usuario in usuarios:
                    if usuario["nombre"] == nombre_usuario:
                        usuario_encontrado = usuario
                        print("Usuario encontrado✅")

                if usuario_encontrado is None:
                    print("Usuario no encontrado❌, intente nuevamente")
                    continue

                for i in range(3):
                    contraseña_usuario = input("CONTRASEÑA (0 si quiere cancelar): ")
                    if contraseña_usuario == "0":
                        print("Cancelando operación, Volviendo al menú principal...")
                        break

                    if usuario_encontrado["contraseña"] == contraseña_usuario:
                        print("Sesión iniciado exitosamente✅")
                        break
                        #Calculadora iniciada
                    if i < 2:
                        print(f"Le quedan {2-i} intentos")
                    else: 
                        print("Ha superado el número maximo de intentos")
                break    

        case "2":
            while True:
                print("\n--- REGISTRO DE USUARIO ---")
                nombre_registro = input("Registre un nombre de usuario: ")
                existe = any(u["nombre"] == nombre_registro for u in usuarios)
                if existe:
                    print("Ese nombre de usuario ya esta registrado, intente nuevamente")
                    continue
                else:
                    print("Nombre de usuario registrado correctamente✅")
                    break
            while True:
                print("\n--- REGISTO CONTRASEÑA ---")
                print("\n*** Requisitos contraseña ***")
                print('Letra mayuscula\nLetra minuscula\nNumero\nCaracter especial (+) (-) (*) (#) (,) (.)\nLargo min 8 caracteres\n')
                contraseña_registro = input("Registre una contraseña: ")
                if validar_clave(contraseña_registro):
                    for i in range(3):
                        confirmar_contraseña = input("Ingrese nuevamente su contraseña: ") 
                        if confirmar_contraseña == contraseña_registro:
                            print("Contraseña registrada exitosamente✅")
                            usuarios.append({"nombre": nombre_registro, "contraseña" : confirmar_contraseña})
                            break   
                        else:
                            if i < 2:
                                print(f"Le quedan {2-i} intentos para confirmar la contraseña")
                            else:
                                print("\nHa llegado al limite de intentos, Volviendo al menú principal...")
                                break
                    break

                else:
                    print("La contraseña no cumple con los requisitos, intente nuevamente")

        case "3":
            while True:
                print("\n--- SALIR ---")
                pregunta_confirmacion = input("Esta segur@ que quiere salir del programa (s/n): ").lower()
                if pregunta_confirmacion == "s":
                    confirmacion = True
                    break
                elif pregunta_confirmacion == "n":
                    confirmacion = False
                    break
                else:
                    print("Opción ingresada inválida, intente con (s/n): ")

            if confirmacion:
                print("Saliendo del sistema, Hasta pronto👋👋👋")
                break
            else:
                print("Cancelando operación❌, Volviendo al menú principal...")     