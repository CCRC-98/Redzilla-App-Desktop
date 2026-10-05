import flet as ft

from components.main_layout import MainLayout
from components.protected_route import ProtectedRoute
from context.auth_context import AuthContext, AuthState
from pages.login_page import LoginPage
from pages.orders_page import OrdersPage


@ft.component
def router():
    auth, _ = ft.use_state(AuthState)

    return ft.SafeArea(
        content=AuthContext(
            auth,
            lambda: ft.Router(
                [
                    ft.Route(path="login", component=LoginPage),
                    ft.Route(
                        component=ProtectedRoute,
                        children=[
                            ft.Route(
                                component=MainLayout,
                                children=[ft.Route(path="orders", component=OrdersPage)],
                            ),
                        ],
                    ),
                ]
            ),
        )
    )
