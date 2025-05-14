from flet import (
    Container,
    Colors,
    Divider,
    VerticalDivider,
    Column,
    Row,
    ScrollMode,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextField,
    ElevatedButton,
    OutlinedButton,
    IconButton,
    Icon,
    Icons,
    Text,
    Checkbox,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    border,
    BorderSide,
    AlertDialog,
)


class ViewCuentaCorriente(Container):

    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    ###Controles de Agregar Cliente
    tf_nombre_cliente = TextField(expand=True, label="Nombre y apellido")
    tf_direccion_cliente = TextField(expand=True, label="Direccion")
    tf_celular_cliente = TextField(expand=True, label="N° Celular")
    tf_credito_limite = TextField(
        expand=True,
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
        label="Credito limite",
        width=150,
    )
    ebtn_guardar_cliente = ElevatedButton(text="Guarda", icon=Icons.SAVE_OUTLINED)
    ibtn_cancelar_cliente = IconButton(icon=Icons.CLOSE_ROUNDED)

    ###Controles de Clientes
    dt_cliente = DataTable(
        width=1500,
        # expand=True,
        # data_row_max_height=40,
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1),
        border_radius=5,
        vertical_lines=BorderSide(1),
        heading_row_color=color_black26,
        sort_column_index=0,
        sort_ascending=True,
        columns=[
            DataColumn(
                numeric=True,
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="ID"),
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Nombre y Apellido"),
            ),
            DataColumn(
                label=Text(value="Direccion"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Celular"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Credito limite"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )
    tx_total_adeudado = Text(value="Total adeudado: ...")
    tx_credito_disponoble = Text(value="Credito diponible: ...")
    ebtn_ver_estado_cuenta = ElevatedButton(
        text="Estado de cuenta",
        icon=Icons.ACCOUNT_BALANCE_OUTLINED,
    )
    ebtn_editar_cliente = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
    obtn_eliminar_cliente = OutlinedButton(text="Eliminar", icon=Icons.DELETE_OUTLINE)

    ###Controles del Dialog Estado de la Cuenta
    tx_nombre_cliente = Text(value="Juan Cabeza")
    dt_productos_cuenta = DataTable(
        width=1500,
        # expand=True,
        # data_row_max_height=40,
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1),
        border_radius=5,
        vertical_lines=BorderSide(1),
        heading_row_color=color_black26,
        sort_column_index=0,
        sort_ascending=True,
        columns=[
            DataColumn(
                numeric=True,
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="ID"),
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Fecha"),
            ),
            DataColumn(
                label=Text(value="Productos"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Subtotal"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
        rows=[
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
            DataRow(
                on_select_changed=lambda e: print(e),
                selected=True,
                cells=[
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
        ],
    )
    ebtn_anular = ElevatedButton(text="Quitar")
    ebtn_pagar = ElevatedButton(text="Pagar")
    obtn_pagar_todo = OutlinedButton(text="Pagar todo")
    ibtn_cerrar_estado_cuenta = IconButton(icon=Icons.CLOSE)
    ##Panel Agregar Cliente
    cont_agregar_cliente = Container(
        bgcolor=color_black26,
        border_radius=5,
        padding=5,
        content=Column(
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.PERSON_ADD_OUTLINED),
                        Text(value="Agregar cliente"),
                    ]
                ),
                hor_divider,
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        tf_nombre_cliente,
                        tf_direccion_cliente,
                        tf_celular_cliente,
                        tf_credito_limite,
                        ebtn_guardar_cliente,
                        ibtn_cancelar_cliente,
                    ],
                ),
            ]
        ),
    )

    ##Panel Clientes
    cont_cliente = Container(
        bgcolor=color_black26,
        border_radius=5,
        padding=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.PEOPLE_OUTLINE_OUTLINED),
                        Text(value="Clientes"),
                    ]
                ),
                hor_divider,
                Column(expand=True, scroll=ScrollMode.AUTO, controls=[dt_cliente]),
                Column(
                    controls=[
                        Row(
                            expand=True,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                ebtn_ver_estado_cuenta,
                                ebtn_editar_cliente,
                                obtn_eliminar_cliente,
                            ],
                        )
                    ]
                ),
            ],
        ),
    )

    ##Dialog Estado de la Cuenta
    ad_estado_cuenta = AlertDialog(
        modal=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            controls=[
                                Icon(name=Icons.ACCOUNT_BALANCE_OUTLINED),
                                Text(value="Estado de cuenta:"),
                                tx_nombre_cliente,
                            ]
                        ),
                        ibtn_cerrar_estado_cuenta,
                    ],
                ),
                hor_divider,
                Column(
                    expand=True, scroll=ScrollMode.AUTO, controls=[dt_productos_cuenta]
                ),
                Row(
                    controls=[
                        Column(controls=[tx_total_adeudado, tx_credito_disponoble]),
                        Row(
                            expand=True,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                ebtn_anular,
                                ebtn_pagar,
                                obtn_pagar_todo,
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Column(
            expand=True, controls=[self.cont_agregar_cliente, self.cont_cliente]
        )
