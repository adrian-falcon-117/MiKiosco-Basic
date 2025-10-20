from flet import (
    Tabs,
    Tab,
    Page,
    Icons,
    TabAlignment,
    app,
    padding,
    Theme,
    AlertDialog,
    Text,
    ElevatedButton,
    OutlinedButton,
    Row,
    MainAxisAlignment,
    ColorScheme,
    DividerTheme,
    SnackBar,
    DataRow,
    DataCell,
    RoundedRectangleBorder,
    SnackBarBehavior,
    SegmentedButton,
    Segment,
    Icon,
    Column,
    Container,
    CrossAxisAlignment,
    Colors,
)
from views.view_login import ViewLogin
from views.view_caja import ViewCaja
from views.view_productos import ViewProducto
from views.view_combos import ViewCombos
from views.view_crear_combos import ViewCrearCombos
from views.view_ventas import ViewVentas
from views.view_cuenta_corriente import ViewCuentaCorriente
from views.view_movimiento_caja import ViewMovimientoCaja
from views.view_configuracion import ViewConfiguracion

from controllers.controller_caja import ControllerCaja
from controllers.controller_productos import ControllerProductos
from controllers.controller_configuracion import ControllerConfiguracion

# from controllers.controller_combos import ControllerCombo

from views.mensaje import Mensaje

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

    def on_cambiar(e):
        # print(e.data)
        # cont_combo.content = None
        if e.data == '["1"]':
            cont_combo.content = ViewCombos(page)
        else:
            cont_combo.content = ViewCrearCombos(page)
        page.update()

    # Dialogo cerrar aplicacon
    def on_abrir_dialog(e):
        if e.data == "close":
            page.open(ad_cerrar)

    def on_cerrar_dialog(e):
        page.close(ad_cerrar)

    # Mensaje en la parte inferior

    ##Funciones de ViewLogin----------------------------------------------------------------
    def on_usuario(e):
        ControllerConfiguracion.contrasena_usuario()

    # Para iniciar sesion
    def on_login_ok(e):
        contrasena = ViewLogin.tf_contrasena.value

        if contrasena == ControllerConfiguracion.contrasena_usuario():
            page.close(ViewLogin.ad_login)
            sms.mensaje(Icons.PERSON_OUTLINE, "Bienvenido")
        else:
            ViewLogin.tf_contrasena.error_text = "Contraseña incorrecta"
        page.update()

    ##Funciones de ViewCaja----------------------------------------------------------------------------------------
    def on_item_agregar_todo(e):
        page.open(ViewCaja.ad_cuenta_corriente)
        page.update()

    def on_cerrar_caja_corriente(e):
        page.close(ViewCaja.ad_cuenta_corriente)
        page.update()

    def on_producto_seleccionado(e):
        pass

    ##Funciones de ViewProductos-----------------------------------------------------------------------------------

    # Aplicaca el recargo al precio de venta

    ##Funciones de ViewCombos------------------------------------------------------------------------
    """
    def on_producto_seleccionado_combo(e):
        ControllerCombo.action_producto_seleccionado(e.selection.value)

    def on_cambiar_cantidad(e):
        ControllerCombo.action_cambiar_cantidad(e.control.value)
        page.update()
        
    def on_buscar_producto_combo(e):

        if e.data:
            ControllerCombo.action_buscar_producto(e.data)
            ViewCombos.sb_buscar_producto.open_view()
        else:
            ViewCombos.sb_buscar_producto.close_view()
            ControllerCombo.limpiar_variables()
            ControllerCombo.action_cambiar_cantidad(0)
        page.update()

    def get_all_productos_combo():
        l_row = []
        total = 0
        for i in ControllerCombo.action_obtener_combo():
            total += i[3]  # Suma el subtotal de la tabla
            l_row.append(
                DataRow(
                    # on_select_changed=on_seleccionar_fila_producto,
                    data=i[0],
                    cells=[
                        DataCell(content=Text(value=i[0])),
                        DataCell(content=Text(value=i[1])),
                        DataCell(content=Text(value=i[2])),
                        DataCell(content=Text(value=i[3])),
                    ],
                ),
            )
        ControllerCombo.total_combo(total)
        ControllerCombo.action_precio_combo(total)
        ViewCombos.dt_combos.rows = l_row
        # page.update()

    # Arreglar aca el botom de agregar al combo
    def on_agregar_producto_combo(e):
        get_all_productos_combo()
        on_cerrar_agregar_producto(e)
        page.update()

    def on_guardar_combo(e):
        pass

    def on_precio_combo(e):
        ControllerCombo.action_precio_combo(e.control.value)
        page.update()

    def on_descuento_combo(e):
        ControllerCombo.action_descuento_combo(e.control.value)w
        page.update()
    """

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
        global id_usuario, nombre_usuario, contrasena_usuario, estado_guardar_usuario
        ControllerConfiguracion.action_cancelar_usuario()
        estado_guardar_usuario = True
        id_usuario = None
        nombre_usuario = None
        contrasena_usuario = None

        # Permite seleccionar solo una fila a la vez
        if e.control.selected:
            e.control.selected = False
        else:
            for i in range(len(ViewConfiguracion.dt_usuarios.rows)):
                ViewConfiguracion.dt_usuarios.rows[i].selected = False
            e.control.selected = True

            # Obtiene los datos de la fila seleccionada
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
            if id_usuario:
                page.open(ViewConfiguracion.ad_eliminar_usuario)
            else:
                mensaje("Seleccione un usuario")

    # Cuando se preciona el boton editar
    def on_editar_usuario(e):
        global estado_guardar_usuario

        if id_usuario:
            ControllerConfiguracion.action_editar_usuario(
                nombre_usuario, contrasena_usuario, id_usuario
            )
            print(nombre_usuario, contrasena_usuario, id_usuario)
            estado_guardar_usuario = False
        else:
            mensaje("Seleccione un usuario")
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

    # Eventos de ViewCombos
    """
    ViewCombos.ebtn_crear_combo.on_click = on_crear_combo
    ViewCombos.ebtn_ver_combos.on_click = on_ver_combos
    ViewCombos.ebtn_agregar_producto.on_click = on_agregar_producto
    ViewCombos.ibtn_cerrar_seleccionar_productos.on_click = on_cerrar_agregar_producto
    # ViewCombos.ac_buscar_producto.on_select = on_producto_seleccionado_combo
    ViewCombos.tf_cantidad_producto.on_change = on_cambiar_cantidad
   # ViewCombos.sb_buscar_producto.on_change = on_buscar_producto_combo
    ViewCombos.ebtn_agregar.on_click = on_agregar_producto_combo
    ViewCombos.ebtn_guardar_combo = on_guardar_combo
    ViewCombos.tf_precio_combo.on_change = on_precio_combo
    ViewCombos.tf_descuento_combo.on_change = on_descuento_combo
    """

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
    sms = Mensaje(page)

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

    sb_combo = SegmentedButton(
        width=300,
        padding=2,
        selected_icon=Icon(Icons.CHECK),
        selected={"1"},
        allow_multiple_selection=False,
        on_change=on_cambiar,
        segments=[
            Segment(
                value="1",
                label=Text("Combos"),
                icon=Icon(Icons.DISCOUNT_OUTLINED),
            ),
            Segment(
                value="2",
                label=Text("Crear combo"),
                icon=Icon(Icons.ADD_CIRCLE_OUTLINE_OUTLINED),
            ),
        ],
    )

    cont_combo = Container(expand=True, content=ViewCombos(page))

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
                icon=Icons.LOCAL_OFFER_ROUNDED,
                text="Productos",
                content=ViewProducto(page),
            ),
            Tab(
                icon=Icons.DISCOUNT,
                text="Combos",
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        Container(
                            content=Row(
                                controls=[sb_combo],
                                alignment=MainAxisAlignment.CENTER,
                                # height=40,
                            ),
                            border_radius=5,
                            bgcolor=Colors.BLACK26,
                        ),
                        cont_combo,
                    ],
                ),
            ),
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
