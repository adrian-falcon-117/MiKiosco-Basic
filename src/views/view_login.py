from flet import (
    AlertDialog,
    Icon,
    Icons,
    TextField,
    Dropdown,
    Text,
    ElevatedButton,
    OutlinedButton,
    Column,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
    CircleAvatar,
    Container,
    Divider,
)

from controllers.controller_configuracion import (
    ControllerConfiguracion as my_controller,
)


class ViewLogin(Container):

    ca_avatar = CircleAvatar(
        Icon(name=Icons.PERSON_OUTLINE_ROUNDED, size=90), width=100, height=100
    )
    dd_usuario = Dropdown(
        width=300,
        leading_icon=Icons.PERSON_OUTLINE_ROUNDED,
        label="Usuario",
        options=my_controller.lista_usuarios(),
    )
    tf_contrasena = TextField(
        prefix_icon=Icons.PASSWORD,
        expand=True,
        label="Contraseña",
        # error_text="Contraseña incorrecta",
        password=True,
        can_reveal_password=True,
    )
    ebtn_iniciar = ElevatedButton(text="Iniciar sesión")
    obtn_salir = OutlinedButton(text="Salir")
    ad_login = AlertDialog(
        modal=True,
        content=Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            height=350,
            controls=[
                ca_avatar,
                Text(value="Iniciar sesión", size=20),
                Divider(),
                dd_usuario,
                tf_contrasena,
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[ebtn_iniciar, obtn_salir],
                ),
            ],
        ),
    )

    def __init__(self):
        super().__init__()
        self.content = self.ad_login
