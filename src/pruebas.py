"""
# Lista de productos con sus precios
productos = {"producto1": 100, "producto2": 150, "producto3": 200, "producto4": 250}

# Definición de combos (productos que forman un combo y el descuento asociado)
combos = {
    "combo1": {
        "productos": ["producto1", "producto2"],
        "descuento": 0.10,
    },  # 10% de descuento
    "combo2": {
        "productos": ["producto3", "producto4"],
        "descuento": 0.15,
    },  # 15% de descuento
}


# Función para calcular el total con descuento
def calcular_total_con_descuento(carrito):
    total = 0
    combos_aplicados = []

    # Calcular el total inicial suma todo el carrito
    for producto in carrito:
        total += productos.get(producto, 0)

    # print(combos.items())

    # Detectar y aplicar descuentos por combos
    for combo, detalles in combos.items():
        print(combo,"#")

        if all(item in carrito for item in detalles["productos"]):

            descuento = (
                sum(productos[item] for item in detalles["productos"])
                * detalles["descuento"]
            )
            total -= descuento

            combos_aplicados.append(combo)

            print(combo)

    return total, combos_aplicados


# Ejemplo de carrito de compras
carrito = ["producto1", "producto2", "producto1", "producto4"]

# Calcular el total con descuento
total, combos_aplicados = calcular_total_con_descuento(carrito)

# Mostrar resultados
print(f"Total con descuento: ${total:.2f}")
if combos_aplicados:
    print(f"Combos aplicados: {', '.join(combos_aplicados)}")
else:
    print("No se aplicaron combos.")

"""

""" import flet as ft


def main(page):

    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")
        page.update()

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")
        anchor.open_view()

    anchor = ft.SearchBar(
        # view_elevation=4,
        # divider_color=ft.Colors.AMBER,
        bar_hint_text="Busca un color",
        view_hint_text="Selecciona un color de las sugerencias",
        view_shape=ft.RoundedRectangleBorder(radius=5),
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(5)
        ],
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.OutlinedButton(
                    "Open Search View",
                    on_click=lambda _: anchor.open_view(),
                ),
            ],
        ),
        anchor,
    )


ft.app(main)
 """

import flet as ft
from model.model_combos import ModelCombos as my_model


def main(page):

    def action_buscar_producto(descripcion):
        # print(descripcion)
        lista = ft.ListView()
        for i in my_model.get_producto2(descripcion):
            print(i[1])
            lista.controls.append(ft.Text(value=i[1]))
        return lista

    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")
        print(f"handle_change e.data: {e.data}")

        lv.controls.clear()

        for i in my_model.get_producto2(e.data):
            lv.controls.append(
                ft.ListTile(title=ft.Text(value=i[1]), on_click=lambda e: print(i[1]))
            )
        # for i in range(6):
        #     lv.controls.append(action_buscar_producto(e.data))
        lv.update()

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")

    lv = ft.ListView()
    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Search colors...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            lv
            # ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            # for i in range(10)
        ],
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.OutlinedButton(
                    "Open Search View",
                    on_click=lambda _: anchor.open_view(),
                ),
            ],
        ),
        anchor,
    )


ft.app(target=main)
