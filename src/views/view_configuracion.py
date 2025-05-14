from flet import (
    Container,
    Colors,
    Divider,
    VerticalDivider,
    Text,
    TextField,
    ElevatedButton,
    IconButton,
    OutlinedButton,
    Icon,
    Icons,
    Column,
    Row,
    ResponsiveRow,
    ScrollMode,
    MainAxisAlignment,
    RadioGroup,
    Radio,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    TextAlign,
    border,
    BorderSide,
    AlertDialog,
)


class ViewConfiguracion(Container):

    color_black26 = Colors.BLACK26
    color_divider = Colors.GREY
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    ###Controles Contenedor Recargos
    tf_debito_recargo = TextField(label="Debito", suffix_icon=Icons.PERCENT_ROUNDED)
    tf_credito_recargo_uno = TextField(
        label="Credito x1", suffix_icon=Icons.PERCENT_ROUNDED, expand=True
    )
    tf_credito_recargo_dos = TextField(
        label="Credito x2", suffix_icon=Icons.PERCENT_ROUNDED, expand=True
    )
    tf_credito_recargo_tres = TextField(
        label="Credito x3", suffix_icon=Icons.PERCENT_ROUNDED, expand=True
    )
    tf_credito_recargo_seis = TextField(
        label="Credito x6", suffix_icon=Icons.PERCENT_ROUNDED, expand=True
    )
    tf_transferencia_recargo = TextField(
        label="Transferencia", suffix_icon=Icons.PERCENT_ROUNDED
    )
    ebtn_guardar_recargos = ElevatedButton(icon=Icons.SAVE_OUTLINED, text="Guardar")

    ###Controles Contenedor Colores y tema
    r_color_automatico = Radio(value="auto", label="Automatico")
    r_color_rojo = Radio(fill_color=Colors.RED_900, value="red900", label="Rojo")
    r_color_azul = Radio(fill_color=Colors.BLUE_900, value="blue900", label="Azul")
    r_color_amarillo = Radio(
        fill_color=Colors.YELLOW_900, value="yellow900", label="Amarillo"
    )
    r_color_verde = Radio(fill_color=Colors.GREEN_900, value="green900", label="Verde")
    r_color_rosado = Radio(fill_color=Colors.PINK_900, value="pink900", label="Rosado")
    r_color_morado = Radio(
        fill_color=Colors.PURPLE_900, value="purple900", label="Morado"
    )
    r_color_naranja = Radio(
        fill_color=Colors.ORANGE_900, value="orange900", label="Naranja"
    )
    r_tema_claro = Radio(value="light", label="Tema claro")
    r_tema_oscuro = Radio(value="darck", label="Tema oscuro")

    rg_colores = RadioGroup(
        content=Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Column(
                    controls=[
                        r_color_automatico,
                        r_color_rojo,
                    ]
                ),
                Column(
                    controls=[
                        r_color_azul,
                        r_color_amarillo,
                    ]
                ),
                Column(
                    controls=[
                        r_color_verde,
                        r_color_rosado,
                    ]
                ),
                Column(
                    controls=[
                        r_color_morado,
                        r_color_naranja,
                    ]
                ),
            ],
        )
    )
    rg_temas = RadioGroup(content=Row(controls=[r_tema_claro, r_tema_oscuro]))

    ###Controles Contenedor Usuario

    tf_usuario_nombre = TextField(
        prefix_icon=Icons.ALTERNATE_EMAIL, expand=True, label="Nombre usuario"
    )
    tf_contrasena = TextField(
        prefix_icon=Icons.PASSWORD,
        expand=True,
        label="Constraseña",
        # password=True,
        # can_reveal_password=True,
    )
    ebtn_guardar_usuario = ElevatedButton(icon=Icons.SAVE_OUTLINED, text="Guardar")
    ibtn_cancelar_usuario = IconButton(icon=Icons.CLOSE)
    ebtn_editar_usuario = ElevatedButton(icon=Icons.EDIT_OUTLINED, text="Editar")
    obtn_eliminar_usuario = OutlinedButton(icon=Icons.DELETE_ROUNDED, text="Eliminar")
    dt_usuarios = DataTable(
        # width=1050,
        # data_row_min_height=40,
        # data_row_max_height=40,
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1, color_divider),
        border_radius=5,
        vertical_lines=BorderSide(1, color_divider),
        expand=True,
        heading_row_color=color_black26,
        sort_column_index=0,
        sort_ascending=True,
        columns=[
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="ID"),
                visible=False,
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Nombre de usuario"),
            ),
            DataColumn(
                label=Text(value="Contraseña"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
        # rows=my_controller.all_usuarios(),
    )

    # Controles de Dialog Eliminar
    ebtn_si_eliminar_usuario = ElevatedButton(text="Si")
    obtn_no_eliminar_usuario = OutlinedButton(text="No")

    cont_recargos_pagos = Container(
        bgcolor=color_black26,
        padding=5,
        border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[Icon(name=Icons.PERCENT_ROUNDED), Text(value="Recargos")]
                ),
                hor_divider,
                Row(
                    controls=[
                        tf_transferencia_recargo,
                        tf_debito_recargo,
                    ]
                ),
                Row(
                    controls=[
                        tf_credito_recargo_uno,
                        tf_credito_recargo_dos,
                        tf_credito_recargo_tres,
                        tf_credito_recargo_seis,
                    ]
                ),
                Row(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ebtn_guardar_recargos,
                    ],
                ),
            ],
        ),
    )
    cont_config_color = Container(
        expand=True,
        bgcolor=color_black26,
        padding=5,
        border_radius=5,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.COLOR_LENS_OUTLINED),
                        Text(value="Personalizar"),
                    ]
                ),
                hor_divider,
                rg_colores,
                rg_temas,
            ],
        ),
    )
    cont_agregar_usuarios = Container(
        bgcolor=color_black26,
        padding=5,
        border_radius=5,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.PERSON_ADD_OUTLINED),
                        Text(value="Agregar usuarios"),
                    ]
                ),
                hor_divider,
                Row(
                    controls=[
                        tf_usuario_nombre,
                        tf_contrasena,
                        ebtn_guardar_usuario,
                        ibtn_cancelar_usuario,
                    ]
                ),
            ],
        ),
    )
    cont_usuarios = Container(
        bgcolor=color_black26,
        padding=5,
        border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.PERSON_OUTLINE_ROUNDED),
                        Text(value="Usuarios"),
                    ]
                ),
                hor_divider,
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[ResponsiveRow(expand=True, controls=[dt_usuarios])],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[ebtn_editar_usuario, obtn_eliminar_usuario],
                ),
            ],
        ),
    )

    ad_eliminar_usuario = AlertDialog(
        modal=True,
        title=Text(value="Eliminar?"),
        content=Row(
            alignment=MainAxisAlignment.CENTER,
            expand=True,
            controls=[ebtn_si_eliminar_usuario, obtn_no_eliminar_usuario],
        ),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Row(
            expand=True,
            controls=[
                Column(
                    expand=True,
                    controls=[self.cont_agregar_usuarios, self.cont_usuarios],
                ),
                Column(
                    expand=True,
                    controls=[self.cont_recargos_pagos, self.cont_config_color],
                ),
            ],
        )
