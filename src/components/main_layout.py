import flet as ft

from context.auth_context import AuthContext


@ft.component
def MainLayout():
    auth = ft.use_context(AuthContext)
    outlet = ft.use_route_outlet()

    if auth is None:
        return ft.ProgressRing()

    return ft.Column(
        [
            # Header
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text("Router Demo", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Hi"),
                        ft.IconButton(
                            ft.Icons.LOGOUT,
                            on_click=lambda: (
                                auth.logout(),
                                ft.context.page.navigate("/login"),
                            ),
                        ),
                    ],
                ),
                padding=10,
                bgcolor=ft.Colors.SURFACE_BRIGHT,
            ),
            ft.Divider(height=1),
            # Content
            ft.Container(content=outlet, padding=20),
        ],
    )
