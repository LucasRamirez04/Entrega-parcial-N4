"""
SISTEMA DE GESTION DE RESERVAS DE HOTEL

1.REGISTRAR RESERVA
    DATOS SOLICITADOS:
    - Identificador unico de reserva
    - Nombre del huésped
    - N° habitacion (entre 101 y 999)
    - Tipo de habitacion (Individual,Doble,Suite)
    - Días de estadia (entero positivo, min 1 día)

    CALCULOS AUTOMÁTICOS:
    - Costo Total (Individual: $50/dia, Doble: $80/dia, Suite: $120/dia)

    VALIDACIONES:
    - Identificador de reserva (Debe contener letras y numeros )
    - Nombre del Huesped (no puede estar vacío)
    - Días de estadias válidos (>= 1)
    - La habitacíon debe estar libre al momento de reservar

2.BUSCAR RESERVA
 - ID de reserva
   Mostrar:
   ID: [ID reserva]
   Huesped: [Nombre]
   Habitacion: [Número][Tipo]
   Dias: [Cantidad]
   Total: [Costo]

3.MODIFICAR RESERVA
    PROCESO:
    1. Buscar ID
    2. Permitir cambiar: 
        - Tipo de habitacíon
        - Días de estadía 
    3. Recalcular costo automáticamente

    VALIDACIÓNES:
    - Nueva conf. debe ser válida
    - Días >= 1

4.CANCELAR RESERVA:
    - ID RESERVA
    - ELIMINAR RESERVA 
    - CONFIRMACIÓN 
        print("Reserva cancelada exitosamente")
        
5. MOSTRAR TODAS LAS RESERVAS:
    FORMATO:
    [ID] - HAB.[numero]-[Huesped](dias: X,Total: $Y)

6. SALIR
    Finalizar programa

"""

def registro_id_reserva(reservas:list):
    while True:
        id_reserva = input("Ingrese el id de reserva (tiene que tener numeros y letras): ")

        id_repetido = False
        for reserva in reservas:
            if reserva["ID"] == id_reserva:
                print("Ese id ya está en uso, intente con uno nuevo")
                id_repetido = True
                break

        if id_repetido:
            continue

        tiene_letra = any(c.isalpha() for c in id_reserva)
        tiene_numero = any(c.isdigit() for c in id_reserva)

        if tiene_letra and tiene_numero:
            print("Id de reserva valido✅")
            return id_reserva
        
        if not tiene_letra:
            print("Le falta agregar alguna letra al id de reserva")
            continue

        if not tiene_numero:
            print("Le falta agregar algun número al id de reserva") 
            continue

def registro_nombre_huesped():
    while True:
        nombre = input("Ingrese el nombre del huesped: ")
        if len(nombre) == 0:
            print("El nombre no puede estar vacio, intente nuevamente")
            continue

        tiene_numero = any(c.isdigit() for c in nombre)

        if tiene_numero:
            print("El nombre no puede contener números")
            continue

        return nombre
    
def registro_n_habitacion(reservas:list):
    while True:
        try:
            n_habitacion = int(input("Ingrese el número de la habitacion a reservar (101-999): ").strip())

            if n_habitacion not in range(101,1000):
                print("Numero de habitación inválido")
                continue

            n_encontrado = False         
            for reserva in reservas:
                if reserva["número"] == n_habitacion:
                    n_encontrado = True

            if n_encontrado:
                    print("Esa habitacion se encuentra ocupada, intente con otra")
                    continue
            else:
                print("Se ha registrado correctamente en número de habitacion✅")
                return n_habitacion
         

        except ValueError:
            print("Error: Tiene que ingresar un número entero válido")

def registro_tipo_habitacion():
    while True:
        tipos = ["individual","doble","suite"]
        tipo = input("Ingrese el tipo de habitacion a reservar (individual/doble/suite): ").lower().strip()
        if tipo in tipos:
            print("Tipo seleccionado correctamente✅")
            return tipo
        else:
            print("El tipo ingresado no se encuentra entre las opciones, intente nuevamente con (individual/doble/suite)")

def registro_dias():
    while True:
        try:
            dias = int(input("Ingrese los dias de estadía: ").strip())
            if dias > 0:
                print("Dias ingresados correctamente✅")
                return dias
            else:
                print("La cantidad de dias debe ser mayor a 0, intente nuevamente")
        except ValueError:
            print("Error: El valor ingresado debe ser un numero entero")

def calculo_costo(tipo,dias):
    if tipo == "individual":
        return dias * 50
    elif tipo == "doble":
        return dias * 80
    elif tipo == "suite":
        return dias * 120

def buscar_reserva(id,lista):  
    reserva_buscada = None
    for reserva in lista:
        if reserva["ID"] == id:
            reserva_buscada = reserva 
            break
            
    if reserva_buscada is not None:
        return reserva_buscada
    else:
        return None

#Código Main    
reservas = []
print("BIENVENIDO AL SISTEMA DE RESREVAS DE NUESTRO HOTEL")
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("[1]. Nueva Reserva")
    print("[2]. Buscar Reserva")
    print("[3]. Modificar Reserva")
    print("[4]. Cancelar Reserva")
    print("[5]. Mostrar Todas Las Reservas")
    print("[6]. Salir")
    opcion = input("Elija una opcíon (1/2/3/4/5/6): ")
    match opcion:
        case "1":
            reserva = {}
            reserva["ID"] = registro_id_reserva(reservas)
            reserva["nombre"] = registro_nombre_huesped()
            reserva["numero"] =  registro_n_habitacion(reservas)
            reserva["tipo"] = registro_tipo_habitacion()
            reserva["dias"] = registro_dias() 
            reserva["total"] = calculo_costo(reserva["tipo"],reserva["dias"])

            print("\n--- Resumen reserva ---")
            for key,value in reserva.items():
                if key == "total":
                    print(f"{key}: ${value}")
                else:
                    print(f"{key}: {value}")
            print("Se ha registrado su reserva correctamente✅")
            reservas.append(reserva)


        case "2":
            while True:
                id = input("Ingrese el id unico asociado a su reserva (0 si quiere cancelar): ").strip()
                if id == "0":
                    print("Volviendo al menú principal")
                    break
                else:
                    reserva_buscada = buscar_reserva(id,reservas)
                    if reserva_buscada is not None:
                        print("Se ha encontrado la reserva✅")
                        print("\n--- RESERVA ---")
                        for key,value in reserva_buscada.items():
                            if key == "total":
                                print(f"{key}: ${value}")
                            else:
                                print(f"{key}: {value}")
                        break
                    else:
                        print("No se ha encontrado la reserva, intente nuevamente")


        case "3":
            while True:
                id = input("Ingrese el id unico asociado a su reserva (0 si quiere cancelar): ").strip()
                if id == "0":
                    print("Volviendo al menú principal")
                    break
                else:
                    reserva_buscada = buscar_reserva(id,reservas)
                    if reserva_buscada is not None:
                        print("Se ha encontrado la reserva✅")
                        print("\n--- RESERVA ---")
                        for key,value in reserva_buscada.items():
                            if key == "total":
                                print(f"{key}: ${value}")
                            else:
                                print(f"{key}: {value}")
                        print("DATOS PERMITIDOS A MODIFICAR (TIPO/DIAS)")
                        print("SI NO QUIERE MODIFICAR ALGUN DATO APRETE 0")
                        while True:
                            tipos = ["individual","doble","suite"]
                            nuevo_tipo = input("Ingrese el nuevo tipo de habitacion a reservar (individual/doble/suite): ").lower().strip()
                            if nuevo_tipo == "0":
                                print("No se realizo cambios al tipo")
                                break
                            if nuevo_tipo in tipos:
                                print("Tipo modificado correctamente✅")
                                reserva_buscada["tipo"] = nuevo_tipo
                                break
                            else:
                                print("El tipo ingresado no se encuentra entre las opciones, intente nuevamente con (individual/doble/suite)")
                        
                        while True:
                            try:
                                nuevo_dias_str = input("Ingrese los nuevos dias de estadía: ")
                                if nuevo_dias_str == "0":
                                    print("No se han realizado cambios a los dias de la estadia")
                                    break
                                nuevo_dias = int(nuevo_dias_str)
                                if nuevo_dias > 0:
                                    print("Dias modificados correctamente✅")
                                    reserva_buscada["dias"] = nuevo_dias
                                    break
                                else:
                                    print("La cantidad de dias debe ser mayor a 0, intente nuevamente")
                            except ValueError:
                                print("Error: El valor ingresado debe ser un numero entero")
                        
                        reserva_buscada["total"] = calculo_costo(reserva_buscada['tipo'],reserva_buscada['dias'])
                        print(f"Nuevo Total {reserva_buscada['total']}")
                        break
                    else:    
                        print("No se ha encontrado la reserva, intente nuevamente")                                                  


        case "4":
            while True:
                id = input("Ingrese el id unico asociado a su reserva (0 si quiere cancelar): ").strip()
                if id == "0":
                    print("Volviendo al menú principal")
                    break
                else:
                    reserva_buscada = buscar_reserva(id,reservas)
                    if reserva_buscada is not None:
                        print("Se ha encontrado la reserva✅")
                        print("\n--- RESERVA ---")
                        for key,value in reserva_buscada.items():
                            if key == "total":
                                print(f"{key}: ${value}")
                            else:
                                print(f"{key}: {value}")

                       
                        while True:
                            pregunta = input("Esta segur@ que quiere cancelar la reserva (s/n): ").lower()
                            if pregunta == "s":
                                reservas.remove(reserva_buscada)
                                print("La reserva se ha cancelado correctamente✅")
                                break
                                
                            elif pregunta == "n":
                                print("Cancelando operación...")
                                break

                            else: 
                                print("Opción inválida, intente nuevamente con (s/n): ")
                                continue
                        break

                    else:
                        print("No se ha encontrado la reserva, intente nuevamente")


        case "5":
            if reservas:
                print("--- TODAS LAS RESERVAS ---")
                for reserva in reservas:
                    print("--- RESERVA ---")
                    for key,value in reserva.items():                        
                        if key == "total":
                            print(f"{key}: ${value}")
                        else:
                            print(f"{key}: {value}")
            else:
                print("No se han registrado reservas aún")


        case "6":
            while True:
                confirmacion = input("Esta segur@ que quiere salir del programa (s/n): ").lower()
                if confirmacion == "s":
                    salir = True
                    break
                elif confirmacion == "n":
                    salir = False
                    break
                else: 
                    print("Opción inválida, intente nuevamente con (s/n)")
            if salir:
                print("Saliendo del sistema, Hasta pronto👋👋👋...")
                break
            else:
                print("Volviendo al menú principal...")

                
        case _:
            print("Opcíon Inválida intente con (1/2/3/4/5/6)")