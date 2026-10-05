import flet as ft

from context.auth_context import AuthContext


@ft.component
def LoginPage():
    auth = ft.use_context(AuthContext)

    email_ref = ft.use_ref(None)
    password_ref = ft.use_ref(None)

    def handle_login(e):
        email = email_ref.current.value
        password = password_ref.current.value

        auth.login(email, password)

        ft.context.page.navigate("/orders")

    return ft.Container(
        expand=True,
        padding=30,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            width=500,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=64,
                    height=64,
                    border_radius=16,
                    bgcolor=ft.Colors.RED_50,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(
                        ft.Icons.LOCK_OUTLINE,
                        size=30,
                        color=ft.Colors.RED_600,
                    ),
                ),
                ft.Container(height=20),
                ft.Text(
                    "Bienvenido",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_GREY_900,
                ),
                ft.Text(
                    "Inicia sesión para continuar",
                    size=15,
                    color=ft.Colors.BLUE_GREY_500,
                ),
                ft.Container(height=35),
                # Email
                ft.TextField(
                    ref=email_ref,
                    label="Correo electrónico",
                    hint_text="correo@ejemplo.com",
                    prefix_icon=ft.Icons.MAIL_OUTLINE,
                    keyboard_type=ft.KeyboardType.EMAIL,
                    border_radius=10,
                    border_color=ft.Colors.BLUE_GREY_200,
                    focused_border_color=ft.Colors.RED_500,
                    cursor_color=ft.Colors.RED_500,
                    text_size=14,
                    on_submit=handle_login,
                ),
                # Password
                ft.TextField(
                    ref=password_ref,
                    label="Contraseña",
                    hint_text="Ingresa tu contraseña",
                    prefix_icon=ft.Icons.LOCK_OUTLINE,
                    password=True,
                    can_reveal_password=True,
                    border_radius=10,
                    border_color=ft.Colors.BLUE_GREY_200,
                    focused_border_color=ft.Colors.RED_500,
                    cursor_color=ft.Colors.RED_500,
                    text_size=14,
                    on_submit=handle_login,
                ),
                ft.Container(height=25),
                # Botón
                ft.Button(
                    "Iniciar sesión",
                    width=float(300),
                    height=50,
                    on_click=handle_login,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.RED_600,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(
                            radius=10,
                        ),
                    ),
                ),
                ft.Container(height=25),
                ft.Divider(
                    color=ft.Colors.BLUE_GREY_100,
                ),
                ft.Text(
                    "© 2026 Agencia Redzilla. Todos los derechos reservados.",
                    size=11,
                    color=ft.Colors.BLUE_GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    )
