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
    Card,
    BottomSheet,
)

from controllers.controller_combos import ControllerCombo


# sa
class ViewCombos(Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.controller = ControllerCombo(page, self)
        self.expand = True

        self.color_black26 = Colors.BLACK26
        self.hor_divider = Divider()
        self.ver_divider = VerticalDivider()

        ##Controles------------------

        # Botones
        self.ebtn_editar_combo = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
        self.obtn_eliminar_combo = OutlinedButton(
            text="Eliminar", icon=Icons.DELETE_OUTLINE
        )
        self.ebtn_ver_combos = ElevatedButton(
            text="Ver combos",
            icon=Icons.DISCOUNT_OUTLINED,
            on_click=self.controller.on_ver_combos,
        )
        self.ebtn_editar_combo2 = ElevatedButton(
            text="Editar", icon=Icons.EDIT_OUTLINED
        )

        # Otos
        self.txt_mensaje_alerta = Text(color=Colors.RED)

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

        # self.bs_editar_producto = BottomSheet()
        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[
                self.cont_combos,
            ],
        )
