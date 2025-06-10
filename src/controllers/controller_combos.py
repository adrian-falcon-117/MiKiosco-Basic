from flet import AutoCompleteSuggestion, Text, ListTile, ListView

from model.model_combos import ModelCombos as my_model
from views import view_combos as my_view


class ControllerCombo:

    id_producto = None
    descripcion_producto = None
    precio_producto = 0
    cantidad = None
    subtotal = None
    producto_combo = []

    total_combo = 0

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

        self.id_producto = producto[0][0]
        self.descripcion_producto = producto[0][1]
        self.precio_producto = producto[0][2]

    # Cuando se selecciona un producto de las sugerencias

    # Cuando se cambia la cantidad de producto a agregar
    @classmethod
    def action_cambiar_cantidad(self, cantidad):
        v = my_view.ViewCombos()
        self.cantidad = cantidad
        print(self.precio_producto)
        try:
            v.tf_cantidad_producto.error_text = None
            self.subtotal = int(self.precio_producto) * int(self.cantidad)
            v.txt_subtotal.value = f"Subtotal: ${self.subtotal}"
        except ValueError:
            v.tf_cantidad_producto.error_text = "Requerido"
            v.txt_subtotal.value = "Subtotal: $0"

    def on_seleccionar_producto(self, e):
        v = my_view.ViewCombos()
        self.id_producto = e.control.data
        self.descripcion_producto = e.control.title.value
        self.precio_producto = e.control.key

        v.sb_buscar_producto.close_view(e.control.title.value)

        print(self.id_producto)
        print(self.descripcion_producto)
        print(self.precio_producto)

    # Cuando se busca un producto les aparecera sugerencias que conuncidan con la busqueda
    @classmethod
    def action_buscar_producto(self, descripcion):
        v = my_view.ViewCombos()
        v.lv_productos.controls.clear()
        for i in my_model.get_producto2(descripcion):
            v.lv_productos.controls.append(
                ListTile(
                    title=Text(value=i[1]),
                    subtitle=Text(value=f"${i[2]}"),
                    data=i[0],
                    key=i[2],
                    on_click=lambda e: self.on_seleccionar_producto(self, e),
                )
            )

    @classmethod
    def action_obtener_combo(self):
        if self.id_producto and self.descripcion_producto and self.cantidad:
            self.producto_combo.append(
                (
                    self.id_producto,
                    self.descripcion_producto,
                    self.cantidad,
                    self.subtotal,
                )
            )
        return self.producto_combo

    def action_agregar_producto_combo(self):
        v = my_view.ViewCombos()
        if not self.id_producto:
            pass

    def action_guardar_combo(self):
        v = my_view.ViewCombos()
        nombre_combo = v.tf_nombre_combo.value

    @classmethod
    def sumar_total(self, total):
        v = my_view.ViewCombos()
        self.total_combo = total
        print(f"Total: {self.total_combo}")
        v.tf_total_combo.value = self.total_combo

    @classmethod
    def limpiar_variables(self):
        v = my_view.ViewCombos()
        self.precio_producto = 1
        self.id_producto = None
        self.descripcion_producto = None
        self.cantidad = None
        self.subtotal = None
        v.txt_mensaje_alerta.value = ""

        # return Text(value=producto[0])
