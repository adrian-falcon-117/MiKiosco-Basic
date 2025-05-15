from flet import DropdownOption, Text, AutoCompleteSuggestion
from views import view_caja as my_view
from model.model_caja import ModelCaja as my_model


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
    def resultado_burqueda_producto(self):
        lista_producto = []
        for i in my_model.get_productos():
            lista_producto.append(
                AutoCompleteSuggestion(
                    key=i[1],
                    value=i[1],
                )
            )
        return lista_producto

    @classmethod
    def action_ebtn_quitar_lista(self):
        instancia = my_view.ViewPaginaPrincipal()
        instancia.num_caja.value = "Hola mundo"
