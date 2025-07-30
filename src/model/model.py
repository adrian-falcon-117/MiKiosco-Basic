import sqlite3 as sql3


class Model:

    def __init__(self):
        self.path = "src/storage/db/mi_db.db"

        # Conexion a Base de Datos
        try:
            self.conexion = sql3.connect(self.path, check_same_thread=False)
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print("No se pudo conectar a la DB error:", e)
