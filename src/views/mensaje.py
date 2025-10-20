from flet import (
    SnackBar,
    SnackBarBehavior,
    RoundedRectangleBorder,
    Text,
    Colors,
    Icons,
    Icon,
    Row,
    Container,
)


class Mensaje(Container):
    def __init__(self, page):
        self.page = page

    def mensaje(self, icon, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            # width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Row(
                controls=[
                    Icon(name=icon, color=Colors.BLACK),
                    Text(value=mensaje),
                ]
            ),
            # content=Text(value=mensaje),
        )
        self.page.open(sbar)

    def mensaje_ok(self, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            # width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Row(
                controls=[
                    Icon(name=Icons.CHECK, color=Colors.BLACK),
                    Text(value=mensaje),
                ]
            ),
            bgcolor=Colors.GREEN_500,
        )
        self.page.open(sbar)

    def mensaje_error(self, mensaje):
        sbar = SnackBar(
            behavior=SnackBarBehavior.FLOATING,
            # width=300,
            shape=RoundedRectangleBorder(radius=5),
            show_close_icon=True,
            content=Row(
                controls=[
                    Icon(name=Icons.CANCEL_OUTLINED, color=Colors.BLACK),
                    Text(value=mensaje),
                ]
            ),
            bgcolor=Colors.RED_400,
        )
        self.page.open(sbar)
