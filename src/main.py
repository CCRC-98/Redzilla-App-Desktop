import flet as ft

from router import router


def main(page: ft.Page):
    page.title = "Agencia Redzilla"

    page.window.alignment = ft.Alignment.CENTER

    page.window.width = 1000
    page.window.height = 600

    page.window.min_width = 1000
    page.window.min_height = 600

    page.window.resizable = True

    page.window.always_on_top = False

    page.render(router)


ft.run(main)
