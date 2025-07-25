# main.py
import flet as ft

from modulo2.conn import Conn


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.DARK
    page.title = "TEST"

    page.add(
        ft.Row(
            controls=[Conn(page)],
            expand=True,
        )
    )

    page.update()


ft.app(target=main)
