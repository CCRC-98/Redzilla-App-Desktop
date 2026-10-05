from dataclasses import dataclass

import flet as ft


@ft.observable
@dataclass
class AuthState:
    is_authenticated: bool = False
    email: str = ""
    password: str = ""

    def login(self, email, password):
        self.email = email
        self.password = password
        self.is_authenticated = True

    def logout(self):
        self.email = ""
        self.password = ""
        self.is_authenticated = False


AuthContext: ft.ContextProvider[AuthState | None] = ft.create_context(None)
