from flet import (
    Container,
    Column,
    Row,
    TextField,
    Text,
    ElevatedButton,
    IconButton,
    OutlinedButton,
    Divider,
    DataTable,
    DataColumn,
    border,
    BorderSide,
    MainAxisAlignment,
    Icons,
    Icon,
    Colors,
    VerticalDivider,
    ScrollMode,
    ResponsiveRow,
    ExpansionPanel,
    ExpansionPanelList,
    padding,
    AlertDialog,
    AutoComplete,
    SearchBar,
    ListView,
    RoundedRectangleBorder,
)

from controllers.controller_combos import ControllerCombo


class ViewCombos(Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.controller = ControllerCombo(page, self)

        self.lv_productos = ListView()
        self.sb_buscar_producto = SearchBar(
            expand=True,
            bar_hint_text="Buscar un producto",
            view_hint_text="Selecciona un color de las sugerencias",
            view_shape=RoundedRectangleBorder(radius=5),
            bar_shape=RoundedRectangleBorder(radius=5),
            controls=[self.lv_productos],
            on_change=self.controller.action_buscar_producto,
        )
        self.expand = True

        self.color_black26 = Colors.BLACK26
        self.hor_divider = Divider()
        self.ver_divider = VerticalDivider()

        ###Controles de Crear Combos
        self.tf_nombre_combo = TextField(label="Nombre del combo")
        self.tf_descuento_combo = TextField(
            label="Descuento general",
            suffix_icon=Icons.PERCENT_ROUNDED,
            expand=True,
        )
        self.tf_precio_combo = TextField(
            prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
            label="Precio del combo",
        )
        self.ebtn_agregar_producto = ElevatedButton(
            text="Agregar producto", icon=Icons.ADD_CIRCLE_OUTLINE
        )
        self.ebtn_guardar_combo = ElevatedButton(
            text="Guardar", icon=Icons.SAVE_OUTLINED
        )
        self.ibtn_cancelar_combo = IconButton(
            tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED
        )
        self.ibtn_cerrar_agregar_producto = IconButton(icon=Icons.CLOSE)

        self.ebtn_ver_combos = ElevatedButton(
            text="Ver combos", icon=Icons.DISCOUNT_OUTLINED
        )
        self.ebtn_editar_combo2 = ElevatedButton(
            text="Editar", icon=Icons.EDIT_OUTLINED
        )
        self.obtn_quitar_combo = OutlinedButton(
            text="Quitar", icon=Icons.CANCEL_OUTLINED
        )

        ###Controles de Combos
        self.ebtn_crear_combo = ElevatedButton(
            text="Crear combo",
            icon=Icons.ADD_CIRCLE_OUTLINE_OUTLINED,
            on_click=self.controller.on_crear_combo,
        )
        self.ebtn_editar_combo = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
        self.obtn_eliminar_combo = OutlinedButton(
            text="Eliminar", icon=Icons.DELETE_OUTLINE
        )
        self.txt_total_combo = Text(value="Total: $...")

        ###Controles de Dialog seleccionar producto

        self.tf_cantidad_producto = TextField(
            label="Cantidad", width=100, disabled=True
        )
        self.txt_subtotal = Text(value="Subtotal: $0")
        self.ebtn_agregar = ElevatedButton(text="Agregar producto", disabled=True)
        self.ibtn_cerrar_seleccionar_productos = IconButton(
            tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED
        )
        self.txt_mensaje_alerta = Text(color=Colors.RED)

        self.dt_combos = DataTable(
            show_checkbox_column=True,
            checkbox_horizontal_margin=0,
            border=border.all(1),
            border_radius=5,
            vertical_lines=BorderSide(1),
            heading_row_color=self.color_black26,
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
                    label=Text(value="Producto"),
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Cantidad"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Subtotal"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
            ],
        )

        self.dt_promociones_activas = DataTable(
            # expand=True,
            # data_row_max_height=40,
            show_checkbox_column=True,
            checkbox_horizontal_margin=0,
            border=border.all(1),
            border_radius=5,
            vertical_lines=BorderSide(1),
            heading_row_color=self.color_black26,
            sort_column_index=0,
            sort_ascending=True,
            columns=[
                DataColumn(
                    heading_row_alignment=MainAxisAlignment.START,
                    label=Text(value="Productos"),
                ),
                DataColumn(
                    heading_row_alignment=MainAxisAlignment.START,
                    label=Text(value="Cantidad"),
                ),
                DataColumn(
                    heading_row_alignment=MainAxisAlignment.START,
                    label=Text(value="Total"),
                ),
            ],
        )

        self.ep_venta = ExpansionPanel(
            header=Container(
                padding=padding.only(left=5),
                content=Row(
                    expand=True,
                    controls=[Text(value="hola")],
                ),
            ),
            expand=True,
        )
        self.ep_venta_1 = ExpansionPanel(expand=True, content=Text(value="Hola"))
        self.ep_venta_2 = ExpansionPanel(expand=True, content=Text(value="Hola"))

        self.eplist_combo = ExpansionPanelList(
            expand=True,
            # divider_color=color_divider,
            controls=[
                self.ep_venta,
                self.ep_venta_1,
                self.ep_venta_2,
            ],
        )
        self.cont_combos = Container(
            expand=True,
            content=Column(
                expand=True,
                controls=[
                    Column(
                        scroll=ScrollMode.AUTO,
                        expand=True,
                        controls=[self.eplist_combo],
                    ),
                    Column(
                        controls=[
                            Container(
                                expand=True,
                                bgcolor=self.color_black26,
                                border_radius=5,
                                padding=5,
                                content=Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    height=40,
                                    expand=True,
                                    controls=[
                                        self.ebtn_crear_combo,
                                        self.ver_divider,
                                        self.ebtn_editar_combo,
                                        self.obtn_eliminar_combo,
                                    ],
                                ),
                            )
                        ]
                    ),
                ],
            ),
        )
        self.cont_crear_combos = Container(
            visible=False,
            padding=5,
            bgcolor=self.color_black26,
            border_radius=5,
            expand=True,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Icon(name=Icons.ADD_CIRCLE_OUTLINE_OUTLINED),
                            Text(value="Crear combos"),
                        ]
                    ),
                    self.hor_divider,
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                expand=True,
                                controls=[
                                    self.tf_nombre_combo,
                                    # tf_descuento_combo,
                                    self.tf_precio_combo,
                                    self.ebtn_agregar_producto,
                                ],
                            ),
                            Row(
                                controls=[
                                    self.ebtn_guardar_combo,
                                    self.ibtn_cancelar_combo,
                                ]
                            ),
                        ],
                    ),
                    Column(
                        expand=True,
                        scroll=ScrollMode.AUTO,
                        controls=[
                            ResponsiveRow(expand=True, controls=[self.dt_combos])
                        ],
                    ),
                    Row(
                        height=30,
                        alignment=MainAxisAlignment.END,
                        controls=[self.txt_total_combo],
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        height=40,
                        controls=[
                            self.ebtn_ver_combos,
                            self.ver_divider,
                            self.ebtn_editar_combo2,
                            self.obtn_quitar_combo,
                        ],
                    ),
                ],
            ),
        )

        self.ad_seleccionar_productos = AlertDialog(
            modal=True,
            content=Container(
                width=450,
                height=200,
                # expand=True,
                content=Column(
                    height=200,
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Column(
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        Row(
                                            controls=[
                                                Icon(name=Icons.LOCAL_OFFER_OUTLINED),
                                                Text(value="Seleccione un producto"),
                                            ]
                                        ),
                                        Row(
                                            controls=[
                                                self.ibtn_cerrar_seleccionar_productos
                                            ]
                                        ),
                                    ],
                                ),
                                self.hor_divider,
                            ]
                        ),
                        Row(
                            expand=True,
                            controls=[
                                # TODO segir aqui
                                self.sb_buscar_producto,
                                self.tf_cantidad_producto,
                                self.txt_subtotal,
                            ],
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[self.ebtn_agregar],
                        ),
                        # txt_mensaje_alerta,
                    ],
                ),
            ),
        )

        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[
                self.cont_combos,
                self.cont_crear_combos,
            ],
        )
