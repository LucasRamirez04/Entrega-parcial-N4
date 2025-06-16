"""
EJ:
La fundacion Duoc UC solicita de sus servicios profesisonales para desarrollar un sistema que le permita almacenar los datos personales de 
cada uno de sus estudiantes
como lo son: nombre, apellido, rut, correo electronico, carrera
dentro de carrera estan las siguientes opciones:
ingenieria:
    desarrollo web
    desarrollo movil
    desarrollo escritorio
analista:
    analisis de datos
    limpieza de datos
    creacion de dashboard
gastronomia:
    historia de gastronomia
    alimentos porcesados y no
    sopaipillas II

"""
def agregar_ramos(a,b,c):
    ramos = []
    while True:
        print("\n--- RAMOS ---")
        print(f"[1]. {a}")
        print(f"[2]. {b}")
        print(f"[3]. {c}")
        print(f"[0]. No estoy cursando más ramos")
        eleccion = input("Seleccione los ramos que está cursando (1 x intento): ")
        if eleccion == "1":
            if a not in ramos:
                ramos.append(a)
                print(f"Se ha agregado el ramo {a} a tu lista de ramos")
            else:
                print(f"Ya agregaste {a} a tu lista de ramos")

        elif eleccion == "2":
            if b not in ramos:
                ramos.append(b)
                print(f"Se ha agregado el ramo {b} a tu lista de ramos")
            else:
                print(f"Ya agregaste {b} a tu lista de ramos")
            
        elif eleccion == "3":
            if c not in ramos:
                ramos.append(c)
                print(f"Se ha agregado el ramo {c} a tu lista de ramos")
            else:
                print(f"Ya agregaste {c} a tu lista de ramos")

        elif eleccion == "0":
            print(f"\nTu lista de ramos se ha completado {ramos}")
            break            
    return ramos

lista_estudiantes = []
while True:
    print("\nBienvenido al menu de registro de alumnos DUOC UC")
    print("[1]. Registrar estudiante")
    print("[2]. Salir")
    op = input("Elija una opción (1/2): ")
    if op == "1":
        estudiante = {}
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiante['Nombre'] = nombre
        apellido = input("Ingrese el apellido del estudiante: ")
        estudiante['Apellido'] = apellido
        rut = input("Ingrese el rut del estudiante (formato 12345678-9): ")
        estudiante['Rut'] = rut
        email = input("Ingrese el email del estudiante: ")
        estudiante['Email'] = email
        while True:
            print("\n--- Carreras ---")
            print("[1]. Ingenieria")
            print("[2]. Analista")
            print("[3]. Gastronomia")
            carrera = input("Que carrera está cursando el estudiante (1/2/3): ")
            
            if carrera == "1":
                estudiante['Carrera'] = "Ingenieria"
                ramos = agregar_ramos("Desarrollo Web","Desarrollo Movil","Desarrollo Escritorio")
                estudiante['Ramos'] = ramos
                break
            elif carrera == "2":
                estudiante['Carrera'] = "Analista"
                ramos = agregar_ramos("Analisis De Datos","Limpieza De Datos","Creacion De Dashboard")
                estudiante['Ramos'] = ramos
                break
            elif carrera == "3":
                estudiante['Carrera'] = "Gastronomia"
                ramos = agregar_ramos("Historia de Gastronomia","Alimentos Procesados y No","Sopaipillas II")
                estudiante['Ramos'] = ramos
                break
            else: 
                print("Opción Inválida, intente con (1/2/3)")

        lista_estudiantes.append(estudiante)
        print("\nSe ha inscritos correctamente al estudiante✅\n")

        print("--- Resumen de inscripción ---")
        for key,valor in estudiante.items():
            print(f"{key}: {valor}")
        

    elif op == "2":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción Inválida, intente con (1/2)")



        