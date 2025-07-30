from flet import AutoCompleteSuggestion, Text, ListTile, Container, DataRow, DataCell

from model.model_combos import ModelCombos
from views.mensaje import Mensaje


class ControllerCombo(Container):

    def __init__(self, page, view):
        super().__init__()
        self.page = page
        self.view = view
        self.model = ModelCombos()
        self.mensaje = Mensaje(self.page)

    id_producto = None
    descripcion_producto = None
    precio_producto = 0
    cantidad = None
    subtotal = None
    producto_combo = {}

    precio_total = 0
    precio_descuento = 0
    descuento = 0
    nombre_combo = None

    # Activa el contenedor Crear combo
    def on_crear_combo(self, e):
        self.view.cont_crear_combos.visible = True
        self.view.cont_combos.visible = False
        self.page.update()

    # Activa el contenedor Ver combos
    def on_ver_combos(self, e):
        self.view.cont_crear_combos.visible = False
        self.view.cont_combos.visible = True
        self.view.ebtn_ver_combos.data
        self.page.update()

    # Abre el Cuadro de dialogo para Buscar un producto
    def on_agregar_producto(self, e):
        self.page.open(self.view.ad_seleccionar_productos)

    # Cierra el Cuadro de dialogo para Buscar un producto y Reestablese las variables y campos de textos
    def on_cerrar_agregar_producto(self, e):
        self.clear_all()
        self.view.sb_buscar_producto.value = ""
        self.page.close(self.view.ad_seleccionar_productos)

    def on_cambiar_cantidad(self, e):
        self.view.tf_cantidad_producto.error_text = None
        try:
            self.cantidad = int(e.control.value)
            self.subtotal = int(self.precio_producto) * self.cantidad
            self.view.txt_subtotal.value = f"Subtotal: ${self.subtotal}"
            self.view.ebtn_agregar_producto_combo.disabled = False

        except ValueError:
            self.view.tf_cantidad_producto.value = None
            self.view.tf_cantidad_producto.error_text = "Ingrese solo números"
            self.view.txt_subtotal.value = "Subtotal: $0"
            self.view.ebtn_agregar_producto_combo.disabled = True

        self.page.update()

    # Cuando se selecciona un item de la lista de sugerencias
    def on_seleccionar_producto(self, e):
        self.id_producto = e.control.data
        self.descripcion_producto = e.control.title.value
        self.precio_producto = e.control.key

        self.view.tf_cantidad_producto.disabled = False

        self.view.sb_buscar_producto.close_view(e.control.title.value)

        self.page.update()

    # Cuando se busca un producto les aparecera sugerencias que concidan con la busqueda
    def buscar_producto(self, descripcion):
        self.view.lv_productos.controls.clear()
        for i in self.model.get_producto2(descripcion):
            if i[1]:
                self.view.lv_productos.controls.append(
                    ListTile(
                        title=Text(value=i[1]),
                        subtitle=Text(value=f"${i[2]}"),
                        data=i[0],
                        key=i[2],
                        on_click=self.on_seleccionar_producto,
                    )
                )

    # Cuando se esta buscando un producto en el campo de texto
    def on_buscar_producto(self, e):
        if e.data:
            self.buscar_producto(e.data)
            self.view.sb_buscar_producto.open_view()

        self.clear_all()
        self.view.ebtn_agregar_producto_combo.disabled = True
        self.page.update()

    def obtener_combo(self):
        if self.id_producto in self.producto_combo:
            self.producto_combo[self.id_producto]["cantidad"] += self.cantidad
            self.producto_combo[self.id_producto]["precio"] += self.subtotal
        else:
            self.producto_combo[self.id_producto] = {
                "id": self.id_producto,
                "descripcion": self.descripcion_producto,
                "cantidad": self.cantidad,
                "precio": self.subtotal,
            }

    # Cuando se cambia el precio total del Combo
    def on_precio_combo(self, e):
        self.view.tf_precio_combo.error_text = ""

        try:
            self.precio_total = int(e.control.value)

        except ValueError as e:
            self.view.tf_precio_combo.error_text = "Ingrese un precio"
            self.view.tf_precio_combo.value = ""
        self.page.update()

    # Cuando se selecciona una fila de la tabla
    def on_seleccionar_fila_producto(self, e):
        if e.control.selected:
            e.control.selected = False
            self.view.obtn_quitar_combo.disabled = True
            self.id_producto = None
        else:
            for i in range(len(self.view.dt_combos.rows)):
                self.view.dt_combos.rows[i].selected = False
            e.control.selected = True

            self.view.obtn_quitar_combo.disabled = False
            self.id_producto = e.control.cells[0].content.value
        self.page.update()

    def actualizar_datos(self, total, lista_producto):
        self.view.obtn_quitar_combo.disabled = True
        self.view.txt_total_combo.value = f"Total: ${total}"
        # self.view.tf_precio_combo.value = total
        self.view.dt_combos.rows = lista_producto

    def productos_del_combo(self):
        lista_producto = []
        total = 0
        for producto, i in self.producto_combo.items():
            total += i["precio"]
            lista_producto.append(
                DataRow(
                    on_select_changed=self.on_seleccionar_fila_producto,
                    # data=i[0],
                    cells=[
                        DataCell(content=Text(value=i["id"])),  # id
                        DataCell(content=Text(value=i["descripcion"])),  # descripcion
                        DataCell(content=Text(value=i["cantidad"])),  # cantidad
                        DataCell(content=Text(value=i["precio"])),  # subtotal
                    ],
                ),
            )
        self.precio_total = int(total)
        self.aplicar_descuento(total)
        self.actualizar_datos(total, lista_producto)
        self.page.update()

    # TODO Segir aqui
    def aplicar_descuento(self, total):
        total = int(total - (total * self.descuento / 100))
        self.view.txt_precio_combo.value = f"Precio: ${total}"

    def on_descuento_combo(self, e):
        self.view.tf_descuento_combo.error_text = ""
        try:
            self.descuento = int(e.control.value)
            self.aplicar_descuento(self.precio_total)
        except:
            self.view.tf_descuento_combo.error_text = "Solo números"
            self.view.tf_descuento_combo.value = ""
            self.view.txt_precio_combo.value = f"Precio: ${self.precio_total}"
        self.page.update()

    def on_blur_descuento_combo(self, e):
        self.view.tf_descuento_combo.error_text = ""
        self.page.update()

    def on_quitar_combo(self, e):
        del self.producto_combo[self.id_producto]

        self.productos_del_combo()

    def on_agregar_producto_combo(self, e):
        self.obtener_combo()
        self.productos_del_combo()
        self.on_cerrar_agregar_producto(e)
        self.page.update()

    def on_guardar_combo(self, e):
        nombre_combo = self.view.tf_nombre_combo.value
        precio_combo = self.view.tf_precio_combo.value

        if nombre_combo and precio_combo and self.producto_combo:
            for producto, i in self.producto_combo.items():
                self.model.create(
                    nombre_combo,
                    precio_combo,
                    i["id"],
                    i["descripcion"],
                    i["cantidad"],
                    i["precio"],
                )
        self.mensaje.mensaje_ok("Guardado")

    # Recetea las variables y campos de textos
    def on_cancelar_combo(self, e):
        self.mensaje.mensaje("Cancelado")

    def clear_all(self):
        self.view.tf_cantidad_producto.value = ""
        self.view.tf_cantidad_producto.error_text = None
        self.view.tf_cantidad_producto.disabled = True
        self.view.ebtn_agregar_producto_combo.disabled = True
        self.view.txt_subtotal.value = "Subtotal: $0"
        self.precio_producto = 0
        self.id_producto = None
        self.descripcion_producto = None
        self.cantidad = None
        self.subtotal = None
        self.view.txt_mensaje_alerta.value = ""
        # self.precio_combo = 0

        # return Text(value=producto[0])
