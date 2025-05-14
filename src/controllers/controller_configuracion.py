from flet import DropdownOption, Text, DataRow, DataCell

from model.model_configuracion import ModelConfiguracion as my_model
from views import view_login as my_view_login
from views import view_configuracion as my_view_configuracion


class ControllerConfiguracion:

    id_usuario = None

    @classmethod
    def obtener_usuario(self):
        return my_model.get_usuario()

    # Devuelve una lista con todos los usuarios cargados
    @classmethod
    def lista_usuarios(self):
        l_usuarios = []
        for i in self.obtener_usuario():
            l_usuarios.append(
                DropdownOption(key=i[2], text=i[1], content=Text(value=i[1]))
            )
        return l_usuarios

    # Devuelve la contraseña del usuario seleccionado
    @classmethod
    def contrasena_usuario(self):
        v = my_view_login.ViewLogin()
        contrasena = v.dd_usuario.value
        return contrasena

    # Hace las comprobaciones antes de agregar un nuevo usuario
    @classmethod
    def action_guardar_usuario(self):
        v = my_view_configuracion.ViewConfiguracion()
        usuario = v.tf_usuario_nombre.value
        contrasena = v.tf_contrasena.value

        # Si los campos de texto no estan vacio
        if usuario and contrasena:
            self.action_cancelar_usuario()
            return my_model.add_usuario(usuario, contrasena)
        else:
            if not usuario:
                v.tf_usuario_nombre.error_text = "Ingrese un nombre de usuarios"
            if not contrasena:
                v.tf_contrasena.error_text = "Ingrese una contraseña"

    # Valida los campos y actuliza la informacion
    @classmethod
    def action_actualizar_usuario(self):
        v = my_view_configuracion.ViewConfiguracion()
        usuario = v.tf_usuario_nombre.value
        contrasena = v.tf_contrasena.value

        # Si los campos de texto no estan vacio
        if usuario and contrasena:
            self.action_cancelar_usuario()
            return my_model.update_usuario(usuario, contrasena, self.id_usuario)
        else:
            if not usuario:
                v.tf_usuario_nombre.error_text = "Ingrese un nombre de usuarios"
            if not contrasena:
                v.tf_contrasena.error_text = "Ingrese una contraseña"

    @classmethod
    def action_eliminar_usuario(self, id_usuario):
        self.action_cancelar_usuario()
        return my_model.delete_usuario(id_usuario)

    # Obtiene los datos de los TextField
    @classmethod
    def action_editar_usuario(self, nombre, contrasena, id):
        self.id_usuario = id
        v = my_view_configuracion.ViewConfiguracion
        v.tf_usuario_nombre.value = nombre
        v.tf_contrasena.value = contrasena
        # return my_model.update_usuario(nombre, contrasena, id)

    # Limpia los TextField
    @classmethod
    def action_cancelar_usuario(self):
        v = my_view_configuracion.ViewConfiguracion()
        # self.id_usuario = None
        v.tf_usuario_nombre.value = ""
        v.tf_contrasena.value = ""
        v.tf_usuario_nombre.error_text = None
        v.tf_contrasena.error_text = None

    # Guarda el color seleccionado
    @classmethod
    def seleccionar_color(self, color):
        # self.archivo_color.write(color)
        archivo_color = open("src/storage/data/color.dat", "w")
        archivo_color.write(color)
        archivo_color.close()

    # Devuelve el color seleccionado
    @classmethod
    def color_seleccionado(self):
        color_archivo = open("src/storage/data/color.dat", "r")
        return color_archivo.readline()

    # Guarda el tema seleccionado
    @classmethod
    def seleccionar_tema(self, tema):
        # self.archivo_color.write(color)
        archivo_tema = open("src/storage/data/tema.dat", "w")
        archivo_tema.write(tema)
        archivo_tema.close()

    # Devuelve el tema seleccionado
    @classmethod
    def tema_seleccionado(self):
        archivo_tema = open("src/storage/data/tema.dat", "r")
        return archivo_tema.readline()

    # Todos los usuarios

    # print(e.control.selected)
