import sqlite3 as sql3


class ModelProductos:

    # Conexion a Base de Datos
    try:
        conexion = sql3.connect("src/storage/db/mi_db.db", check_same_thread=False)
        cursor = conexion.cursor()
    except Exception:
        print(Exception)

    # Agregar datos
    @classmethod
    def add_producto(self, descripcion, cantidad, precio_compra, recargo, precio_venta):
        try:
            self.cursor.execute(
                "INSERT INTO productos (descripcion, cantidad, precio_compra, recargo, precio_venta) VALUES (?,?,?,?,?)",
                (descripcion, cantidad, precio_compra, recargo, precio_venta),
            )
            self.conexion.commit()
            return True
        except Exception:
            print("Error de conexion")
            return False

    # Obtener todos los productos
    @classmethod
    def get_producto(self):
        try:
            self.cursor.execute("SELECT * FROM productos")
            usuarios = self.cursor.fetchall()
        except Exception:
            print("Error al obtener los productos")

        return usuarios

    # Eliminar usario
    @classmethod
    def delete_producto(self, id):
        try:
            self.cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            self.conexion.commit()
            return True
        except Exception:
            print("Error al eliminar")
            return False

    # Obtener todos los datos

    # Actualizar dato
    @classmethod
    def update_producto(
        self, descripcion, cantidad, precio_compra, recargo, precio_venta, id
    ):
        try:
            self.cursor.execute(
                "UPDATE productos SET descripcion = ?, cantidad = ?, precio_compra = ?, recargo = ?, precio_venta = ? WHERE id = ?",
                (descripcion, cantidad, precio_compra, recargo, precio_venta, id),
            )
            self.conexion.commit()
            return True
        except Exception:
            print("No se pudo actualizar")
            return False
