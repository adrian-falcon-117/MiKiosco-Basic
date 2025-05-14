from flet import DropdownOption, Text


class ControllerVentas:

    fecha_venta = ["20/02/2020", "21/02/2020", "22/02/2020"]

    @classmethod
    def lista_fecha_venta(self):
        lista = []
        for i in self.fecha_venta:
            lista.append(DropdownOption(key=i, content=(Text(value=i))))

        return lista
