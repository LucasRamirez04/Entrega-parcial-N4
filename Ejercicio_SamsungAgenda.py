"""
EJ 1:
Samsung nos acaba de contratar para realizar el directorio de su ultimo telefono el cual maneja el lenguaje de python 
nos solicita que esta aplicacion almacene el nombre, apellido, direccion, fecha de cumpleaños y una nota de solo 50 caracteres
esta agenda o lista de contactos debe poderse editar,guardar,modificar
resuelva las dificultades de dicho caso.

"""
def mostrar_menu():
    print("\n--- MENU OPCIONES ---")
    print("[1] Agregar nuevo cliente")
    print("[2] Editar datos")
    print("[3] Guardar datos y salir")

agenda = []

while True:
    mostrar_menu()
    opcion = input("Elija una opción (1/2/3): ")

    match opcion:
        case "1":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese el apellido: ")
            direccion = input("Ingrese su dirección: ")
            fecha_cumpleaños = input("Ingrese su fecha de cumpleaños (formato: dd/mm/aaaa): ")

            while True:
                nota = input("Ingrese su nota (máx. 50 caracteres):\n")
                if len(nota) <= 50:
                    break
                else:
                    print("Error: La nota excede el límite de caracteres.")

            directorio = {
                "nombre": nombre,
                "apellido": apellido,
                "direccion": direccion,
                "fecha cumpleaños": fecha_cumpleaños,
                "nota": nota
            }

            agenda.append(directorio)
            print("Contacto agregado correctamente.")

        case "2":
            if not agenda:
                print("La agenda está vacía. Agrega contactos primero.")
                continue

            nombre_buscado = input("Ingrese el nombre del contacto que desea editar: ")
            contacto_encontrado = None
            for contacto in agenda:
                if contacto["nombre"].lower() == nombre_buscado.lower():
                    contacto_encontrado = contacto
                    break

            if not contacto_encontrado:
                print("No se encontró ningún contacto con ese nombre.")
                continue

            print(f"\nEditando a: {contacto_encontrado['nombre']} {contacto_encontrado['apellido']}")
            print("¿Qué desea editar?")
            print("[1] Nombre")
            print("[2] Apellido")
            print("[3] Dirección")
            print("[4] Fecha de cumpleaños")
            print("[5] Nota")
            print("[6] Cancelar")

            opcion_editar = input("Seleccione una opción (1-6): ")
            match opcion_editar:
                case "1":
                    contacto_encontrado["nombre"] = input("Nuevo nombre: ")
                case "2":
                    contacto_encontrado["apellido"] = input("Nuevo apellido: ")
                case "3":
                    contacto_encontrado["direccion"] = input("Nueva dirección: ")
                case "4":
                    contacto_encontrado["fecha cumpleaños"] = input("Nueva fecha de cumpleaños (dd/mm/aaaa): ")
                case "5":
                    while True:
                        nueva_nota = input("Nueva nota (máx. 50 caracteres):\n")
                        if len(nueva_nota) <= 50:
                            contacto_encontrado["nota"] = nueva_nota
                            break
                        else:
                            print("Error: La nota excede los 50 caracteres.")
                case "6":
                    print("Edición cancelada.")
                case _:
                    print("Opción no válida.")

        case "3":
            try:
                with open("agenda_samsung.txt", "w", encoding="utf-8") as archivo:
                    for contacto in agenda:
                        archivo.write(f"Nombre: {contacto['nombre']}\n")
                        archivo.write(f"Apellido: {contacto['apellido']}\n")
                        archivo.write(f"Dirección: {contacto['direccion']}\n")
                        archivo.write(f"Fecha de cumpleaños: {contacto['fecha cumpleaños']}\n")
                        archivo.write(f"Nota: {contacto['nota']}\n")
                        archivo.write("-" * 40 + "\n")
                print("Datos guardados correctamente en 'agenda_samsung.txt'.")
            except Exception as e:
                print("Error al guardar el archivo:", e)
            break

        case _:
            print("Opción inválida. Intente nuevamente.")