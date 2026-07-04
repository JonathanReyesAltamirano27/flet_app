import flet as ft

from pages.authentication.login import Login
from pages.authentication.signup import SignUp
from utils.colors import (
    customPrimaryColor,
    customBgColor,
    customTextColor,
    customTextHeaderColor,
    customSidebarIconColor,
    custonDashboardBg,
    customBorderColor,
)

def views_handler(page):
    return {
        "/login": ft.View(route="/login", bgcolor=customPrimaryColor, padding=ft.Padding.all(0), controls=[Login(page)]),
        "/signup": ft.View(route="/signup", bgcolor=customBgColor, padding=ft.Padding.all(0), controls=[SignUp(page)]),
    }
