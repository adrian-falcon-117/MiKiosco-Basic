from flet import (
    Text,
    Container,
    DataRow,
    DataCell,
    Colors,
    Icons,
)


from model.model_productos import ModelProductos
from views.mensaje import Mensaje


class ControllerProductos(Container):

    def __init__(self, page, view):
        # super().__init__()
        self.page = page
        self.view = view
        self.model = ModelProductos(self.page)
        self.mensaje = Mensaje(self.page)

    id_productos = None

    datos = [None] * 6
    datos_dt = [None] * 6
    # id_producto = None
    # descripcion_producto = None
    # cantidad_producto = None
    # precio_compra_producto = None
    # recargo_producto = None
    # precio_venta_producto = None
    estado = True

    # Cuando se selecciona una fila de la tabla
    def on_descripcion_ordenar(self, e):
        # print(f"{e.column_index}, {e.ascending}"),

        if not e.ascending:
            self.view.dt_productos.rows = self.datos_tabla("ORDER BY descripcion ASC")
        else:
            self.view.dt_productos.rows = self.datos_tabla("")
        self.page.update()

    def on_fila_seleccionada(self, e):
        # self.cancelar()

        # Permite seleccionar solo una fila a la vez
        if e.control.selected:
            e.control.selected = False
            self.view.cont_botones_inferior.disabled = True
        else:
            for i in range(len(self.view.dt_productos.rows)):
                self.view.dt_productos.rows[i].selected = False
            e.control.selected = True
            self.view.cont_botones_inferior.disabled = False
            # Obtiene los datos de la fila seleccionada
            # print(e)
            self.datos_dt[0] = int(e.control.cells[0].content.value)
            self.datos_dt[1] = e.control.cells[1].content.value
            self.datos_dt[2] = int(e.control.cells[2].content.value)
            self.datos_dt[3] = int(e.control.cells[3].content.value)
            self.datos_dt[4] = int(e.control.cells[4].content.value)
            self.datos_dt[5] = int(e.control.cells[5].content.value)

            # print(self.datos)
        self.page.update()

    def datos_fila(self, color, i):
        dr = DataRow(
            color=color,
            on_select_changed=self.on_fila_seleccionada,
            data=i[0],
            cells=[
                DataCell(content=Text(value=i[0])),
                DataCell(content=Text(value=i[1])),
                DataCell(content=Text(value=i[2])),
                DataCell(content=Text(value=i[3])),
                DataCell(content=Text(value=i[4])),
                DataCell(content=Text(value=i[5])),
            ],
        )
        return dr

    def datos_tabla(self, txt):
        l_row = []
        for i in self.model.read(txt):
            if i[2] <= 5:
                l_row.append(self.datos_fila(Colors.RED_400, i))
            else:
                l_row.append(self.datos_fila(None, i))
        return l_row

    def comprobar_datos(self):
        # Si los campos de texto no estan vacio
        if (
            self.datos[1] != None
            and self.datos[2] != None
            and self.datos[3] != None
            and self.datos[4] != None
            and self.datos[5] != None
        ):
            return True
        else:
            self.mensaje.mensaje(Icons.ERROR_OUTLINE, "Falta informacion")
            return False

    # -----------------------------------------------------------------------------------------
    # Guarda o actualiza un producto
    def on_guardar_producto(self, e):
        # print(self.datos)
        if self.estado and self.comprobar_datos():  # Guarda un nuevo producto
            self.model.create(self.datos)
            self.cancelar()
            # Actuliza la tabla y muestra un mensaje de guardado
        elif not self.estado and self.comprobar_datos():  # Actualiza un nuevo producto
            self.model.update(self.datos)
            self.cancelar()

        self.view.dt_productos.rows = self.datos_tabla("")
        self.page.update()

    def on_editar_producto(self, e):
        # self.page.open(self.view.ad_editar_producto)
        # self.page.update()
        self.datos = self.datos_dt.copy()
        self.view.tf_descripcion.value = self.datos_dt[1]
        self.view.tf_cantidad.value = self.datos_dt[2]
        self.view.tf_precio_compra.value = self.datos_dt[3]
        self.view.tf_recargo.value = self.datos_dt[4]
        self.view.tf_precio_venta.value = self.datos_dt[5]
        self.estado = False
        self.view.cont_botones_inferior.disabled = True
        self.page.update()

    # Elimina el producto selecionado
    def on_si_eliminar(self, e):
        # Actualiza la tabla y muestra un mensaje de que se Elimino correctamente
        self.model.delete(self.datos_dt[0])
        self.page.close(self.view.ad_eliminar_producto)
        self.view.dt_productos.rows = self.datos_tabla("")
        self.view.cont_botones_inferior.disabled = True
        self.cancelar()

        self.page.update()

    def on_no_eliminar(self, e):
        self.page.close(self.view.ad_eliminar_producto)
        self.page.update()

    # Abrir o Cerrar Alert Dialog de ViewProducto para eliminar un producto de la lista
    def on_eliminar(self, e):
        if self.datos_dt[0] != self.datos[0]:
            self.page.open(self.view.ad_eliminar_producto)
        else:
            self.mensaje.mensaje(
                Icons.ERROR_OUTLINE, "No se puede eliminar en este momento"
            )
        self.page.update()

    # Cancela la operacion para guardar o editar un producto
    def on_cancelar(self, e):
        self.view.cont_producto.disabled = False
        self.cancelar()
        self.page.update()

    # Limpia los TextField y variables
    def cancelar(self):
        for i in range(0, 5):
            self.datos[i] = None

        self.estado = True

        self.view.tf_descripcion.value = None
        self.view.tf_cantidad.value = None
        self.view.tf_precio_compra.value = None
        self.view.tf_recargo.value = None
        self.view.tf_precio_venta.value = None

        self.view.tf_descripcion.error_text = None
        self.view.tf_cantidad.error_text = None
        self.view.tf_precio_compra.error_text = None
        self.view.tf_recargo.error_text = None
        self.view.tf_precio_venta.error_text = None

    # Se validan los Campos de texto----------------------------------------

    def recargo(self):
        try:
            self.datos[5] = (self.datos[3] * self.datos[4]) / 100 + self.datos[3]
            self.view.tf_precio_venta.value = int(self.datos[5])
        except TypeError:
            pass

    def on_descripcion(self, e):
        if e.control.value != "":
            self.datos[1] = e.control.value
        else:
            self.view.tf_descripcion.error_text = "Falta descripcion"
        self.page.update()

    def on_cantidad(self, e):
        self.view.tf_cantidad.error_text = None
        try:
            if e.control.value != "":
                self.datos[2] = int(e.control.value)
            else:
                self.view.tf_cantidad.error_text = "Falta cantidad"
        except ValueError:
            self.view.tf_cantidad.value = None
            self.view.tf_cantidad.error_text = "Solo números"
        self.page.update()

    def on_precio_compra(self, e):
        self.view.tf_precio_compra.error_text = None
        try:
            if e.control.value != "":
                self.datos[3] = int(e.control.value)
                self.recargo()
            else:
                self.view.tf_precio_compra.error_text = "Falta precio"
        except ValueError:
            self.view.tf_precio_compra.error_text = "Solo números"
            self.view.tf_precio_compra.value = None
        self.page.update()

    def on_recargo(self, e):
        self.view.tf_recargo.error_text = None
        try:
            if e.control.value != "":
                self.datos[4] = int(e.control.value)
                self.recargo()
            else:
                self.view.tf_recargo.error_text = "Falta recargo"
        except ValueError:
            self.view.tf_recargo.error_text = "Solo números"
            self.view.tf_recargo.value = None
        self.page.update()

    def on_precio_venta(self, e):
        self.view.tf_recargo.value = 0
        self.view.tf_precio_venta.value = e.control.value
        self.view.tf_precio_venta.error_text = None
        try:
            if e.control.value != "":
                self.datos[5] = int(e.control.value)
            else:
                self.view.tf_precio_venta.error_text = "Falta precio"

        except ValueError:
            self.view.tf_precio_venta.error_text = "Solo números"
            self.view.tf_precio_venta.value = None
        self.page.update()

    def formatear_numeroo(self, numero):
        try:
            numero_float = float(numero)
            return (
                "{:,.2f}".format(numero_float)
                .replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            )
        except ValueError:
            return numero

    # TODO Seguir aqui
    def formatear_numero(self, entrada):
        # Eliminar todo excepto dígitos y coma (solo una coma permitida)
        limpio = ""
        parte_decimal
        coma_encontrada = False
        for c in entrada:
            if c.isdigit() or c == ",":
                limpio += c

        # Separar parte entera y decimal
        if "," in entrada:
            parte_entera, parte_decimal = limpio.split(",", 1)
            print("Aqui:", parte_decimal)
        else:
            parte_entera, parte_decimal = limpio, ""

        print(limpio)

        # Formatear parte entera con puntos
        parte_entera = parte_entera[::-1]
        grupos = [parte_entera[i : i + 3] for i in range(0, len(parte_entera), 3)]
        parte_entera_formateada = ".".join(grupos)[::-1]

        # Reconstruir número
        resultado = parte_entera_formateada
        if parte_decimal:
            resultado += "," + parte_decimal

        return resultado
