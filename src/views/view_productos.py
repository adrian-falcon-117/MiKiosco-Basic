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
from controllers.controller_productos import ControllerProductos


class ViewProducto(Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.controller = ControllerProductos(page, self)

        self.expand = True

        self.color_black26 = Colors.BLACK26
        self.hor_divider = Divider()
        self.ver_divider = VerticalDivider()

        ###Controles de Agregar Productos
        self.tf_descripcion = TextField(
            expand=True,
            multiline=True,
            max_lines=2,
            label="Descripcion",
            on_change=self.controller.on_descripcion,
            # col={"sm": 6, "md": 4, "xl": 2},
        )
        self.tf_cantidad = TextField(
            expand=True,
            label="Cantidad",
            on_change=self.controller.on_cantidad,
            # col={"sm": 6, "md": 4, "xl": 2},
        )
        self.tf_precio_compra = TextField(
            expand=True,
            prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
            label="Precion de compra",
            on_change=self.controller.on_precio_compra,
            # col={"sm": 6, "md": 4, "xl": 2},
        )
        self.tf_recargo = TextField(
            expand=True,
            suffix_icon=Icons.PERCENT_ROUNDED,
            label="Recargo",
            on_change=self.controller.on_recargo,
            # col={"sm": 6, "md": 4, "xl": 2},
        )
        self.tf_precio_venta = TextField(
            expand=True,
            prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
            label="Precio de venta",
            on_change=self.controller.on_precio_venta,
            # col={"sm": 6, "md": 4, "xl": 2},
        )

        self.ibtn_cancelar_producto = IconButton(
            tooltip="Cancelar",
            icon=Icons.CLOSE_ROUNDED,
            on_click=self.controller.on_cancelar,
        )
        self.ebtn_guardar_producto = ElevatedButton(
            text="Guardar",
            icon=Icons.SAVE_OUTLINED,
            on_click=self.controller.on_guardar_producto,
        )

        ### Controles de Productos
        self.dt_productos = DataTable(
            # expand=True,
            # data_row_max_height=40,
            show_checkbox_column=True,
            checkbox_horizontal_margin=5,
            border=border.all(1),
            border_radius=5,
            vertical_lines=BorderSide(1),
            heading_row_color=self.color_black26,
            sort_column_index=1,
            sort_ascending=True,
            columns=[
                DataColumn(
                    numeric=True,
                    heading_row_alignment=MainAxisAlignment.START,
                    label=Text(value="ID"),
                    tooltip = "Ordenar por",
                    on_sort=self.controller.on_descripcion_ordenar,
                ),
                DataColumn(
                    heading_row_alignment=MainAxisAlignment.START,
                    label=Text(value="Descripcion"),
                    tooltip = "Ordenar por",
                    on_sort=self.controller.on_descripcion_ordenar,
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Cantidad"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Precio de compra"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Recargo"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
                DataColumn(
                    numeric=True,
                    label=Text(value="Precio de Venta"),
                    heading_row_alignment=MainAxisAlignment.START,
                ),
            ],
            rows=self.controller.datos_tabla(""),
        )

        self.ebtn_editar = ElevatedButton(
            text="Editar",
            icon=Icons.EDIT_OUTLINED,
            on_click=self.controller.on_editar_producto,
        )
        self.obtn_eliminar = OutlinedButton(
            text="Eliminar",
            icon=Icons.DELETE_OUTLINE,
            on_click=self.controller.on_eliminar,
        )

        ###Controles del AlertDialog Eliminar
        self.ebtn_si = ElevatedButton(
            text="Si", on_click=self.controller.on_si_eliminar
        )
        self.obtn_no = OutlinedButton(
            text="No", on_click=self.controller.on_no_eliminar
        )

        ##Contenedor Agregar Productos
        self.cont_agregar_producto = Container(
            padding=5,
            bgcolor=self.color_black26,
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
                    self.hor_divider,
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.tf_descripcion,
                            self.tf_cantidad,
                            self.tf_precio_compra,
                            self.tf_recargo,
                            self.tf_precio_venta,
                            Row(
                                controls=[
                                    self.ebtn_guardar_producto,
                                    self.ibtn_cancelar_producto,
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )

        ##Contenedor Productos
        self.cont_botones_inferior = Row(
            alignment=MainAxisAlignment.CENTER,
            disabled=True,
            controls=[self.ebtn_editar, self.obtn_eliminar],
        )
        self.cont_producto = Container(
            expand=True,
            padding=5,
            bgcolor=self.color_black26,
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
                    self.hor_divider,
                    Column(
                        expand=True,
                        scroll=ScrollMode.AUTO,
                        controls=[
                            ResponsiveRow(expand=True, controls=[self.dt_productos]),
                        ],
                    ),
                    self.cont_botones_inferior,
                ],
            ),
        )

        self.ad_eliminar_producto = AlertDialog(
            modal=True,
            title=Text("Esta seguro de eliminar?"),
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[self.ebtn_si, self.obtn_no],
            ),
        )

        self.ad_editar_producto = AlertDialog(
            modal=True,
            content=Column(
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[self.tf_descripcion],
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[self.tf_cantidad, self.tf_precio_compra],
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[self.tf_recargo, self.tf_precio_venta],
                    ),
                ]
            ),
        )

        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[self.cont_agregar_producto, self.cont_producto],
        )
