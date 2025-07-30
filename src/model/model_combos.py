import sqlite3 as sql3
import threading
from flet import Container

from model.model import Model

# import time


class ModelCombos(Model):

    def _init__(self):
        pass

    # # Conexion a Base de Datos
    # try:
    #     lock = threading.Lock()
    #     conexion = sql3.connect("src/storage/db/mi_db.db", check_same_thread=False)
    #     cursor = conexion.cursor()
    # except Exception:
    #     print(Exception)  # Conexion a Base de Datos

    def get_descripcion_producto(self):
        try:
            self.cursor.execute("SELECT descripcion FROM productos")
            productos = self.cursor.fetchall()

        except Exception:
            print("Error al obtener los productos")

        return productos

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

    def get_producto2(self, descripcion):

        producto = []
        try:
            # time.sleep(3)
            #self.lock.acquire(True)
            self.cursor.execute(
                "SELECT id, descripcion, precio_venta FROM productos WHERE descripcion LIKE ? COLLATE NOCASE",
                (f"%{descripcion}%",),
            )
            producto = self.cursor.fetchall()
        except Exception as exp:
            print(f"Error al obtener el id, descripcion, precio_venta: \n {exp}")
        # finally:
        #     self.lock.release()

        return producto

    def create(
        self,
        nombre,
        precio,
        id_producto,
        descripcion_producto,
        cantidad_producto,
        subtotal_producto,
    ):
        try:
            self.cursor.execute(
                "INSERT INTO combo (nombre, precio, id_producto, descripcion_producto, cantidad_producto, subtotal_producto) VALUES (?,?,?,?,?,?)",
                (
                    nombre,
                    precio,
                    id_producto,
                    descripcion_producto,
                    cantidad_producto,
                    subtotal_producto,
                ),
            )
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error de conexion:", e)
            return False
