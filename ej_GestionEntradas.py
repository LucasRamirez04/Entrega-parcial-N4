"""
Realice un programa que permita realizar un menu de gestion de entradas para el concierto de 'Noche de brujas'
El munu principal debe mostrar 4 opciones:

opcion 1: Comprar entradas
    Se debe permitir el nombre del comprador
    Tipo de entrada 
    codigo de confirmación

    *Para que la comopra sea exitosa*
    a) Nombre del comprador no puede repetirse
    b) Tipo de entrada debe ser general(10K) o VIP(50K)
    c) El codigo de confirmación debe tener un min de 6 caracteres, un numero o una letra mayus o min,  y sin espacios

opcion 2: Consultar compradores
    Debe permitir buscar comprador mediante el nombre:

    Si el comprador existe, mostrar datos asociados:
        Nombre,tipo y codigo de verificación
    Si no existe, mostrar:
        'Comprador no existe'

opcion 3: Cancelar compra
    
    Debe permitir mostrar una opción que le permita eliminar un comprador con toda su información asociada

opcione 4: 'Continuar comprando o salir del sistema'
    
    Mostrar mensaje si es que desea seguir comprando o desea salir del programa

*Todas las opciones del menu deben estar implementadas mediante funciones, separadas del codigo principal (MAIN)*
"""
def Comprar_entradas(lista):
    import random
    venta = {}
    #Registro de nombre del comprador
    while True:
        nombre_comprador = input("Ingrese el nombre del comprador: ")
        repetido = False
        for ventas in lista:
            if ventas["nombre"] == nombre_comprador:
                repetido = True
        if not nombre_comprador.strip():
            print("Error: El nombre no puede estar vacio, intente nuevamente")
        elif repetido:
            print("Ese nombre ya se encuencuentra registrado, intente nuevamente")
        else:            
            venta['nombre'] = nombre_comprador
            break
    #Registro de cantidad y tipo de entradas
    Total = 0
    while True:
        tipo_entradas = input("Ingrese el tipo de entrada a comprar\n1.General ($10.000)\n2.VIP ($50.000)\n('0' si no quiere comprar más): ")
        if tipo_entradas == "1":
            while True:
                try:    
                    print("ENTRADA GENERAL")
                    cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))
                    Total += 10000 * cantidad
                    venta['Entrada General'] =  venta.get('Entrada General',0) + cantidad
                    print("Se agregaron las entradas con exito✅")
                    break
                except:
                    print("Error: debe ingresar una cantidad valida")
        elif tipo_entradas == "2":
            while True:
                try:    
                    print("ENTRADA VIP")
                    cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))
                    Total += 50000 * cantidad
                    venta['Entrada VIP'] = venta.get('Entrada VIP',0) + cantidad
                    print("Se agregaron las entradas con exito✅")
                    break
                except:
                    print("Error: debe ingresar una cantidad valida")
        elif tipo_entradas == "0":
            print(f"Total a pagar {Total}")
            break
        else:
            print("Opcion invalida, intente con (1/2/0)")
    #COdigo de confirmacion 
    codigo_de_confirmacion = "VER"
    for i in range(3):
        num = random.randint(0,9)
        codigo_de_confirmacion += str(num)
    print(f"Su codigo de verificación de la compra es {codigo_de_confirmacion}")
    print("❗❗❗NO LO OLVIDE, SE LE PEDIRA AL ENTRAR AL RECINTO❗❗❗")
    venta['codigo verificacion'] = codigo_de_confirmacion
    print("Venta registrada con exito✅")

    return venta

def Consultar_entradas(lista):
    if lista:
        nombre_buscado = input("Ingrese el nombre del usuario a buscar: ")
        encontrado = False
        for ventas in lista:
            if ventas['nombre'] == nombre_buscado:
                print('Usuario encontrado✅')
                print("\n--- Resumen de compra ---")
                print(f"Nombre: {ventas['nombre']}")
                print(f"Entradas compradas\nEntradas Generales: {ventas.get('Entrada General', 0)}\nEntradas VIP: {ventas.get('Entrada VIP', 0)}")
                print(f"Codigo de verificación: {venta['codigo verificacion']}")
                encontrado = True
        if not encontrado:
            print("Usuario no encontrado❌, volviendo al menú principal...")
    else:
        print("Todavia no se han registrado ventas, volviendo al menú principal...")

def Cancelar_compra(lista):
    if lista:
        nombre_buscado = input("Ingrese el nombre del usuario a buscar: ")
        encontrado = False
        for ventas in lista:
            if ventas['nombre'] == nombre_buscado:
                print('Usuario encontrado✅')
                print("\n--- Resumen de compra ---")
                print(f"Nombre: {ventas['nombre']}")
                print(f"Entradas compradas\nEntradas Generales: {ventas.get('Entrada General', 0)}\nEntradas VIP: {ventas.get('Entrada VIP', 0)}")
                print(f"Codigo de verificación: {venta['codigo verificacion']}\n")
                encontrado = True
                while True:
                    confirmacion = input("Desea eliminar esta venta (S/N): ").upper()
                    if confirmacion == "S":
                        lista.remove(venta)
                        print("Venta eliminada exitosamente")
                        break 
                    elif confirmacion == "N":
                        print("Cancelando eliminación...")
                        break
                    else:
                        print("Opción inválida, intente con (S/N)")
                break
        if not encontrado:
            print("Usuario no encontrado❌, volviendo al menú principal...")
    else:
        print("Aún no se han registrado ventas, volviendo al menú principal...")

def Confirmar_salida():
    while True:
        salir = input("Desea seguir comprando (S/N): ").upper()
        if salir == "S":
            print("Volviendo al menú principal...")
            return False
        elif salir == "N":                
            return True
        else:
            print("Opción inválida, intente con (S/N)")

lista_ventas = []
while True:
    print("\nBIENVENIDO AL PROGRAMA DE VENTA DE ENTRADAS PARA 'NOCHE DE BRUJAS'\n")
    print("--- MENU DE OPCIONES ---")
    print("[1]. Comprar entradas")
    print("[2]. Consultar compradores")
    print("[3]. Cancelar compra")
    print("[4]. Salir ")
    op = input("Elija una opción: ")

    if op == "1":
        venta = Comprar_entradas(lista_ventas)
        lista_ventas.append(venta)

    elif op == "2":
        Consultar_entradas(lista_ventas)
    
    elif op == "3":
        Cancelar_compra(lista_ventas)

    elif op == "4":
        fin = Confirmar_salida()
        if fin:
            print("Saliendo del sistema...👋👋👋")
            break   
    
    else:
        print("Opción inválida, intente con (1/2/3/4)")