import sqlite3 as sql3
import threading

# import time


class ModelCombos:
    # Conexion a Base de Datos
    try:
        lock = threading.Lock()
        conexion = sql3.connect("src/storage/db/mi_db.db", check_same_thread=False)
        cursor = conexion.cursor()
    except Exception:
        print(Exception)  # Conexion a Base de Datos

    @classmethod
    def get_descripcion_producto(self):
        try:
            self.cursor.execute("SELECT descripcion FROM productos")
            productos = self.cursor.fetchall()

        except Exception:
            print("Error al obtener los productos")

        return productos

    @classmethod
    def get_producto(self, descripcion):
        producto = []
        try:
            self.cursor.execute(
                "SELECT id, descripcion, precio_venta FROM productos WHERE descripcion = ?",
                (descripcion,),
            )
            producto = self.cursor.fetchall()
        except Exception:
            print("Error al obtener los productos")

        return producto

    @classmethod
    def get_producto2(self, descripcion):

        producto = []
        try:
            # time.sleep(3)
            self.lock.acquire(True)
            self.cursor.execute(
                "SELECT id, descripcion, precio_venta FROM productos WHERE descripcion LIKE ? COLLATE NOCASE",
                (f"%{descripcion}%",),
            )
            producto = self.cursor.fetchall()
        except Exception as exp:
            print(f"Error al obtener el id, descripcion, precio_venta: \n {exp}")
        finally:
            self.lock.release()

        return producto
