from database import validar_empleado
from database import crear_ticket
from database import buscar_solucion

print("===================================")
print(" BOT DE SOPORTE TÉCNICO")
print("===================================")

# =========================
# NOMBRE
# =========================
nombre = input("Ingrese su nombre completo: ")

# =========================
# LEGAJO
# =========================
intentos = 0
empleado_valido = False

while intentos < 3:

    legajo = input("Ingrese su legajo: ")

    # CAMINO INFELIZ
    if not legajo.isdigit():
        print("ERROR: El legajo debe ser numérico.")
        continue

    empleado = validar_empleado(int(legajo), nombre)

    if empleado:
        empleado_valido = True
        break

    else:
        intentos += 1
        print(f"Legajo inválido. Intento {intentos}/3")

if not empleado_valido:
    print("Demasiados intentos fallidos.")
    exit()

print("Empleado validado correctamente.")

# =========================
# CATEGORÍA
# =========================
print("\nSeleccione categoría:")
print("1 - Hardware")
print("2 - Software")
print("3 - Red")
print("4 - Accesos")

categorias = {
    "1": "Hardware",
    "2": "Software",
    "3": "Red",
    "4": "Accesos"
}

categoria_opcion = input("Opción: ")

if categoria_opcion not in categorias:
    print("Categoría inválida.")
    exit()

categoria = categorias[categoria_opcion]

# =========================
# URGENCIA
# =========================
print("\nNivel de urgencia:")
print("1 - Baja")
print("2 - Media")
print("3 - Crítica")

urgencia = input("Urgencia: ")

if urgencia not in ["1", "2", "3"]:
    print("Urgencia inválida.")
    exit()

urgencia = int(urgencia)

# =========================
# DESCRIPCIÓN
# =========================
descripcion = input("\nDescriba el problema: ")

# =========================
# CREAR TICKET
# =========================
ticket_id = crear_ticket(
    int(legajo),
    categoria,
    urgencia,
    descripcion
)

print(f"\nTicket generado correctamente. ID: {ticket_id}")

# =========================
# GATEWAY URGENCIA
# =========================
if urgencia == 3:
    print("URGENTE: Caso derivado a técnico senior.")
    exit()

# =========================
# BUSCAR SOLUCIÓN
# =========================
solucion = buscar_solucion(categoria)

if solucion:

    print("\nPosible solución encontrada:")
    print(solucion)

    respuesta = input("\n¿El problema fue resuelto? (SI/NO): ")

    if respuesta.upper() == "SI":

        print("Gracias por utilizar el sistema.")
        calificacion = input("Califique la atención (1-5): ")

        print("Ticket cerrado.")

    else:
        print("Caso derivado a técnico.")

else:
    print("No se encontró solución automática.")
    print("Caso derivado a técnico.")

print("\nFin del proceso.")