from model.model import Model
from views.mensaje import Mensaje


class ModelCombos(Model):

    def __init__(self, page):
        self.page = page
        self.mensaje = Mensaje(self.page)

    # Obtiene el id de un combo
    def get_id_combo(self, nombre):
        try:
            self.cursor.execute("SELECT id FROM combo WHERE nombre = ?", (nombre))
            return self.cursor.fetchone()[0]

        except Exception as ex:
            self.mensaje(f"Error de coneccion:{ex}")

    def buscar(self, descripcion):
        try:
            self.cursor.execute(
                f"SELECT id, descripcion, precio_venta FROM productos WHERE descripcion LIKE ?",
                (f"%{descripcion}%",),
            )
            productos = self.cursor.fetchall()
            return productos

        except Exception as ex:
            self.mensaje.mensaje_error(f"Error de coneccion:{ex}")
            print(ex)

    # Agregar un nuevo combo
    def create(self, nombre, descuento):
        try:
            self.cursor.execute(
                "INSERT INTO combo (nombre, descuento) VALUES (?,?)",
                (nombre, descuento),
            )
            self.conexion.commit()
            self.mensaje.mensaje_ok("Guardado")
        except Exception as ex:
            self.mensaje.mensaje_error(f"Error de coneccion: {ex}")
            return False
