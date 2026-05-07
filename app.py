import sqlite3

def inicializar_db():
    # Crea (o abre) el archivo 'datos_bot.db'
    conexion = sqlite3.connect('datos_bot.db')
    cursor = conexion.cursor()
    # Creamos una tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_nota(texto):
    conexion = sqlite3.connect('datos_bot.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO notas (contenido) VALUES (?)', (texto,))
    conexion.commit()
    conexion.close()
    print(f"✅ Guardado: {texto}")

def ver_notas():
    conexion = sqlite3.connect('datos_bot.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM notas')
    notas = cursor.fetchall()
    conexion.close()
    
    print("\n--- NOTAS GUARDADAS ---")
    for nota in notas:
        print(f"{nota[0]}. {nota[1]}")
    print("-----------------------\n")

# --- Programa Principal ---
inicializar_db()

while True:
    print("¿Qué quieres hacer?")
    print("1. Guardar algo")
    print("2. Ver todo lo guardado")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        dato = input("Escribe lo que quieras guardar: ")
        guardar_nota(dato)
    elif opcion == "2":
        ver_notas()
    elif opcion == "3":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida.")