from utils.api_client import ApiClient, api


class AuthService:
    def __init__(self, api: ApiClient):
        self.api = api

    def login(self, email: str, password: str):
        return self.api.post("/auth/login", data={"email": email, "password": password})
