from flet import DropdownOption, Text, AutoCompleteSuggestion
from views import view_caja as my_view


class ControllerCaja:

    # Lista de precios
    precio = ["Venta", "Promociones"]

    # Lista de Cuotas
    cuotas = ["1", "2", "3"]

    # Lista de agregar a cuenta corriente
    agregar = ["Todos", "Solo seleccionados"]

    # Lista de las sugerencias de los productos buscados
    productos = ["Gaseosa", "Vinos", "Pan", "Jamon"]

    @classmethod
    def lista_precio_lista(self):
        lista = []
        for i in self.precio:
            lista.append(DropdownOption(key=i, content=Text(value=i)))
        return lista

    @classmethod
    def lista_cantidad_cuotas(self):
        lista = []
        for i in self.cuotas:
            lista.append(DropdownOption(key=i, content=Text(value=i)))
        return lista

    @classmethod
    def lista_agregar_cuenta_corriente(self):
        lista = []
        for i in self.agregar:
            lista.append(DropdownOption(key=i, content=Text(value=i)))
        return lista

    @classmethod
    def lista_resultado_productos(self):
        lista = []
        for i in self.productos:
            lista.append(
                AutoCompleteSuggestion(
                    key=i,
                    value=i,
                )
            )
        return lista

    @classmethod
    def action_ebtn_quitar_lista(self):
        instancia = my_view.ViewPaginaPrincipal()
        instancia.num_caja.value = "Hola mundo"
