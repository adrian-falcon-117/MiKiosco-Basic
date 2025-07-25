# views.view_home
import flet as ft


class HomeView(ft.Container):
    def __init__(self, page, conn):
        print("initialize home view")
        self.page = page
        self.conn = conn

    
    def btn_click(self, e):
        self.conn.text.value = "Button clicked!"
        self.page.update()

