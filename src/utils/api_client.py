from typing import Any

import requests


class ApiClient:
    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        timeout: int = 10,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def set_token(self, token: str | None) -> None:
        self.token = token

    def clear_token(self) -> None:
        self.token = None

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        data: Any = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        request_headers = {
            "Content-Type": "application/json",
        }

        if self.token:
            request_headers["Authorization"] = f"Bearer {self.token}"

        if headers:
            request_headers.update(headers)

        response = requests.request(
            method=method.upper(),
            url=url,
            json=data,
            params=params,
            headers=request_headers,
            timeout=self.timeout,
        )

        return response

    def get(
        self,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        return self.request(
            "GET",
            endpoint,
            params=params,
            headers=headers,
        )

    def post(
        self,
        endpoint: str,
        *,
        data: Any = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        return self.request(
            "POST",
            endpoint,
            data=data,
            headers=headers,
        )

    def put(
        self,
        endpoint: str,
        *,
        data: Any = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        return self.request(
            "PUT",
            endpoint,
            data=data,
            headers=headers,
        )

    def patch(
        self,
        endpoint: str,
        *,
        data: Any = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        return self.request(
            "PATCH",
            endpoint,
            data=data,
            headers=headers,
        )

    def delete(
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        return self.request(
            "DELETE",
            endpoint,
            headers=headers,
        )
