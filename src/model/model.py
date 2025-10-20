import sqlite3 as sql3


class Model:

    # Conexion a Base de Datos
    try:
        conexion = sql3.connect("src/storage/db/mi_db.db", check_same_thread=False)
        cursor = conexion.cursor()
    except Exception as ex:
        print("No se pudo conectar a la DB error:", ex)
