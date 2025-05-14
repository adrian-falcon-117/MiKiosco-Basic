from flet import (
    ExpansionPanel,
    Row,
    Column,
    MainAxisAlignment,
    Text,
    Container,
    padding,
    DropdownOption,
)
from views import view_movimiento_caja as my_view


class ControllerMovimientoCaja:
    movimientos_caja = ["Ingreso", "Egreso"]

    @classmethod
    def lista_movimientos_caja(self):
        lista = []
        for i in self.movimientos_caja:
            lista.append(DropdownOption(key=i, content=Text(value=i)))
        return lista

    @classmethod
    def list_ep_movimiento(self):
        lista = []
        exp = ExpansionPanel(
            expand=True,
            header=Container(
                padding=padding.only(left=5),
                content=Row(
                    expand=True,
                    controls=[Text(value="Hola:")],
                ),
            ),
            content=Container(Text(value="Soy Dora")),
        )
        lista.append(exp)
        return lista

    def __init__(self):
        pass
