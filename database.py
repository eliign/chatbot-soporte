import sqlite3

def conectar():
    return sqlite3.connect("soporte.db")

# =========================
# VALIDAR EMPLEADO
# =========================
def validar_empleado(legajo, nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM empleados
    WHERE legajo = ? AND nombre = ?
    """, (legajo, nombre))

    empleado = cursor.fetchone()

    conn.close()

    return empleado

# =========================
# CREAR TICKET
# =========================
def crear_ticket(legajo, categoria, urgencia, descripcion):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tickets
    (legajo, categoria, urgencia, estado, descripcion)
    VALUES (?, ?, ?, ?, ?)
    """, (legajo, categoria, urgencia, "ABIERTO", descripcion))

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id

# =========================
# BUSCAR SOLUCIÓN
# =========================
def buscar_solucion(categoria):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT solucion
    FROM knowledge_base
    WHERE categoria = ?
    """, (categoria,))

    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return resultado[0]

    return None