import sqlite3

# Conectar o crear base de datos
conn = sqlite3.connect("soporte.db")
cursor = conn.cursor()

# =========================
# TABLA EMPLEADOS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    legajo INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT,
    sector TEXT
)
""")

# =========================
# TABLA TICKETS
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    legajo INTEGER,
    categoria TEXT,
    urgencia INTEGER,
    estado TEXT,
    descripcion TEXT,
    FOREIGN KEY (legajo) REFERENCES empleados(legajo)
)
""")

# =========================
# TABLA KNOWLEDGE BASE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,
    solucion TEXT
)
""")

# =========================
# DATOS DE PRUEBA
# =========================

# Empleados
empleados = [
    (1042, "Juan Perez", "juan@empresa.com", "Contabilidad"),
    (2050, "Maria Lopez", "maria@empresa.com", "RRHH"),
    (3099, "Carlos Gomez", "carlos@empresa.com", "IT")
]

cursor.executemany("""
INSERT OR IGNORE INTO empleados
VALUES (?, ?, ?, ?)
""", empleados)

# Soluciones automáticas
soluciones = [
    ("Software", "Reinicie la aplicación y vuelva a intentarlo."),
    ("Red", "Verifique la conexión WiFi y reinicie el router."),
    ("Accesos", "Restablezca la contraseña desde el portal."),
    ("Hardware", "Apague y vuelva a encender el equipo.")
]

cursor.executemany("""
INSERT INTO knowledge_base (categoria, solucion)
VALUES (?, ?)
""", soluciones)

conn.commit()
conn.close()

print("Base de datos creada correctamente.")