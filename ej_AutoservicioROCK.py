"""
EJ:
La gran cadena de autoservicio ROCK requiere de su servicio para desarrollar su nueva app,
a continuacion realice un programa que permita generar un menú de gestion de entrada para que girar rock
Que permita realizar las distintas compras a nvl nacional del autoservicio en chile.
El menú principal debe tener 2 opciones:

op 1 Ingresar Usuario
    ID 
    Nombre
    Comprar servicio:
        Servicio de frenos
        Engrasado
        Lavado
        Pulitura
        Especial (Todas los servicio juntos)

op 2 Ubicaciones
    1. Concepcion
    2. Puente Alto
    3. Muelle Varon (Valdivia)
    4. Muelle Vergara (Viña)
    5. Continuar añadiendo o salir

"""
def validar_rut(rut):
    rut = rut.replace(".", "").upper()

    if "-" not in rut:
        print("Rut inválido, falta el guion")
        return False

    partes = rut.split("-")
    if len(partes) != 2:
        print("Rut inválido, formato incorrecto")
        return False

    cuerpo, verificador = partes

    if not cuerpo.isdigit():
        print("Rut inválido, no se permiten letras en el rut (solo 'k' en el digito verificador)")
        return False

    if not (verificador.isdigit() or verificador == "K"):
        print("Rut inválido, el dígito verificador debe ser numérico o 'K'")
        return False
    
    if len(rut) != 10:
        print("Rut inválido, no cumple con el numero de caracteres correspondientes")
        return False

    return True

print("BIENVENIDO AL PROGRAMA DE GESTIÓN DE VENTAS DE ROCK")
while True:
    print("\n--- MENU DE OPCIONES ---")
    print("[1]. Nueva venta")
    print("[2]. Revisar última venta")
    print("[3]. Salir del programa")
    opcion = input("Elija una opción (1/2/3): ")
    match opcion:
        case "1":
            venta = {}
            while True:
                rut = input("Ingrese su numero de Rut (12345678-9): ")
                if validar_rut(rut):
                    print("Rut ingresado correctamente✅")
                    venta["Rut"] = rut                    
                else:
                    print("Intente nuevamente (0 si quiere cancelar la operación): ")
                    continue
                if rut == "0":
                    print("Volviendo al menú principal...")
                    break
                venta["nombre"] = input("Ingrese su nombre: ")

                servicios = {"1":"Servicio de frenos",
                                "2":"Engrasado",
                                "3":"Lavado",
                                "4":"Pulitura",
                                "5":"Especial" 
                                }
                print("--- LISTA DE SERVICIOS ---")
                for opciones,servicio in servicios.items():
                    print(f"{opciones}. {servicio}")
                while True:
                    opcion_servicios = input("Elija el servicio a contratar (1/2/3/4/5)\nRecuerde que el servicio especial consta de todos los servicios\n")
                    if opcion_servicios in servicios:
                        print(f"Servicio: {servicios[opcion_servicios]} ingresado correctamente")
                        break
                    else:
                        print("Error: Valor ingresado no se encuentra entre las opciones\nIntente nuevamente con (1/2/3/4/5): ")
                
                ubicaciones = {
                    "1" : "Concepción",
                    "2" : "Puente alto",
                    "3" : "Muelle Varon (Valdivia)",
                    "4" : "Muelle Vergara (Viña)"
                }

                print("--- Opciones de ubicaciones ---")
                ubicacion = input("")



