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
)


class ViewCombos(Container):

    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    ###Controles de crear Combos
    tf_nombre_combo = TextField(label="Nombre del combo")
    tf_descuento_combo = TextField(label="Descuento general")
    ebtn_agregar_producto = ElevatedButton(
        text="Agregar productos", icon=Icons.FORMAT_LIST_BULLETED_ADD
    )
    ebtn_guardar_combo = ElevatedButton(text="Guardar")
    ibtn_cancelar_combo = IconButton(tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED)
    ibtn_cerrar_agregar_producto = IconButton(icon=Icons.CLOSE)

    ebtn_ver_productos = ElevatedButton(
        text="Ver productos", icon=Icons.VISIBILITY_OUTLINED
    )
    ebtn_crear_combo = ElevatedButton(
        text="Crear combo", icon=Icons.ADD_CIRCLE_OUTLINE_OUTLINED
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

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[],
        )
