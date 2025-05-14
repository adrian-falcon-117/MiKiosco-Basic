from flet import Text, AutoCompleteSuggestion
from views import view_productos as my_view
from model.model_productos import ModelProductos as my_model


class ControllerProductos:

    id_productos = None

    @classmethod
    def action_ch_productos():
        mv_instancia = my_view.ViewProducto()

    @classmethod
    def lista_contenedor_principal(self):
        mv_instancia = my_view.ViewProducto()
        lista = [Text(value="1"), Text(value="2")]
        return lista

    # Coneccion con model
    @classmethod
    def obtener_productos(self):
        return my_model.get_producto()

    # Hace las comprobaciones antes de agregar un nuevo producto
    @classmethod
    def action_guardar_producto(self):
        v = my_view.ViewProducto()
        descripcion = v.tf_descripcion.value
        cantidad = v.tf_cantidad.value
        precio_compra = v.tf_precio_compra.value
        recargo = v.tf_recargo.value
        precio_venta = v.tf_precio_venta.value

        # Si los campos de texto no estan vacio
        if descripcion and cantidad and precio_compra and precio_venta:
            self.action_cancelar_producto()
            return my_model.add_producto(
                descripcion, cantidad, precio_compra, recargo, precio_venta
            )
        else:
            if not descripcion:
                v.tf_descripcion.error_text = "Ingrese una descripcion"
            if not cantidad:
                v.tf_cantidad.error_text = "Ingrese una cantidad"
            if not precio_compra:
                v.tf_precio_compra.error_text = "Ingrese un precio"
            if not precio_venta:
                v.tf_precio_venta.error_text = "Ingrese un precio"

    # Valida los campos y actuliza la informacion
    @classmethod
    def action_actualizar_producto(self, id):
        v = my_view.ViewProducto()
        descripcion = v.tf_descripcion.value
        cantidad = v.tf_cantidad.value
        precio_compra = v.tf_precio_compra.value
        recargo = v.tf_recargo.value
        precio_venta = v.tf_precio_venta.value

        # Si los campos de texto no estan vacio
        if descripcion and cantidad and precio_compra and precio_venta:
            self.action_cancelar_producto()
            return my_model.update_producto(
                descripcion,
                cantidad,
                precio_compra,
                recargo,
                precio_venta,
                id,
            )
        else:
            if not descripcion:
                v.tf_descripcion.error_text = "Ingrese una descripcion"
            if not cantidad:
                v.tf_cantidad.error_text = "Ingrese una cantidad"
            if not precio_compra:
                v.tf_precio_compra.error_text = "Ingrese un precio"
            if not precio_venta:
                v.tf_precio_venta.error_text = "Ingrese un precio"

    # Elimina el producto selecionado
    @classmethod
    def action_eliminar_producto(self, id):
        print(id)
        self.action_cancelar_producto()
        return my_model.delete_producto(id)

    # Limpia los TextField
    @classmethod
    def action_cancelar_producto(self):
        v = my_view.ViewProducto()
        v.tf_descripcion.value = None
        v.tf_cantidad.value = None
        v.tf_precio_compra.value = None
        v.tf_recargo.value = None
        v.tf_precio_venta.value = None

        v.tf_descripcion.error_text = None
        v.tf_cantidad.error_text = None
        v.tf_precio_compra.error_text = None
        v.tf_recargo.error_text = None
        v.tf_precio_venta.error_text = None

    # Realiza el incremento del precio de venta segun el recargo aplicado
    @classmethod
    def action_recargo_aplicado(self):
        try:
            incremento = self.action_validar_precio_compra() * (
                self.action_validar_recargo() / 100
            )
            precio_venta = self.action_validar_precio_compra() + int(incremento)

            return precio_venta
        except TypeError:
            return 0

    # Validan los Text Fiel para que solo se ingresen numeros
    @classmethod
    def action_validar_recargo(self):
        v = my_view.ViewProducto()
        try:
            recargo = int(v.tf_recargo.value)
            v.tf_recargo.error_text = None
            return recargo
        except ValueError:
            v.tf_recargo.error_text = "Ingrese solo números"
            v.tf_recargo.value = None

    @classmethod
    def action_validar_precio_compra(self):
        v = my_view.ViewProducto()
        try:
            precio_compra = int(v.tf_precio_compra.value)
            v.tf_precio_compra.error_text = None
            return precio_compra
        except ValueError:
            v.tf_precio_compra.error_text = "Ingrese solo números"
            v.tf_precio_compra.value = None

    @classmethod
    def action_validar_precio_venta(self):
        v = my_view.ViewProducto()
        v.tf_recargo.value = 0
        try:
            precio_venta = int(v.tf_precio_venta.value)
            v.tf_precio_venta.error_text = None
            return precio_venta
        except ValueError:
            v.tf_precio_venta.error_text = "Ingrese solo números"
            v.tf_precio_venta.value = None

    @classmethod
    def action_validar_cantidad(self):
        v = my_view.ViewProducto()
        try:
            cantidad = int(v.tf_cantidad.value)
            v.tf_cantidad.error_text = None
            return cantidad
        except ValueError:
            v.tf_cantidad.error_text = "Ingrese solo números"
            v.tf_cantidad.value = None

    # Aplica el recargo al precio de venta
    @classmethod
    def recargo_aplicado(self, recargo):
        v = my_view.ViewProducto()
        v.tf_precio_venta.value = recargo

    @classmethod
    def action_editar_producto(
        self, descripcion, cantidad, precio_compra, recargo, precio_venta
    ):
        v = my_view.ViewProducto()

        v.tf_descripcion.value = descripcion
        v.tf_cantidad.value = cantidad
        v.tf_precio_compra.value = precio_compra
        v.tf_recargo.value = recargo
        v.tf_precio_venta.value = precio_venta

    # Lista de productos para la busqueda
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
