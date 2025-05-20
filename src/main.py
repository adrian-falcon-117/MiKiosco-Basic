from flet import (
    Tabs,
    Tab,
    Page,
    Icons,
    TabAlignment,
    AppView,
    app,
    padding,
    Theme,
    Colors,
    AlertDialog,
    Text,
    TextField,
    Dropdown,
    ElevatedButton,
    OutlinedButton,
    Divider,
    CircleAvatar,
    Icon,
    icons,
    Column,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
    ColorScheme,
    DividerTheme,
    ScrollbarTheme,
    IconTheme,
    ElevatedButtonTheme,
    OutlinedButtonTheme,
    SnackBar,
    DataRow,
    DataCell,
    RoundedRectangleBorder,
    SnackBarBehavior,
)
from views.view_login import ViewLogin
from views.view_caja import ViewCaja
from views.view_productos import ViewProducto
from views.view_combos import ViewCombos
from views.view_ventas import ViewVentas
from views.view_cuenta_corriente import ViewCuentaCorriente
from views.view_movimiento_caja import ViewMovimientoCaja
from views.view_configuracion import ViewConfiguracion

from controllers.controller_caja import ControllerCaja
from controllers.controller_productos import ControllerProductos
from controllers.controller_configuracion import ControllerConfiguracion

# import os
# import winreg
# id_usuario = None

id_usuario = None
nombre_usuario = None
contrasena_usuario = None
estado_guardar_usuario = True

id_producto = None
descripcion_producto = None
cantidad_producto = None
precio_compra_producto = None
recargo_producto = None
precio_venta_producto = None
estado_guardar_producto = True


def main(page: Page):
    page.window.min_height = 600
    page.window.min_width = 1024
    page.window.prevent_close = True

    # Variables goblales del Usuario

    # ViewConfiguracion.rg_temas.value = "claro"
    # page.theme_mode = "light"

    # page.theme = Theme(color_scheme_seed=Colors.ORANGE)
    """page.theme = Theme(
        # use_material3=False,
        color_scheme=ColorScheme(
            primary="orange900",
            outline=Colors.ORANGE_900,
            secondary=Colors.ORANGE_900,
            tertiary=Colors.ORANGE_900,
            background=Colors.ORANGE_50,
        ),
        # primary_color=Colors.ORANGE,
        # hover_color=Colors.ORANGE_200,
        divider_theme=DividerTheme(color="orange900"),
        # icon_theme=IconTheme(color=Colors.ORANGE),
        # elevated_button_theme=ElevatedButtonTheme(bgcolor=Colors.ORANGE),
        # outlined_button_theme=OutlinedButtonTheme(foreground_color=Colors.ORANGE),
    )"""

    ##Funciones de Main---------------------------------------------------------------
    # Aplica un tema
    def tema():
        page.theme_mode = ControllerConfiguracion.tema_seleccionado()
        page.update()

    # Aplica un color a la interfaz
    def color():
        color = ControllerConfiguracion.color_seleccionado()
        page.theme = Theme(
            color_scheme=ColorScheme(
                primary=color,
                outline=color,
                secondary=color,
                tertiary=color,
                background=color,
            ),
            divider_theme=DividerTheme(color=color),
        )
        page.update()

    def cerrar_aplicacion(e):
        page.window.destroy()

    # Dialogo cerrar aplicacon
    def on_abrir_dialog(e):
        if e.data == "close":
            page.open(ad_cerrar)

    def on_cerrar_dialog(e):
        page.close(ad_cerrar)

    # Mensaje en la parte inferior
    def mensaje(mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Text(value=mensaje),
        )
        page.open(sbar)

    ##Funciones de ViewLogin
    def on_usuario(e):
        ControllerConfiguracion.contrasena_usuario()

    # Para iniciar sesion
    def on_login_ok(e):
        contrasena = ViewLogin.tf_contrasena.value

        if contrasena == ControllerConfiguracion.contrasena_usuario():
            page.close(ViewLogin.ad_login)
            mensaje("Bienvenido")
        else:
            ViewLogin.tf_contrasena.error_text = "Contraseña incorrecta"
        page.update()

    ##Funciones de ViewCaja
    def on_item_agregar_todo(e):
        page.open(ViewCaja.ad_cuenta_corriente)
        page.update()

    def on_cerrar_caja_corriente(e):
        page.close(ViewCaja.ad_cuenta_corriente)
        page.update()

    def on_producto_seleccionado(e):
        # print(e.control.selected_index)
        print(e.selection.value)

    ##Funciones de ViewProductos-----------------------------------------------------------------------------------
    def on_seleccionar_fila_producto(e):

        # Permite seleccionar solo una fila a la vez
        for i in range(len(ViewProducto.dt_productos.rows)):
            ViewProducto.dt_productos.rows[i].__setattr__("selected", False)
            print(e, i)
        e.control.__setattr__("selected", True)

        # Obtiene el id de la columna seleccionada
        global id_producto, descripcion_producto, cantidad_producto, precio_compra_producto, recargo_producto, precio_venta_producto
        id_producto = int(e.control.cells[0].content.value)
        descripcion_producto = e.control.cells[1].content.value
        cantidad_producto = int(e.control.cells[2].content.value)
        precio_compra_producto = int(e.control.cells[3].content.value)
        recargo_producto = int(e.control.cells[4].content.value)
        precio_venta_producto = int(e.control.cells[5].content.value)
        page.update()

    def get_all_productos():
        l_row = []
        for i in ControllerProductos.obtener_productos():
            l_row.append(
                DataRow(
                    on_select_changed=on_seleccionar_fila_producto,
                    data=i[0],
                    cells=[
                        DataCell(content=Text(value=i[0])),
                        DataCell(content=Text(value=i[1])),
                        DataCell(content=Text(value=i[2])),
                        DataCell(content=Text(value=i[3])),
                        DataCell(content=Text(value=i[4])),
                        DataCell(content=Text(value=i[5])),
                    ],
                ),
            )
        return l_row

    # Guarda o actualiza un producto
    def on_guardar_producto(e):
        global estado_guardar_producto, id_producto

        if estado_guardar_producto:  # Guarda un nuevo producto
            if ControllerProductos.action_guardar_producto():
                # Actuliza la tabla y muestra un mensaje de guardado
                ViewProducto.dt_productos.rows = get_all_productos()
                mensaje("Guardado")
            else:
                mensaje("No se pudo guardar")

        else:  # Actualiza un nuevo producto
            if ControllerProductos.action_actualizar_producto(id_producto):
                ViewProducto.dt_productos.rows = get_all_productos()
                mensaje("Actualizado")
                estado_guardar_producto = True
                id_producto = None
                ControllerProductos.action_cancelar_producto()
            else:
                mensaje("No se pudo Actualizar")
        page.update()

    def on_editar_producto(e):
        global estado_guardar_producto, id_producto
        if id_producto:
            ControllerProductos.action_editar_producto(
                descripcion_producto,
                cantidad_producto,
                precio_compra_producto,
                recargo_producto,
                precio_venta_producto,
            )
            estado_guardar_producto = False
        else:
            mensaje("Seleccione un producto")
        page.update()

        # Aplicaca el recargo al precio de venta

    def on_aplicar_recargo(e):
        ControllerProductos.action_validar_recargo()
        ControllerProductos.recargo_aplicado(
            ControllerProductos.action_recargo_aplicado()
        )
        page.update()

    def on_validar_precio_compra(e):
        ControllerProductos.action_validar_precio_compra()
        ControllerProductos.recargo_aplicado(
            ControllerProductos.action_recargo_aplicado()
        )
        page.update()

    def on_validar_cantidad(e):
        ControllerProductos.action_validar_cantidad()
        page.update()

    def on_validar_precio_venta(e):
        ControllerProductos.action_validar_precio_venta()
        page.update()

    def on_ver_promociones(e):
        global id_producto
        ViewProducto.cont_productos.visible = False
        ViewProducto.cont_combos.visible = True
        ControllerProductos.action_cancelar_producto()
        ViewProducto.dt_combos.rows = get_all_productos()
        id_producto = None
        page.update()

    def on_ver_productos(e):
        global id_producto
        ViewProducto.cont_productos.visible = True
        ViewProducto.cont_combos.visible = False
        id_producto = None
        page.update()

    def on_cerrar_promocion(e):
        page.close(ViewProducto.ad_crear_promocion)
        page.update()

    # Abrir o Cerrar Alert Dialog de ViewProducto para eliminar un producto de la lista
    def on_eliminar(e):
        global id_producto
        if id_producto:
            page.open(ViewProducto.ad_eliminar_producto)
            page.update()
        else:
            mensaje("Seleccione un producto")

    def on_si_eliminar(e):
        global estado_guardar_producto, id_producto
        if ControllerProductos.action_eliminar_producto(id_producto):
            # Actualiza la tabla y muestra un mensaje de que se Elimino correctamente
            page.close(ViewProducto.ad_eliminar_producto)
            ViewProducto.dt_productos.rows = get_all_productos()
            mensaje("Eliminado correctamente")
            estado_guardar_producto = True
            id_producto = None
        else:
            page.close(ViewProducto.ad_eliminar_producto)
            mensaje("No se pudo eliminar")

        page.update()

    def on_no_eliminar(e):
        page.close(ViewProducto.ad_eliminar_producto)
        page.update()

    def on_cancelar_producto(e):
        global id_producto, estado_guardar_producto
        id_producto = None
        estado_guardar_producto = True
        ControllerProductos.action_cancelar_producto()
        page.update()

    ##Funciones de ViewCombos------------------------------------------------------------------------
    def on_crear_combo(e):
        ViewCombos.cont_crear_combos.visible = True
        ViewCombos.cont_combos.visible = False
        page.update()

    def on_ver_combos(e):
        ViewCombos.cont_crear_combos.visible = False
        ViewCombos.cont_combos.visible = True
        page.update()

    ##Funciones de ViewCuentaCorriente----------------------------------------------------------------
    def on_ver_estado_cuenta(e):
        print(e)
        page.open(ViewCuentaCorriente.ad_estado_cuenta)
        page.update()

    def on_cerrar_estado_cuenta(e):
        page.close(ViewCuentaCorriente.ad_estado_cuenta)
        page.update()

    ##Funciones de ViewMovimientosCaja--------------------------------------------------------------------
    # Dialog Apertura de caja
    def on_apertura_caja(e):
        page.open(ViewMovimientoCaja.ad_apertura_caja)
        page.update()

    def on_cerrar_apertura_caja(e):
        page.close(ViewMovimientoCaja.ad_apertura_caja)
        page.update()

    # Dialog Movimientos de caja
    def on_movimiento_caja(e):
        page.open(ViewMovimientoCaja.ad_movimiento_caja)
        page.update()

    def on_cerrar_movimiento_caja(e):
        page.close(ViewMovimientoCaja.ad_movimiento_caja)
        page.update()

    # Dialog Cierre de caja
    def on_cierre_caja(e):
        page.open(ViewMovimientoCaja.ad_cierre_caja)
        page.update()

    def on_cerrar_cierre_caja(e):
        page.close(ViewMovimientoCaja.ad_cierre_caja)
        page.update()

    ##Funciones de Configuracion----------------------------------------------------------
    def cambiar_tema(e):
        print(e.control.value)
        if e.control.value == "light":
            ControllerConfiguracion.seleccionar_tema("light")
        else:
            ControllerConfiguracion.seleccionar_tema("darck")
        tema()

    def cambiar_color(e):
        ControllerConfiguracion.seleccionar_color(e.control.value)
        color()
        print(ControllerConfiguracion.color_seleccionado())
        page.update()

    # Cuando se selecciona una fila
    def on_seleccionar_fila_usuario(e):

        # Permite seleccionar solo una fila a la vez
        for i in range(len(ViewConfiguracion.dt_usuarios.rows)):
            ViewConfiguracion.dt_usuarios.rows[i].__setattr__("selected", False)
        e.control.__setattr__("selected", True)

        # Obtiene el id de la columna seleccionada
        global id_usuario, nombre_usuario, contrasena_usuario
        id_usuario = int(e.control.cells[0].content.value)
        nombre_usuario = e.control.cells[1].content.value
        contrasena_usuario = e.control.cells[2].content.value
        page.update()

    # Carga todos los usuarios a la tabla
    def get_all_usuarios():
        l_row = []
        for i in ControllerConfiguracion.obtener_usuario():
            l_row.append(
                DataRow(
                    on_select_changed=on_seleccionar_fila_usuario,
                    data=i[0],
                    cells=[
                        DataCell(visible=False, content=Text(value=i[0])),
                        DataCell(content=Text(value=i[1])),
                        DataCell(content=Text(value=i[2])),
                    ],
                ),
            )
        return l_row

    # Cuando se agrega un usuario
    def on_guardar_usuario(e):
        global estado_guardar_usuario

        if estado_guardar_usuario:  # Guarda un nuevo usuario
            if ControllerConfiguracion.action_guardar_usuario():
                # Actuliza la tabla y muestra un mensaje de guardado
                ViewConfiguracion.dt_usuarios.rows = get_all_usuarios()
                mensaje("Guardado")
            else:
                mensaje("No se pudo guardar")

        else:  # Actualiza un nuevo usuario
            if ControllerConfiguracion.action_actualizar_usuario():
                ViewConfiguracion.dt_usuarios.rows = get_all_usuarios()
                mensaje("Actualizado")
                estado_guardar_usuario = True
                ControllerConfiguracion.action_cancelar_usuario()
            else:
                mensaje("No se pudo Actualizar")
        page.update()

    def on_si_eliminar_usuario(e):
        global estado_guardar_usuario, id_usuario
        if ControllerConfiguracion.action_eliminar_usuario(id_usuario):
            # Actualiza la tabla y muestra un mensaje de que se Elimino correctamente
            page.close(ViewConfiguracion.ad_eliminar_usuario)
            ViewConfiguracion.dt_usuarios.rows = get_all_usuarios()
            mensaje("Eliminado correctamente")
            estado_guardar_usuario = True
            id_usuario = None
        else:
            page.close(ViewConfiguracion.ad_eliminar_usuario)
            mensaje("No se pudo eliminar")

        page.update()

    def on_no_eliminar_usuario(e):
        page.close(ViewConfiguracion.ad_eliminar_usuario)
        page.update()

    # Abre el Dialog para elimanar la seleccion
    def on_eliminar_usuario(e):
        if id_usuario == 1:
            mensaje("Usuario Administrador no se puede eliminar")
        else:
            page.open(ViewConfiguracion.ad_eliminar_usuario)

    # Cuando se preciona el boton editar
    def on_editar_usuario(e):
        global estado_guardar_usuario
        ControllerConfiguracion.action_editar_usuario(
            nombre_usuario, contrasena_usuario, id_usuario
        )
        print(nombre_usuario, contrasena_usuario, id_usuario)
        estado_guardar_usuario = False
        page.update()

    # Limpia los campos de Nombre y Contraseña
    def on_cancelar_usuario(e):
        ControllerConfiguracion.action_cancelar_usuario()
        page.update()

    # Eventos de ViewLogin
    # key_usuario = ViewLogin.dd_usuario.value

    ViewLogin.dd_usuario.on_change = on_usuario

    # Eventos de ViewPaginaPrincipal
    ViewCaja.item_agregar_todo.on_click = on_item_agregar_todo
    ViewCaja.ibtn_cerrar_cuenta_corriente.on_click = on_cerrar_caja_corriente
    ViewCaja.ac_buscar_producto.on_select = on_producto_seleccionado

    # Eventos de ViewProducto
    # ViewProducto.ebtn_ver_combos.on_click = on_ver_promociones
    # ViewProducto.ebtn_ver_productos.on_click = on_ver_productos
    # ViewProducto.ibtn_cerrar_combo.on_click = on_cerrar_promocion
    ViewProducto.obtn_eliminar.on_click = on_eliminar
    ViewProducto.obtn_no.on_click = on_no_eliminar
    ViewProducto.ebtn_si.on_click = on_si_eliminar
    ViewProducto.dt_productos.rows = get_all_productos()
    # ViewProducto.dt_combos.rows = get_all_productos()
    ViewProducto.ebtn_guardar_producto.on_click = on_guardar_producto
    ViewProducto.ebtn_editar.on_click = on_editar_producto
    ViewProducto.tf_recargo.on_change = on_aplicar_recargo
    ViewProducto.tf_precio_compra.on_change = on_validar_precio_compra
    ViewProducto.tf_precio_venta.on_change = on_validar_precio_venta
    ViewProducto.tf_cantidad.on_change = on_validar_cantidad
    ViewProducto.ibtn_cancelar_producto.on_click = on_cancelar_producto

    # Eventos de ViewCombos
    ViewCombos.ebtn_crear_combo.on_click = on_crear_combo
    ViewCombos.ebtn_ver_combos.on_click = on_ver_combos

    # Eventos de ViewCuentaCorriente
    ViewCuentaCorriente.ebtn_ver_estado_cuenta.on_click = on_ver_estado_cuenta
    ViewCuentaCorriente.ibtn_cerrar_estado_cuenta.on_click = on_cerrar_estado_cuenta

    # Eventos de ViewMovimientosCaja
    ViewMovimientoCaja.item_apertura_caja.on_click = on_apertura_caja
    ViewMovimientoCaja.ibtn_cerrar_apertura_caja.on_click = on_cerrar_apertura_caja
    ViewMovimientoCaja.item_generar_movimiento.on_click = on_movimiento_caja
    ViewMovimientoCaja.ibtn_cerrar_movimiento_caja.on_click = on_cerrar_movimiento_caja
    ViewMovimientoCaja.item_cierre_caja.on_click = on_cierre_caja
    ViewMovimientoCaja.ibtn_cerrar_cierre_caja.on_click = on_cerrar_cierre_caja

    # Eventos de ViewConfiguracion
    ViewConfiguracion.rg_temas.on_change = cambiar_tema
    ViewConfiguracion.rg_colores.on_change = cambiar_color
    ViewConfiguracion.ebtn_guardar_usuario.on_click = on_guardar_usuario
    ViewConfiguracion.dt_usuarios.rows = get_all_usuarios()
    ViewConfiguracion.obtn_eliminar_usuario.on_click = on_eliminar_usuario
    ViewConfiguracion.ebtn_si_eliminar_usuario.on_click = on_si_eliminar_usuario
    ViewConfiguracion.obtn_no_eliminar_usuario.on_click = on_no_eliminar_usuario
    ViewConfiguracion.ebtn_editar_usuario.on_click = on_editar_usuario
    ViewConfiguracion.ibtn_cancelar_usuario.on_click = on_cancelar_usuario

    # Eventos de ViewLogin
    ViewLogin.ebtn_iniciar.on_click = on_login_ok
    ViewLogin.obtn_salir.on_click = cerrar_aplicacion

    # Controles de Main
    ebtn_si_cerrar = ElevatedButton(text="Si", on_click=cerrar_aplicacion)
    obtn_no_cerrar = OutlinedButton(text="No", on_click=on_cerrar_dialog)
    ad_cerrar = AlertDialog(
        modal=True,
        title=Text(value="Cerrar aplicacion?"),
        content=Row(
            alignment=MainAxisAlignment.CENTER,
            expand=True,
            controls=[ebtn_si_cerrar, obtn_no_cerrar],
        ),
    )
    tabs = Tabs(
        padding=padding.only(left=10, top=0, right=10, bottom=0),
        tab_alignment=TabAlignment.CENTER,
        expand=True,
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(icon=Icons.HOME, text="Inicio", content=ViewCaja()),
            Tab(
                icon=Icons.ALL_INBOX_ROUNDED,
                text="Movimiento de Caja",
                content=ViewMovimientoCaja(),
            ),
            Tab(
                icon=Icons.LOCAL_OFFER_ROUNDED, text="Productos", content=ViewProducto()
            ),
            Tab(icon=Icons.DISCOUNT, text="Combos", content=ViewCombos()),
            Tab(icon=Icons.ATTACH_MONEY_OUTLINED, text="Ventas", content=ViewVentas()),
            Tab(
                icon=Icons.ACCOUNT_BALANCE_ROUNDED,
                text="Cuenta corriente",
                content=ViewCuentaCorriente(),
            ),
            Tab(
                icon=Icons.SETTINGS,
                text="Configuración",
                content=ViewConfiguracion(),
            ),
        ],
    )

    tema()
    color()
    page.add(tabs)
    page.open(ViewLogin.ad_login)
    page.window.on_event = on_abrir_dialog


app(target=main)
# view=ft.AppView.WEB_BROWSER


# Para obtener el tema del sistema operativo windows
"""
def obtener_tema_sistema_operativo():
        if os.name == "nt":  # Windows
            try:
                clave = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
                )
                valor = winreg.QueryValueEx(clave, "AppsUseLightTheme")
                return "Claro" if valor == 1 else "Oscuro"
            except FileNotFoundError:
                return "No se pudo determinar el tema
"""
