from flet import SnackBar, SnackBarBehavior, RoundedRectangleBorder, Text, Colors


class Mensaje:
    def __init__(self, page):
        self.page = page

    def mensaje(self, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Text(value=mensaje),
        )
        self.page.open(sbar)

    def mensaje_ok(self, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Text(value=mensaje),
            bgcolor=Colors.GREEN_500,
        )
        self.page.open(sbar)

    def mensaje_error(self, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Text(value=mensaje),
            bgcolor=Colors.RED_400,
        )
        self.page.open(sbar)
