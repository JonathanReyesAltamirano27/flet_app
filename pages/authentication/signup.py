import flet as ft

from components.fields import CustomTextField
from db import db_path
from db.crud import check_data_exists, connect_to_database, insert_data
from utils.colors import customTextHeaderColor, customBorderColor, customPrimaryColor
from utils.validation import Validation


class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        self._page = page
        self.validation = Validation()
        self.error_field = ft.Text("", color="red", size=0)

        self.first_name = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="First Name"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.surname = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Surname"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.email = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Email"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.confirm_password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Confirm Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(width=1, color=customBorderColor),
        )

        super().__init__(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=2,
                        padding=ft.Padding.all(40),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            controls=[
                                ft.Text(
                                    "Register",
                                    color=customTextHeaderColor,
                                    font_family="abeezee",
                                    size=28,
                                    weight=ft.FontWeight.NORMAL,
                                ),
                                ft.Divider(
                                    color=customBorderColor,
                                    height=0.5,
                                    thickness=1.5,
                                ),
                                self.error_field,
                                self.first_name,
                                self.surname,
                                self.email,
                                self.password,
                                self.confirm_password,
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    height=40,
                                    bgcolor=customPrimaryColor,
                                    content=ft.Text("Register", color="white"),
                                    on_click=self.validate_registration,
                                ),
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    height=40,
                                    content=ft.Text(
                                        "Already have an account? Login",
                                        color=customTextHeaderColor,
                                    ),
                                    on_click=lambda e: page.go("/login"),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        expand=2,
                        image=ft.DecorationImage(
                            src="images/bg.png",
                            fit=ft.BoxFit.COVER,
                        ),
                        padding=ft.Padding.all(40),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.LOCK_PERSON_ROUNDED,
                                    size=200,
                                    color="white",
                                ),
                                ft.Text(
                                    "Signup section",
                                    color="white",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def show_message(self, message: str, color: str = "red"):
        self.error_field.value = message
        self.error_field.color = color
        self.error_field.size = 12
        self.error_field.update()

    def clear_message(self):
        self.error_field.value = ""
        self.error_field.size = 0
        self.error_field.update()

    def validate_registration(self, e):
        self.clear_message()

        first_name_value = self.first_name.content.value.strip()
        surname_value = self.surname.content.value.strip()
        email_value = self.email.content.value.strip()
        password_value = self.password.content.value
        confirm_password_value = self.confirm_password.content.value

        if not (first_name_value and surname_value and email_value and password_value and confirm_password_value):
            self.show_message("All fields are needed")
            return

        if not self.validation.is_valid_email(email_value):
            self.show_message("Enter a valid email")
            return

        if password_value != confirm_password_value:
            self.show_message("Passwords do not match")
            return

        conn = connect_to_database(db_path)
        try:
            if check_data_exists(conn, "user", f"email='{email_value}'"):
                self.show_message("Email already registered")
                return

            insert_data(
                conn,
                "user",
                (first_name_value, surname_value, email_value, password_value),
            )
        finally:
            conn.close()

        self.show_message("You have successfully registered", color="green")
        self._page.go("/login")
