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
    AlertDialog,
    SearchBar,
    ListView,
    RoundedRectangleBorder,
    Card,
    BottomSheet,
)

from controllers.controller_crear_combos import ControllerCrearCombo


class ViewCrearCombos(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.controller = ControllerCrearCombo(page, self)
        self.expand = True

        ## Controles----------------------------------------------------------------

        self.color_black26 = Colors.BLACK26
        self.hor_divider = Divider()
        self.ver_divider = VerticalDivider()

        # Textos
        self.txt_precio_combo = Text(value="Precio: $...", size=20)
        self.txt_total_combo = Text(value="Total: $...")
        self.txt_subtotal = Text(value="Subtotal: $0")

        # Campos de texto
        self.tf_nombre_combo = TextField(
            label="Nombre del combo", on_change=self.controller.on_nombre_combo
        )
        self.tf_cantidad_producto = TextField(
            label="Cantidad",
            width=150,
            disabled=True,
            on_change=self.controller.on_cambiar_cantidad,  # on_cantidad_producto,
        )
        self.tf_descuento_combo = TextField(
            label="Descuento",
            suffix_icon=Icons.PERCENT_ROUNDED,
            width=150,
            on_change=self.controller.on_descuento_combo,
            # on_blur=self.controller.on_blur_descuento_combo,
        )
        self.tf_precio_combo = TextField(
            prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
            label="Precio",
            width=150,
            on_change=self.controller.on_precio_combo,
        )

        # Botones
        self.ebtn_agregar_producto = ElevatedButton(
            text="Agregar producto",
            icon=Icons.ADD_CIRCLE_OUTLINE,
            on_click=self.controller.on_agregar_producto,
        )

        self.ebtn_guardar_combo = ElevatedButton(
            text="Guardar",
            icon=Icons.SAVE_OUTLINED,
            on_click=self.controller.on_guardar_combo,
        )
        self.obtn_quitar_combo = OutlinedButton(
            text="Quitar",
            icon=Icons.CANCEL_OUTLINED,
            disabled=True,
            on_click=self.controller.on_quitar_combo,
        )
        self.ibtn_cancelar_combo = IconButton(
            tooltip="Cancelar",
            icon=Icons.CLOSE_ROUNDED,
            on_click=self.controller.on_cancelar_combo,
        )

        self.ebtn_agregar_producto_combo = ElevatedButton(
            text="Agregar producto",
            disabled=True,
            on_click=self.controller.on_agregar_producto_combo,
        )
        self.ibtn_cerrar_agregar_productos = IconButton(
            tooltip="Cancelar",
            icon=Icons.CLOSE,
            on_click=self.controller.on_cerrar_agregar_producto,
        )

        # Otros
        self.lv_productos = ListView()
        self.sb_buscar_producto = SearchBar(
            expand=True,
            bar_hint_text="Buscar un producto",
            view_hint_text="Seleccione un producto",
            view_shape=RoundedRectangleBorder(radius=5),
            bar_shape=RoundedRectangleBorder(radius=5),
            controls=[self.lv_productos],
            on_change=self.controller.on_buscar_producto,
        )

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

        # Cuadro de dialogos
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
                                                self.ibtn_cerrar_agregar_productos
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
                                self.sb_buscar_producto,
                                self.tf_cantidad_producto,
                                self.txt_subtotal,
                            ],
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[self.ebtn_agregar_producto_combo],
                        ),
                        # txt_mensaje_alerta,
                    ],
                ),
            ),
        )

        self.content = Column(
            expand=True,
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            expand=True,
                            controls=[
                                self.tf_nombre_combo,
                                self.tf_descuento_combo,
                                # self.tf_precio_combo,
                                self.txt_precio_combo,
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
                    controls=[ResponsiveRow(expand=True, controls=[self.dt_combos])],
                ),
                Row(
                    height=30,
                    alignment=MainAxisAlignment.END,
                    controls=[self.txt_total_combo],
                ),
                Container(
                    # expand=True,
                    bgcolor=self.color_black26,
                    border_radius=5,
                    padding=5,
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        height=40,
                        controls=[
                            # self.ebtn_editar_combo2,
                            self.ebtn_agregar_producto,
                            self.obtn_quitar_combo,
                        ],
                    ),
                ),
            ],
        )
