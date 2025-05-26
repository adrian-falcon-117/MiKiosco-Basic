from flet import AutoCompleteSuggestion

from model.model_combos import ModelCombos as my_model


class ControllerCombo:

    @classmethod
    def resultado_burqueda_producto(self):
        lista_producto = []
        for i in my_model.get_descripcion_producto():
            lista_producto.append(
                AutoCompleteSuggestion(
                    key=i[0],
                    value=i[0],
                )
            )
        return lista_producto

    @classmethod
    def action_producto_seleccionado(self, descripcion):
        producto = my_model.get_producto(descripcion)

        return producto
