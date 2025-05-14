from flet import (
    Container,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    border,
    BorderSide,
    Colors,
    Icons,
    Icon,
    MainAxisAlignment,
    Text,
    Divider,
    VerticalDivider,
    ExpansionPanelList,
    ExpansionPanel,
    Row,
    Column,
    ScrollMode,
    Dropdown,
    ElevatedButton,
    OutlinedButton,
    IconButton,
    padding,
)

from controllers.controller_ventas import ControllerVentas as my_controller


class ViewVentas(Container):

    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    dd_fecha_venta = Dropdown(
        label="Seleccione una fecha",
        width=300,
        leading_icon=Icons.CALENDAR_MONTH_OUTLINED,
        options=my_controller.lista_fecha_venta(),
    )
    tx_num_venta = Text(value="Venta N°: ...")
    tx_fecha_venta = Text(value="20/02/2020")

    tx_total_efectivo = Text(value="Efectivo: ...")
    tx_total_transferencia = Text(value="Transferencia: ...")
    tx_total_debito = Text(value="Debito: ...")
    tx_total_credito = Text(value="Credito: ...")

    dt_ventas = DataTable(
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
                numeric=True,
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="ID Producto"),
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
                label=Text(value="Recargo"),
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
                    DataCell(content=Text(value="...")),
                    DataCell(content=Text(value="...")),
                ],
            ),
        ],
    )
    obtn_anular_venta = OutlinedButton(text="Anular venta")
    ebtn_quitar_seleccion = ElevatedButton("Quitar seleccion")
    cont_ventas = Container(
        padding=5,
        expand=True,
        content=Column(
            controls=[
                Column(expand=True, scroll=ScrollMode.AUTO, controls=[dt_ventas]),
                Row(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[ebtn_quitar_seleccion, obtn_anular_venta],
                ),
            ]
        ),
    )

    ep_venta = ExpansionPanel(
        header=Container(
            padding=padding.only(left=5),
            content=Row(
                expand=True,
                controls=[tx_num_venta, tx_fecha_venta],
            ),
        ),
        expand=True,
        content=cont_ventas,
    )
    ep_venta_1 = ExpansionPanel(expand=True, content=dt_ventas)
    ep_venta_2 = ExpansionPanel(expand=True, content=dt_ventas)
    eplist_ventas = ExpansionPanelList(
        expand=True,
        # divider_color=color_divider,
        controls=[ep_venta, ep_venta_1, ep_venta_2],
    )

    cont_totales = Container(
        padding=5,
        bgcolor=color_black26,
        border_radius=5,
        # expand=True,
        height=100,
        content=Column(
            expand=True,
            controls=[
                Row(
                    expand=True,
                    controls=[
                        Icon(name=Icons.ACCOUNT_BALANCE_WALLET_OUTLINED),
                        Text(value="Totales del dia"),
                    ],
                ),
                hor_divider,
                Row(
                    expand=True,
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        tx_total_efectivo,
                        tx_total_transferencia,
                        tx_total_debito,
                        tx_total_credito,
                    ],
                ),
            ],
        ),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        self.padding = 5
        self.bgcolor = self.color_black26
        self.border_radius = 5
        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=(
                self.dd_fecha_venta,
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[
                        self.eplist_ventas,
                    ],
                ),
                Column(
                    # expand=True,
                    controls=[
                        self.cont_totales,
                    ],
                ),
            ),
        )
