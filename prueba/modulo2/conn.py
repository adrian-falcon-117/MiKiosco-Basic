# routing.py
import flet as ft
from modulo.view_home import HomeView


class Conn(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.clickBtn = ft.ElevatedButton(
            text="Set session value and update page", on_click=HomeView(page, self).btn_click
        )
        self.text = ft.Text("Welcome to the Home View")
        self.content = ft.Column([self.text, self.clickBtn])
        
        
