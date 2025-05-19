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

    ###Controles del AlertDialog Eliminar
    ebtn_si = ElevatedButton(text="Si")
    obtn_no = OutlinedButton(text="No")

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
                    controls=[ebtn_editar, obtn_eliminar],
                ),
            ],
        ),
    )

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
            controls=[self.cont_agregar_producto, self.cont_producto],
        )
