from flet import AutoCompleteSuggestion, Text, ListTile, Container

from model.model_combos import ModelCombos as my_model
from views import view_combos as my_view


class ControllerCombo(Container):

    def __init__(self, page, view):
        super().__init__()
        self.page = page
        self.view = view

    id_producto = None
    descripcion_producto = None
    precio_producto = 0
    cantidad = None
    subtotal = None
    producto_combo = []

    precio_combo = 0
    descuento_general = 0
    nombre_combo = None

    def on_crear_combo(self, e):
        self.view.cont_crear_combos.visible = True
        self.view.cont_combos.visible = False
        self.page.update()

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

    # Cuando se selecciona un producto de las sugerencias
    @classmethod
    def action_producto_seleccionado(self, descripcion):
        producto = my_model.get_producto(descripcion)

        self.id_producto = producto[0][0]
        self.descripcion_producto = producto[0][1]
        self.precio_producto = producto[0][2]

    # Cuando se cambia la cantidad de producto a agregar
    @classmethod
    def action_cambiar_cantidad(self, cantidad):
        v = my_view.ViewCombos()
        # v.tf_cantidad_producto.value = ""
        self.cantidad = cantidad
        try:
            v.tf_cantidad_producto.error_text = None
            self.subtotal = int(self.precio_producto) * int(self.cantidad)
            v.txt_subtotal.value = f"Subtotal: ${self.subtotal}"
        except ValueError:
            v.tf_cantidad_producto.value = None
            v.tf_cantidad_producto.error_text = "Requerido"
            v.txt_subtotal.value = "Subtotal: $0"

    # Cuando se selecciona un producto de la lista de sugerencias
    def on_seleccionar_producto(self, e):
        # v = my_view.ViewCombos()
        self.id_producto = e.control.data
        self.descripcion_producto = e.control.title.value
        self.precio_producto = e.control.key

        self.view.ebtn_agregar.disabled = False
        self.view.tf_cantidad_producto.disabled = False

        self.view.sb_buscar_producto.close_view(e.control.title.value)

        self.page.update()

        print(self.id_producto)
        print(self.descripcion_producto)
        print(self.precio_producto)

    def on_buscar_producto_combo(self, e):

        if e.data:
            self.action_buscar_producto(e.data)
            self.view.sb_buscar_producto.open_view()
        else:
            self.view.sb_buscar_producto.close_view()
            self.limpiar_variables()
            self.action_cambiar_cantidad(0)
        self.page.update()

    # Cuando se busca un producto les aparecera sugerencias que concidan con la busqueda
    def action_buscar_producto(self, descripcion):
        self.view.lv_productos.controls.clear()
        for i in my_model.get_producto2(descripcion):
            self.view.lv_productos.controls.append(
                ListTile(
                    title=Text(value=i[1]),
                    subtitle=Text(value=f"${i[2]}"),
                    data=i[0],
                    key=i[2],
                    on_click=lambda e: self.on_seleccionar_producto(self, e),
                )
            )

    # Cuando se selecciona un producto para agregar al combo
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

    @classmethod
    def action_descuento_combo(self, descuento):
        v = my_view.ViewCombos()
        v.tf_descuento_combo.error_text = ""
        try:
            # v.tf_descuento_combo.value = descuento
            total = self.total_combo - int(descuento)
            v.tf_total_combo.value = total
        except ValueError:
            v.tf_total_combo.value = self.total_combo
            v.tf_descuento_combo.value = ""
            v.tf_descuento_combo.error_text = "Ingrese un valor"

    def action_agregar_producto_combo(self):
        v = my_view.ViewCombos()
        if not self.id_producto:
            pass

    def action_guardar_combo(self):
        v = my_view.ViewCombos()
        nombre_combo = v.tf_nombre_combo.value

    # Segir aca
    @classmethod
    def total_combo(self, total):
        v = my_view.ViewCombos()
        self.precio_combo = total
        v.txt_total_combo.value = f"Total: ${self.precio_combo}"

    @classmethod
    def action_precio_combo(self, total):
        v = my_view.ViewCombos()
        v.tf_precio_combo.error_text = ""

        try:
            total_modificado = int(total)
            # print(f"Total: {self.total_combo}")
            v.tf_precio_combo.value = total_modificado

        except ValueError as e:
            v.tf_precio_combo.value = 0
            v.tf_precio_combo.error_text = "Ingrese un valor"

    @classmethod
    def limpiar_variables(self):
        v = my_view.ViewCombos()
        v.tf_cantidad_producto.value = ""
        v.tf_cantidad_producto.error_text = None
        v.sb_buscar_producto.value = ""
        v.txt_subtotal.value = "Subtotal: $0"
        self.precio_producto = 1
        self.id_producto = None
        self.descripcion_producto = None
        self.cantidad = None
        self.subtotal = None
        v.txt_mensaje_alerta.value = ""
        self.precio_combo = 0

        # return Text(value=producto[0])
