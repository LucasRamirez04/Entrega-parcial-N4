"""
EJ:

Realice un programa en Python que permita un menú de gestión de ventas para el supermercado tottus que tenga 4 opciones:

op 1: Venta de productos

   Datos del usuario (rut, nombre, dirección)

   Productos a adquirir (20 productos)

   Inventario de los productos (nombre,codigo,descripcion)

   Añadir al carrito

   Continuar comprando o salir de la opción

op 2: Devolución de productos

   Debe aparecer la lista de productos elegidas por el comprador

   Eliminar o cambiar producto

   Observar total en tiempo total (si se elimina el producto, se resta el monto)   

op 3: Mostrar inventario de los productos   

   Mostrar inventario en tiempo real

op 4: Salir
"""
def añadir_producto(producto,lista_productos,carrito,Total):
   if lista_productos[producto]["inventario"] > 0:
      while True:
         try:
            cantidad = int(input("Ingrese la cantidad de producto que desea llevar\n(0 si quiere cancelar): "))
            if cantidad == 0:
               print("Volviendo al menu principal...")
            if cantidad > lista_productos[producto]["inventario"]:
               print("Error: El valor ingresado supera la cantidad de producto que hay en inventario")
            else:
               print(f"{producto} se ha agregado a su carrito✅")
               lista_productos[producto]["inventario"] -= cantidad
               Total += lista_productos[producto]["precio"] * cantidad                            
               carrito[producto] = cantidad                
               break
         except ValueError:
            print("Error: La cantidad ingresada debe ser un numero entero")
   else:
       print("El producto no se encuentra disponible")
   
   return Total

lista_productos = {"carne cerdo" : {"inventario" : 15, "precio" : 8000},
                   "carne vacuno" : {"inventario": 15, "precio" : 7000},
                   "pollo" : {"inventario" : 10, "precio" : 4500},
                   "pan" : {"inventario" : 10, "precio" : 2000},
                   "leche" : {"inventario" : 10, "precio" : 2500},
                   "leche sl" : {"inventario" : 10, "precio" : 3000},
                   "yogurt_frutilla" : {"inventario" : 20, "precio" : 500},
                   "yogurt_vainilla" : {"inventario" : 20, "precio" : 500},
                   "arroz" : {"inventario" : 5, "precio" : 4000},
                   "fiedos" : {"inventario" : 5, "precio" : 4000},
                   "queso" : {"inventario" : 5, "precio" : 5500},
                   "jamon" : {"inventario" : 5, "precio" : 3500},
                   "bebida_cola" : {"inventario" : 5, "precio" : 2000},
                   "bebida_naranja" : {"inventario" : 5, "precio" : 2000},
                   "bebida_ginger" : {"inventario" : 5, "precio" : 2000},
                   "cerveza": {"inventario" : 10, "precio" : 1500},
                   "agua_mineral_cg" : {"inventario" : 5, "precio" : 1000},
                   "agua_mineral_sg" : {"inventario" : 5, "precio" : 1000},
                   "detergente" : {"inventario" : 10, "precio" : 4500},
                   "lava loza" : {"inventario" : 5, "precio" : 3500}
                  }

while True:
   print("\n¡¡¡¡BIENVENIDO A TOTTUS!!!!")
   print("❤ Nos encanta tenerte en nuestro supermercado ❤")
   print("--- MENU PRINCIPAL DE VENTAS TOTTUS ---")
   print("[1]. Venta de productos")
   print("[2]. Devolución de productos")
   print("[3]. Inventario de productos")
   print("[4]. Salir")
   op = input("Elija una opción (1/2/3/4): ")

   if op == "1":
      carrito = {}
      Total = 0
      while True:
         print("\n--- VENTA DE PRODUCTOS ---")
         print("[1]. Añadir producto al carrito ")
         print("[2]. Ver carrito")
         print("[3]. Terminar venta y volver al menú principal")
         opcion = input("Elija una opción (1/2/3): ")
         if opcion == "1":
            print("\n--- Lista de productos ---")
            for i , (key, value) in enumerate(lista_productos.items(),start=1):        
               print(f"{i}. {key}")
               
            producto = input("Escriba el nombre del producto que quiere llevar: ").lower()
            if producto in lista_productos:
               Total = añadir_producto(producto,lista_productos,carrito,Total)
            else:
               print("El producto no se encuentra en el inventario de productos de Tottus")

         elif opcion == "2":
            if carrito:
               print("\nSU CARRITO") 
               for producto, cantidad in carrito.items():
                  precio_unitario = lista_productos[producto]["precio"]
                  subtotal = precio_unitario * cantidad
                  print(f"{producto}: {cantidad} unidades x ${precio_unitario} = ${subtotal}")
               print(f"TOTAL: ${Total}")
            else: 
               print("Aún no ha agregado ningún producto a su carrito")

         elif opcion == "3":
            print("\n--- SALIR ---")
            confirmacion = input("Desea salir al menu principal (s/n): ").lower()
            if confirmacion == "s":
               print("Volviendo al menu principal...")
               break
            else:
               print("Volviendo al menú de venta...")
         
         else:
            print("Opción inválida, intente con (1/2/3)")
      
   elif op == "2":
      if carrito:
         print("\n--- Devolución de productos ---")
         print("SU CARRITO") 
         for producto,cantidad in carrito.items():
            print(f"{producto}: {cantidad}")

         eliminar = input("Escriba el producto a devolver del carrito: ").lower()

         if eliminar in carrito:
            print("Se ha encontrado el producto a eliminar")
            print(f"PRODUCTO: {eliminar} CANTIDAD: {carrito[eliminar]}")
            confirmacion = input("Esta seguro que quiere eliminar ese producto de su carrito (s/n): ").lower()
            if confirmacion == "s":
               Total -= lista_productos[eliminar]['precio'] * carrito[eliminar]
               lista_productos[eliminar]['inventario'] += carrito[eliminar]
               del carrito[eliminar]
               print("El producto se ha eliminado correctamente de su carrito✅")
            else:
               print("Cancelando operación...")
         else:
            print("No se ha encontrado ese producto en su carrito")
      else:
         print("No se ha aagregado ningun producto al carrito aún")
         print("Volviendo al menú anterior...")
   
   elif op == "3":
      print("--- INVENTARIO ACTUAL DE PRODUCTO ---")
      print("PRODUCTO    CANTIDAD")
      for producto,valor in lista_productos.items():
         print(f"{producto} {valor['inventario']}")

   elif op == "4":
      print("\n--- SALIR ---")
      confirmacion = input("¿Desea salir del programa? (s/n): ").lower()
      if confirmacion == "s":
         print("Saliendo del sistema, Hasta pronto👋👋👏")
         break
      else:
         print("Volviendo al menú principal")
      
   else:
      print("Opción inválida, intente con (1/2/3/4)")