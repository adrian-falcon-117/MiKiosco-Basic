from flet import (
    TextField,
    ElevatedButton,
    OutlinedButton,
    IconButton,
    Container,
    MainAxisAlignment,
    CrossAxisAlignment,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Colors,
    VerticalDivider,
    Divider,
    Column,
    Row,
    Icons,
    Icon,
    ResponsiveRow,
    Text,
    border,
    BorderSide,
    TextAlign,
    ScrollMode,
    AlertDialog,
    Chip,
    Dropdown,
    AutoComplete,
)
from controllers.controller_productos import ControllerProductos as my_controller


class ViewProducto(Container):
    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    ###Controles de Agregar Productos
    tf_descripcion = TextField(
        expand=True,
        multiline=True,
        max_lines=2,
        label="Descripcion",
        # col={"sm": 6, "md": 4, "xl": 2},
    )
    tf_cantidad = TextField(
        expand=True,
        label="Cantidad",
        # col={"sm": 6, "md": 4, "xl": 2},
    )
    tf_precio_compra = TextField(
        expand=True,
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
        label="Precion de compra",
        # col={"sm": 6, "md": 4, "xl": 2},
    )
    tf_recargo = TextField(
        expand=True,
        suffix_icon=Icons.PERCENT_ROUNDED,
        label="Recargo",
        # col={"sm": 6, "md": 4, "xl": 2},
    )
    tf_precio_venta = TextField(
        expand=True,
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
        label="Precio de venta",
        # col={"sm": 6, "md": 4, "xl": 2},
    )

    ibtn_cancelar_producto = IconButton(tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED)
    ebtn_guardar_producto = ElevatedButton(text="Guardar", icon=Icons.SAVE_OUTLINED)

    ### Controles de Productos
    dt_productos = DataTable(
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
                label=Text(value="Descripcion"),
            ),
            DataColumn(
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Precio de compra"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Recargo"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Precio de Venta"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )
    ebtn_editar = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
    obtn_eliminar = OutlinedButton(text="Eliminar", icon=Icons.DELETE_OUTLINE)
    ebtn_ver_combos = ElevatedButton(text="Ver combos", icon=Icons.VISIBILITY_OUTLINED)

    ###Controles del AlertDialog Eliminar
    ebtn_si = ElevatedButton(text="Si")
    obtn_no = OutlinedButton(text="No")

    ###Controles de Crear promocion
    dt_promocion2 = DataTable(
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
                label=Text(value="Descripcion"),
            ),
            DataColumn(
                tooltip="Cantidad incluida en la promocion",
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                tooltip="Descuento por unidad",
                label=Text(value="Descuento"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                tooltip="Precio por unidad",
                label=Text(value="Precio .Un"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                tooltip="El subtotal de este producto",
                label=Text(value="Subtotal"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )
    dt_combos = DataTable(
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
                label=Text(value="Descripcion"),
            ),
            DataColumn(
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Precio de compra"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Recargo"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                label=Text(value="Precio de Venta"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )
    ebtn_ver_productos = ElevatedButton(
        text="Ver productos", icon=Icons.VISIBILITY_OUTLINED
    )
    ebtn_crear_combo = ElevatedButton(
        text="Crear combo", icon=Icons.ADD_CIRCLE_OUTLINE_OUTLINED
    )
    obtn_promocion_cancelar = OutlinedButton(text="Cancelar")
    ebtn_promocion_quitar = ElevatedButton(text="Quitar")
    tf_promocion_nombre = TextField(label="Nombre de combo")
    txt_promocion_total = Text(value="Total:...")

    ebtn_editar_promocion = ElevatedButton(text="Editar combo")
    ebtn_activar_promocion = ElevatedButton(text="Activar")
    obtn_desactivar_promocion = OutlinedButton(text="Desactivar")

    ###Controles de crear Combos
    tf_nombre_combo = TextField(label="Nombre del combo")
    tf_descuento_combo = TextField(label="Descuento general")
    ebtn_agregar_producto = ElevatedButton(
        text="Agregar productos", icon=Icons.FORMAT_LIST_BULLETED_ADD
    )
    ebtn_guardar_combo = ElevatedButton(text="Guardar")
    ibtn_cancelar_combo = IconButton(tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED)
    ibtn_cerrar_agregar_producto = IconButton(icon=Icons.CLOSE)
    dt_promociones_activas = DataTable(
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

    ###Controles de Dialogo Agregar Producto
    ac_buscar_producto = AutoComplete()
    tx_nombre_prodecto = Text(value="Producto:")
    tf_cantidad_produto = TextField(label="Cantidad")
    tx_precio_subtotal = Text(value="Subtotal:")
    ebtn_agregar = ElevatedButton(text="Agregar")

    ##Contenedor Agregar Productos
    cont_agregar_producto = Container(
        padding=5,
        bgcolor=color_black26,
        border_radius=5,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.FORMAT_LIST_BULLETED_ADD),
                        Text(value="Agregar productos"),
                    ]
                ),
                hor_divider,
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        tf_descripcion,
                        tf_cantidad,
                        tf_precio_compra,
                        tf_recargo,
                        tf_precio_venta,
                        Row(
                            controls=[ebtn_guardar_producto, ibtn_cancelar_producto],
                        ),
                    ],
                ),
            ],
        ),
    )

    ##Contenedor Productos
    cont_producto = Container(
        expand=True,
        padding=5,
        bgcolor=color_black26,
        border_radius=5,
        content=Column(
            expand=True,
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            controls=[
                                Icon(name=Icons.FORMAT_LIST_BULLETED_OUTLINED),
                                Text(value="Productos"),
                            ]
                        ),
                    ],
                ),
                hor_divider,
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[
                        ResponsiveRow(expand=True, controls=[dt_productos]),
                    ],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[ebtn_ver_combos, ebtn_editar, obtn_eliminar],
                ),
            ],
        ),
    )

    cont_productos = Container(
        # padding=5,
        # bgcolor=color_black26,
        border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[cont_agregar_producto, cont_producto],
        ),
    )

    ##Contenedor Crear combos
    cont_combos = Container(
        visible=False,
        padding=5,
        bgcolor=color_black26,
        border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.DISCOUNT_OUTLINED),
                        Text(value="Combos"),
                    ]
                ),
                hor_divider,
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[ResponsiveRow(expand=True, controls=[dt_combos])],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ebtn_ver_productos,
                        ebtn_crear_combo,
                    ],
                ),
            ],
        ),
    )

    cont_crear_combos = Container(
        visible=False,
        # padding=5,
        # bgcolor=color_black26,
        # border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.DISCOUNT_OUTLINED),
                        Text(value="Crear combos"),
                    ]
                ),
                hor_divider,
                Row(
                    controls=[
                        tf_nombre_combo,
                        tf_descuento_combo,
                        ebtn_agregar_producto,
                        ebtn_guardar_combo,
                        ibtn_cancelar_combo,
                    ]
                ),
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[ResponsiveRow(expand=True, controls=[dt_combos])],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ebtn_ver_productos,
                        ebtn_crear_combo,
                    ],
                ),
            ],
        ),
    )

    ad_crear_combos = AlertDialog(modal=True)

    ad_eliminar_producto = AlertDialog(
        modal=True,
        title=Text("Esta seguro de eliminar?"),
        content=Row(alignment=MainAxisAlignment.CENTER, controls=[ebtn_si, obtn_no]),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[self.cont_productos, self.cont_combos],
        )
