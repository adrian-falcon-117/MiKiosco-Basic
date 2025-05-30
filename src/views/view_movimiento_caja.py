from flet import (
    Container,
    MenuBar,
    MenuItemButton,
    SubmenuButton,
    Icon,
    Icons,
    Column,
    Row,
    ScrollMode,
    MainAxisAlignment,
    Text,
    TextField,
    ElevatedButton,
    OutlinedButton,
    IconButton,
    Colors,
    Divider,
    VerticalDivider,
    ExpansionPanelList,
    ExpansionPanel,
    padding,
    AlertDialog,
    Dropdown,
)

from controllers.controller_movimiento_caja import (
    ControllerMovimientoCaja as my_controller,
)


class ViewMovimientoCaja(Container):

    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    tx_nombre_usuario = Text(value="Juan Cabeza")
    tx_apertura_caja = Text(value="Apertura: $...")
    tx_cierre_caja = Text(value="Cierre: $...")
    tx_diferencia_caja = Text(value="Diferencia: $...")
    tx_fecha = Text(value="20/02/2020")
    tx_egreso_caja = Text(value="Egresos: $ ...")
    tx_motivo_egreso_caja = Text(value="Motivo: ...")
    tx_ingreso_caja = Text(value="Ingreso: $ ...")
    tx_motivo_ingreso_caja = Text(value="Motivo: ...")

    item_apertura_caja = MenuItemButton(
        leading=Icon(name=Icons.MOVE_TO_INBOX_OUTLINED),
        content=Text("Apertura de caja"),
    )
    item_generar_movimiento = MenuItemButton(
        leading=Icon(name=Icons.INBOX_OUTLINED),
        content=Text("Generar movimieto"),
    )
    item_cierre_caja = MenuItemButton(
        leading=Icon(name=Icons.OUTBOX_OUTLINED),
        content=Text("Cierre de caja"),
    )
    mb_movimietos_caja = MenuBar(
        controls=[
            SubmenuButton(
                leading=Icon(name=Icons.ALL_INBOX_OUTLINED),
                content=Text(value="Movimientos de caja"),
                controls=[
                    item_apertura_caja,
                    item_generar_movimiento,
                    item_cierre_caja,
                ],
            )
        ]
    )
    ep_movimietos = ExpansionPanel(
        expand=True,
        header=Container(
            padding=padding.only(left=5),
            content=Row(
                expand=True,
                controls=[Text(value="Caja de:"), tx_nombre_usuario],
            ),
        ),
        content=Container(
            padding=5,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            tx_fecha,
                            tx_apertura_caja,
                            tx_cierre_caja,
                            tx_diferencia_caja,
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            tx_ingreso_caja,
                            tx_motivo_ingreso_caja,
                            tx_egreso_caja,
                            tx_motivo_egreso_caja,
                        ],
                    ),
                ],
            ),
        ),
    )
    eplist_movimientos_caja = ExpansionPanelList(
        expand=True,
        # divider_color=color_divider,
        controls=my_controller.list_ep_movimiento(),
    )

    ###Controles de Dialog Apertura de Caja
    tf_apertura_caja = TextField(
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED, label="Ingrese un monto"
    )
    ebtn_abrir_caja = ElevatedButton(text="Abrir caja")
    ibtn_cerrar_apertura_caja = IconButton(icon=Icons.CLOSE)

    ###Controles de Dialog Cierre de Caja
    tf_cierre_caja = TextField(
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED, label="Ingrese un monto"
    )
    ebtn_cerrar_caja = ElevatedButton(text="Cerrar caja")
    ibtn_cerrar_cierre_caja = IconButton(icon=Icons.CLOSE)

    ###Controles de Dialog Movimiento de Caja
    dd_movimiento_caja = Dropdown(
        label="Seleccione un movimiento",
        width=300,
        leading_icon=Icons.INBOX_OUTLINED,
        options=my_controller.lista_movimientos_caja(),
    )
    tf_movimiento_caja = TextField(
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED, label="Ingrese un monto"
    )
    ebtn_movimiento_caja = ElevatedButton(text="Generar movimiento")
    ibtn_cerrar_movimiento_caja = IconButton(icon=Icons.CLOSE)

    ad_apertura_caja = AlertDialog(
        modal=True,
        content=Container(
            height=200,
            content=Column(
                # expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        expand=True,
                        controls=[
                            Row(
                                controls=[
                                    Icon(name=Icons.MOVE_TO_INBOX_OUTLINED),
                                    Text(value="Apertura de caja"),
                                ]
                            ),
                            ibtn_cerrar_apertura_caja,
                        ],
                    ),
                    hor_divider,
                    tf_apertura_caja,
                    Row(
                        expand=True,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[ebtn_abrir_caja],
                    ),
                ],
            ),
        ),
    )

    ad_cierre_caja = AlertDialog(
        modal=True,
        content=Container(
            height=200,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        expand=True,
                        controls=[
                            Row(
                                controls=[
                                    Icon(name=Icons.OUTBOX_OUTLINED),
                                    Text(value="Cierre de caja"),
                                ]
                            ),
                            ibtn_cerrar_cierre_caja,
                        ],
                    ),
                    hor_divider,
                    tf_cierre_caja,
                    Row(
                        expand=True,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[ebtn_cerrar_caja],
                    ),
                ],
            ),
        ),
    )

    ad_movimiento_caja = AlertDialog(
        modal=True,
        content=Container(
            height=300,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        expand=True,
                        controls=[
                            Row(
                                controls=[
                                    Icon(name=Icons.INBOX_OUTLINED),
                                    Text(value="Movimientos de caja"),
                                ]
                            ),
                            ibtn_cerrar_movimiento_caja,
                        ],
                    ),
                    hor_divider,
                    dd_movimiento_caja,
                    tf_movimiento_caja,
                    Row(
                        expand=True,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[ebtn_movimiento_caja],
                    ),
                ],
            ),
        ),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        # self.bgcolor = self.color_black26
        # self.border_radius = 5
        # self.padding = 5
        self.content = Column(
            expand=True,
            controls=[
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[self.eplist_movimientos_caja],
                ),
                Container(
                    bgcolor=self.color_black26,
                    border_radius=5,
                    padding=5,
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[self.mb_movimietos_caja],
                    ),
                ),
            ],
        )
