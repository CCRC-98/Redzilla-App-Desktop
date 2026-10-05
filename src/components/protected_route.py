import flet as ft

from context.auth_context import AuthContext


@ft.component
def ProtectedRoute():
    auth = ft.use_context(AuthContext)
    outlet = ft.use_route_outlet()

    if not auth.is_authenticated:
        ft.context.page.navigate("/login")
        return ft.ProgressRing()

    return outlet
