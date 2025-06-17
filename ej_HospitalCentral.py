"""
EJ:

El hospital central de Santiago solicita ayuda para mejorar el ingreso a la sala de urgencias, 
para ello requiere un software realizado en Python.

Datos a solicitar del paciente:

   - Numero de rut (validar guíon, max 8 caracteres numéricos, validar numero de identificación)

   - Nombre y apellido del paciente (validar tipo de variable)

   -Lista de patologías:

       - Heridas cortopunzantes

        - Virus

       - Hemorragias

       - Reacciones alérgicas

       - Deshidratación

   -Dirección (lista de comunas de stgo, sino rechazar "Paciente no corresponde a stgo")
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

comunas_santiago = [
    "cerrillos", "cerro navia", "conchalí", "el bosque", "estación central",
    "huechuraba", "independencia", "la cisterna", "la florida", "la granja",
    "la pintana", "la reina", "las condes", "lo barnechea", "lo espejo",
    "lo prado", "macul", "maipú", "ñuñoa", "pedro aguirre cerda",
    "peñalolén", "providencia", "pudahuel", "quilicura", "quinta normal",
    "recoleta", "renca", "san joaquín", "san miguel", "san ramón",
    "santiago", "vitacura", "puente alto", "pirque", "san josé de maipo",
    "colina", "lampa", "tiltil", "buin", "calera de tango", "paine",
    "san bernardo", "alhué", "curacaví", "maría pinto", "melipilla", "san pedro",
    "el monte", "isla de maipo", "padre hurtado", "peñaflor", "talagante"
]

datos_paciente = {}
print("SALA DE ESPERA URGENCIAS DEL HOSPITAL CENTRAL DE SANTIAGO")
while True:
    rut = input("Ingrese el rut del paciente (formato 12345678-9): ")
    if validar_rut(rut):
        datos_paciente['rut'] = rut
        print("Rut Valido✅")
        break

while True:
    nombre = input("Porfavor ingrese el nombre y apellido del paciente: ").strip()
    if any(c.isdigit() for c in nombre):
        print("El nombre no puede contener numeros.")
        continue

    partes = nombre.split()
    if len(partes) != 2:
        print("Debe ingresar el nombre separado por un espacio del apellido")
        continue

    print("Nombre valido✅")
    datos_paciente['nombre'] = nombre
    break

while True:
    print("LISTA DE PATOLOGIAS\n1.Heridas cortopunzantes\n2.Virus\n3.Hemorragias\n4.Reacciones alérgicas\n5.Deshidratación")
    patologia = input("Elija la patologia a tratar (1/2/3/4/5): ")
    if patologia == "1":
        datos_paciente['Patologia'] = "Heridas cortopunzantes"
        
    elif patologia == "2":
        datos_paciente['Patologia'] = "Virus"
    elif patologia == "3":
        datos_paciente['Patologia'] = "Hemorragias"
    elif patologia == "4":
        datos_paciente['Patologia'] = "Reacciones alergicas"
    elif patologia == "5":
        datos_paciente['Patologia'] = "Deshidratación"       
    else:
        print("Opción Inválida, intente con (1/2/3/4/5)")
        continue
    print("Patologia ingresada con exito✅")
    break

while True:
    datos_paciente['dirección'] = []
    comuna = input("Ingrese la comuna del domicilio: ").lower()
    if comuna not in comunas_santiago:
        print("❗❗La comuna ingresada no se encuentra en santiago,\nNo le corresponde atenderse en este hospital❗❗")
        print("PORFAVOR DIRIJIRSE AL HOSPITAL CORRESPONDIENTE A SU CIUDAD PARA PODER SER ATENDIDO")
        print("Cancelando incripción...👋👋👋")
        break
    direccion = input("Ingrese la dirección del domicilio del paciente: ")
    datos_paciente['dirección'].append(direccion)
    datos_paciente['dirección'].append(comuna)
    print("Direccion ingresada con exito✅")
    print("--- RESUMEN DE INSCRIPCIÓN ---")
    for key, valor in datos_paciente.items():
        print(f"{key}: {valor}")
    break
