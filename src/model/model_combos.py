import sqlite3 as sql3


class ModelCombos:
    # Conexion a Base de Datos
    try:
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
            self.cursor.execute(
                "SELECT id, descripcion, precio_venta FROM productos WHERE descripcion LIKE ? COLLATE NOCASE",
                (f"%{descripcion}%",),
            )
            producto = self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener los productos, descripcion: \n {e}")

        return producto
