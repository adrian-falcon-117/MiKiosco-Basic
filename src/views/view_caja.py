from flet import (
    Text,
    TextField,
    OutlinedButton,
    ElevatedButton,
    DataTable,
    DataColumn,
    DataCell,
    DataRow,
    Colors,
    Icon,
    Icons,
    Divider,
    VerticalDivider,
    Container,
    AutoComplete,
    Dropdown,
    border,
    BorderSide,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextAlign,
    IconButton,
    Checkbox,
    MenuItemButton,
    SubmenuButton,
    MenuBar,
    FilledButton,
    AlertDialog,
    Column,
    Row,
    ScrollMode,
    ResponsiveRow,
)

from controllers.controller_caja import (
    ControllerCaja as my_controller,
)


class ViewCaja(Container):

    # Colores
    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    # Datos usuario
    ######Controles de Barra superior
    """
    user_uri_img = "https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
    user_name = "Juan Cabeza"

    # Numero de caja
    num_caja = ft.Text(value="Caja 01", weight=ft.FontWeight.BOLD)

    # Fecha y hora
    hora = ft.Text(value="20:02")
    fecha = ft.Text(value="20/02/2020")
    name = ft.Text(value=user_name)
    """

    # Items de movimieto de caja
    """"
    item_aperura_caja = ft.MenuItemButton(
        leading=ft.Icon(ft.Icons.MOVE_TO_INBOX),
        content=ft.Text("Apertura de caja"),
    )
    item_ingreso_caja = ft.MenuItemButton(
        leading=ft.Icon(ft.Icons.ADD_BOX),
        content=ft.Text("Ingreso de caja"),
    )
    item_egreso_caja = ft.MenuItemButton(
        leading=ft.Icon(ft.Icons.INDETERMINATE_CHECK_BOX),
        content=ft.Text("Egreso de caja"),
    )
    item_cierre_caja = ft.MenuItemButton(
        leading=ft.Icon(ft.Icons.OUTBOX),
        content=ft.Text("Cierre de caja"),
    )

    # Permitira relizar los distintos moviento de caja
    mb_movimieto_caja = ft.MenuBar(
        controls=[
            ft.SubmenuButton(
                leading=ft.Icon(name=ft.Icons.ALL_INBOX),
                content=ft.Text(value="Movimientos de caja"),
                controls=[
                    item_aperura_caja,
                    item_ingreso_caja,
                    item_egreso_caja,
                    item_cierre_caja,
                ],
            )
        ]
    )

    # Foto o avatar del usuario
    avatar = ft.Stack(
        controls=[
            ft.CircleAvatar(foreground_image_src=user_uri_img),
            ft.Container(
                content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),
                alignment=ft.alignment.bottom_left,
            ),
        ],
        width=40,
        height=40,
        alignment=ft.alignment.center_left,
    )
    """

    ######Controles de Contenedor Carriro
    ac_buscar_producto = AutoComplete(
        suggestions=my_controller.resultado_burqueda_producto()
    )
    tf_codigo_barra = TextField(
        prefix_icon=Icons.SEARCH_ROUNDED, label="Descripcion/Codigo de barra"
    )
    dd_lista_precio = Dropdown(
        leading_icon=Icons.FORMAT_LIST_BULLETED,
        options=my_controller.lista_precio_lista(),
    )
    ebtn_quitar_lista = ElevatedButton(
        text="Quitar seleccion",
        icon=Icons.HIGHLIGHT_REMOVE,
        # on_click=my_controller.action_ebtn_quitar_lista,
    )
    # Tabla de las compras
    dt_carrito = DataTable(
        # data_row_min_height=40,
        # data_row_max_height=40,
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1),
        border_radius=5,
        vertical_lines=BorderSide(1),
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
                label=Text(value="Descripcion"),
            ),
            DataColumn(
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Descuento(-)\nRecargo(+)"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Precio Un."),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Subtotal"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )

    ####### Controles Contenedor Cuenta corriente
    tf_nombre_apellido = TextField(label="Nombre y apellido")
    # ibtn_buscar_cliente = IconButton(icon=Icons.SEARCH_ROUNDED)
    ebtn_agregar_cuenta_corriente = ElevatedButton(text="Agregar")
    # cbox_usuario = Checkbox(label="Soy usuario")
    tx_direccion = Text(value="Direccion")
    tx_telefono = Text(value="Telefono:")
    tx_credito_disponible = Text(value="Credito disponible: ...")
    tx_total_adeudado = Text(value="Total adeudado: ...")

    ###### Controles de Contenedor Ticket
    """
    txt_fecha_ticket = ft.Text(
        col={"sm": 6, "md": 4, "xl": 2}, value="Fecha: 20/02/2020"
    )
    dd_tipo_ticket = ft.Dropdown(
        col={"sm": 6, "md": 4, "xl": 2},
        value="Tipo de ticket/factura",
        leading_icon=ft.Icons.FORMAT_LIST_BULLETED,
        options=my_controller.lista_precio_lista(),
    )
    tf_num_factura = ft.TextField(col={"sm": 6, "md": 4, "xl": 2}, label="N° Ticket")
    tf_observaciones = ft.TextField(
        col={"sm": 6, "md": 4, "xl": 2},
        label="Observaciones",
        multiline=True,
        max_lines=2,
    )
    ebtn_generar_ticket = ft.ElevatedButton(
        col={"sm": 6, "md": 4, "xl": 2},
        text="Generar ticket",
        icon=ft.Icons.LOCAL_PRINTSHOP_OUTLINED,
    )
    """

    ###### Controles de Contenedor Medios de Pago
    tf_efectivo = TextField(suffix_icon=Icons.MONEY, label="Efectivo")
    tf_tarjeta_debito = TextField(
        suffix_icon=Icons.CREDIT_CARD_OUTLINED, label="Tarjeta de debito"
    )
    tf_targeta_credito = TextField(
        # suffix_icon=ft.Icons.CREDIT_SCORE_OUTLINED,
        label="Tarjeta de credito",
        width=180,
    )
    tf_transferencia = TextField(
        suffix_icon=Icons.SEND_TO_MOBILE_OUTLINED, label="Transferencias"
    )
    dd_cuotas = Dropdown(
        options=my_controller.lista_cantidad_cuotas(),
        text_align=TextAlign.RIGHT,
        tooltip="Seleccione el número de cuotas",
        leading_icon=Icons.CREDIT_SCORE_OUTLINED,
        width=100,
    )
    item_agregar_todo = MenuItemButton(
        leading=Icon(Icons.BALLOT_OUTLINED),
        content=Text("Agragar todo"),
    )
    item_agregar_seleccionados = MenuItemButton(
        leading=Icon(Icons.CHECKLIST),
        content=Text("Solo seleccionados"),
    )
    mb_agregar_producto_cuenta = MenuBar(
        controls=[
            SubmenuButton(
                leading=Icon(name=Icons.ACCOUNT_BALANCE_OUTLINED),
                content=Text(value="Agregar a cuenta corriente"),
                controls=[item_agregar_todo, item_agregar_seleccionados],
            )
        ]
    )
    tx_total = Text(value="Total: $99999", size=15)
    tx_vuelto = Text(value="Vuelto: $999999", size=15)
    # cbox_agregar_producto_cuenta = Checkbox(label="Agregar a cuenta corriente")
    fbtn_finalizar_venta = FilledButton(
        height=50,
        text="Finalizar venta",
        # bgcolor=ft.Colors.GREEN_900,
        # color=ft.Colors.BLACK,
        icon=Icons.SHOPPING_CART_CHECKOUT_OUTLINED,
    )

    ###### Controles de Dialogo Cuenta Corriente
    ibtn_cerrar_cuenta_corriente = IconButton(icon=Icons.CLOSE)

    ## Contenedores

    # Contenedor de la barra superior
    """
    cont_barra = ft.Container(
        border_radius=5,
        height=60,
        bgcolor=color_black26,
        padding=5,
        # expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        avatar,
                        name,
                        ver_divider,
                    ]
                ),
                num_caja,
                ft.Row(
                    controls=[
                        mb_movimieto_caja,
                        ver_divider,
                        fecha,
                        hora,
                    ]
                ),
            ],
        ),
    )
    """
    # Contenedor del Carrito
    cont_carrito = Container(
        bgcolor=color_black26,
        border_radius=5,
        padding=5,
        expand=True,
        # width=700,
        # height=500,
        content=Column(
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.LOCAL_GROCERY_STORE_OUTLINED),
                        Text(value="Carrito"),
                    ]
                ),
                hor_divider,
                Row(
                    controls=[
                        Icon(name=Icons.SEARCH),
                        Container(
                            padding=2,
                            border_radius=5,
                            bgcolor=Colors.BLACK12,
                            width=270,
                            height=50,
                            content=ac_buscar_producto,
                        ),
                        dd_lista_precio,
                        ebtn_quitar_lista,
                    ]
                ),
                Column(
                    scroll=ScrollMode.AUTO,
                    expand=True,
                    controls=[ResponsiveRow(expand=True, controls=[dt_carrito])],
                ),
            ],
        ),
    )
    # Contenedor de la cuenta corriente
    cont_cuenta_corriente = Container(
        # bgcolor=color_black26,
        border_radius=5,
        # expand=True,
        padding=5,
        width=500,
        height=300,
        content=Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            controls=[
                                Icon(name=Icons.ACCOUNT_BALANCE_OUTLINED),
                                Text(value="Cuenta corriente"),
                            ]
                        ),
                        ibtn_cerrar_cuenta_corriente,
                    ],
                ),
                hor_divider,
                Row(
                    controls=[
                        tf_nombre_apellido,
                    ]
                ),
                tx_direccion,
                tx_telefono,
                tx_credito_disponible,
                tx_total_adeudado,
                Row(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ebtn_agregar_cuenta_corriente,
                    ],
                ),
            ]
        ),
    )

    # Contenedor de los tickets
    """
    cont_ticket = ft.Container(
        bgcolor=color_black26,
        border_radius=5,
        expand=True,
        padding=5,
        # height=300,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.INSERT_DRIVE_FILE_OUTLINED),
                        ft.Text(value="Tickets"),
                    ]
                ),
                hor_divider,
                ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        txt_fecha_ticket,
                        dd_tipo_ticket,
                        tf_num_factura,
                        tf_observaciones,
                        ebtn_generar_ticket,
                    ],
                ),
            ]
        ),
    )
    """
    # Contenedor de Medios de Pago
    cont_medios_pago = Container(
        bgcolor=color_black26,
        border_radius=5,
        padding=5,
        width=300,
        height=500,
        content=Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.PAYMENTS_OUTLINED),
                        Text(value="Medios de pago"),
                    ]
                ),
                hor_divider,
                tf_efectivo,
                tf_tarjeta_debito,
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[tf_targeta_credito, dd_cuotas],
                ),
                tf_transferencia,
                mb_agregar_producto_cuenta,
                # cbox_agregar_producto_cuenta,
                hor_divider,
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[tx_total, hor_divider, tx_vuelto],
                ),
                fbtn_finalizar_venta,
            ],
        ),
    )

    ad_cuenta_corriente = AlertDialog(
        modal=True,
        # icon=ft.Icons.CLOSE,
        # title=ft.Text("Cerrar sesion"),
        content=cont_cuenta_corriente,
        adaptive=True,
    )

    # Constructor
    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Row(
            expand=True,
            vertical_alignment=CrossAxisAlignment.START,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.cont_carrito,
                self.cont_medios_pago,
            ],
        )
