from model.model import Model
from views.mensaje import Mensaje


class ModelProductos(Model):

    def __init__(self, page):
        self.page = page
        self.mensaje = Mensaje(self.page)

    # Obtine el id de un producto
    def get_id_producto(self, descripcion):
        try:
            self.cursor.execute(
                "SELECT id FROM productos WHERE descripcion = ?", (descripcion)
            )
            return self.cursor.fetchone()[0]

        except Exception as ex:
            self.mensaje.mensaje_error(f"Error de coneccion:{ex}")

    # Agregar datos
    def create(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO productos (descripcion, cantidad, precio_compra, recargo, precio_venta) VALUES (?,?,?,?,?)",
                (datos[1], datos[2], datos[3], datos[4], datos[5]),
            )
            self.conexion.commit()
            self.mensaje.mensaje_ok("Guadado correctamente")
        except Exception as ex:
            self.mensaje.mensaje_error(f"No se pudo guardar, error: {ex}")

    # Obtener todos los productos
    def read(self, txt):
        try:
            self.cursor.execute(f"SELECT * FROM productos {txt}")
            productos = self.cursor.fetchall()
            # print(productos)
            return productos
        except Exception as ex:
            self.mensaje.mensaje_error(f"No se pudo obtener, error: {ex}")

    def read_asc(self):
        try:
            self.cursor.execute("SELECT * FROM productos ORDER BY descripcion ASC")
            productos = self.cursor.fetchall()
            # print(productos)
            return productos
        except Exception as ex:
            print("Error aca", ex)
            # self.mensaje.mensaje_error(f"No se pudo obtener, error: {ex}")

    def read_desc(self):
        try:
            self.cursor.execute("SELECT * FROM productos ORDER BY descripcion DESC")
            productos = self.cursor.fetchall()
            # print(productos)
            return productos
        except Exception as ex:
            print("Error aca", ex)
            # self.mensaje.mensaje_error(f"No se pudo obtener, error: {ex}")

    # Eliminar un producto
    def delete(self, id):
        try:
            self.cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            self.conexion.commit()
            self.mensaje.mensaje_ok("Eliminado correctamente")
        except Exception as ex:
            self.mensaje.mensaje_error(f"No se pudo eliminar error: {ex}")

    # Obtener todos los datos

    # Actualizar datos
    def update(self, datos):
        try:
            self.cursor.execute(
                "UPDATE productos SET descripcion = ?, cantidad = ?, precio_compra = ?, recargo = ?, precio_venta = ? WHERE id = ?",
                (datos[1], datos[2], datos[3], datos[4], datos[5], datos[0]),
            )
            self.conexion.commit()
            self.mensaje.mensaje_ok("Actualizado correctamente")
        except Exception as ex:
            self.mensaje.mensaje_error(f"No se pudo actulizar, error: {ex}")
