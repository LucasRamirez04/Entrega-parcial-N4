"""
EJ2:

La empresa Netflix solicita a nuestra empresa de desarrollo mejorar su menú de opciones de entretenimiento

opción 1 ("Añadir película")

- Nombre   

- Categorías:

    -Acción

    -Ciencia ficción

    -Terror

    -Comedia

    -Salir del menú

- Duración de la película

- Volver al menú principal

opción 2 ("Salir")

"""
peliculas = []
while True:
    print("--- BIENVENIDO AL NUEVO MENU DE NETFLIX ---")
    print("[1]. Añadir pelicula")
    print("[2]. Mostrar lista de peliculas")
    print("[3]. Salir")
    op = input("Elija una opción: ")
    match op:
        
        case "1":
            nombre = None
            categoria = None
            duracion = None
            while True:
                print("--- MENU ---")
                print("[1]. Nombre pelicula")
                print("[2]. Categoria pelicula")
                print("[3]. Duración pelicula ")
                print("[4]. Volver al menu principal")
                op_item = input("Elija una opción: ")

                match op_item:

                    case "1":
                        nombre = input("Ingrese el nombre de la pelicula: ")
            
                    case "2":
                        while True:
                            print("--- CATEGORIAS ---")
                            print("[1].Acción")
                            print("[2].Ciencia Ficción")
                            print("[3].Terror")
                            print("[4].Comedia")
                            print("[5].Salir al menú")
                            op_categoria = input("Elija una opción: ")
                            if op_categoria == "1":
                                categoria = "Accion"
                                break
                            elif op_categoria == "2":
                                categoria = "Ciencia Ficción"
                                break                    
                            elif op_categoria == "3":
                                categoria = "Terror" 
                                break                       
                            elif op_categoria == "4":
                                categoria = "Comedia"
                                break
                            elif op_categoria == "5":
                                print("Volviendo al menú principal...")
                                break
                            else:
                                print("Error: Opción Inválida")                        
                        
                    case "3":
                        while True:
                            try:
                                duracion = int(input("Ingrese la duración de la pelicula: "))
                                
                                break
                            except:
                                print("Error: Ingresa un valor válido")
                    case "4":
                        print("\nVolviendo al menú principal...\n")
                        break
                    case _:
                        print("Opción Inválida")
                
                if nombre and categoria and duracion is not None:
                    print("Todos los items completados")
                    movie = {
                        "Nombre" : nombre,
                        "Categoria" : categoria,
                        "Duración" : duracion
                    }
                    peliculas.append(movie)
                    print("Pelicula guardada correctamente✅")
                    break

        case "2":
            if peliculas:
                print("LISTA DE PELICULAS")
                for i,pelicula in enumerate(peliculas,start=1):
                    print(f"Pelicula {i}")
                    for key,valor in pelicula.items():
                        print(f"{key} = {valor}")

            else:
                print("No se han registrado peliculas aún")
                continue

        case "3":
            print("Saliendo del sistema...¡Hasta pronto👋👋👋!")
            break
                    
        case _ :
             print("Opción Inválida")