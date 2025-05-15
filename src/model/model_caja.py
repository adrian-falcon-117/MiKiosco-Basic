import sqlite3 as sql3


class ModelCaja:

    # Conexion a Base de Datos
    try:
        conexion = sql3.connect("src/storage/db/mi_db.db", check_same_thread=False)
        cursor = conexion.cursor()
    except Exception:
        print(Exception)

    # Agregar datos
    @classmethod
    def add_cuenta_corriente(self, nombre, contrasena):
        try:
            self.cursor.execute(
                "INSERT INTO users (nombre, contrasena) VALUES (?,?)",
                (nombre, contrasena),
            )
            self.conexion.commit()
            return True
        except Exception:
            print("Error de conexion")
            return False

    # Obtiene el detalle del producto
    @classmethod
    def get_productos(self):
        try:
            self.cursor.execute("SELECT * FROM productos")
            usuarios = self.cursor.fetchall()
        except Exception:
            print("Error al obtener el producto")

        return usuarios

    # Eliminar usario
    @classmethod
    def delete_usuario(self, id):
        try:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
            self.conexion.commit()
            return True
        except Exception:
            print("Error al eliminar")
            return False

    # Obtener todos los datos

    # Actualizar dato
    @classmethod
    def update_usuario(self, nombre, contrasena, id):
        try:
            self.cursor.execute(
                "UPDATE users SET nombre = ?, contrasena = ? WHERE id = ?",
                (nombre, contrasena, id),
            )
            self.conexion.commit()
            return True
        except Exception:
            print("No se pudo actualizar")
            return False

    @classmethod
    def get_all_usuario(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            usuarios = self.cursor.fetchall()
        finally:
            pass

        return usuarios
