import flet as ft
from pages.authentication.login import Login
from pages.authentication.signup import SignUp


def main(page: ft.Page):
    page.bgcolor = "white"
    page.padding = ft.Padding.all(0)

    def route_change(e=None):
        page.clean()
        if page.route == "/login":
            page.add(Login(page))
        elif page.route == "/signup":
            page.add(SignUp(page))
        page.update()

    page.fonts = {
        "abeezee": "fonts/ABeeZee-Regular"
    }

    page.on_route_change = route_change
    page.go("/login")
    route_change()


ft.app(target=main, assets_dir="assets")
