import flet as ft

from pages.authentication.login import Login
from pages.authentication.signup import SignUp
from utils.colors import (
    customPrimaryColor,
    customBgColor,
    customTextColor,
    customTextHeaderColor,
    customSidebarIconColor,
    customSideBarIconColor,
    customDashboardBG,
    customBorderColor,

)


def views_handler(page):
    return {
        "/login": ft.View(route="/login", bgcolor= customPrimaryColor,padding=ft.Padding.all(0), controls=[Login(page)],),
        "/signup": ft.View(route="/signup", bgcolor=customBgColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor=customTextColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor= customTextHeaderColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor=  customSidebarIconColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor= customSideBarIconColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor= customDashboardBG,padding=ft.Padding.all(0), controls=[SignUp(page)],),
        "/signup": ft.View(route="/signup", bgcolor= customBorderColor,padding=ft.Padding.all(0), controls=[SignUp(page)],),
    }
