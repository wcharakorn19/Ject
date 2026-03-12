# src/main.py
import flet as ft
from core.config import APP_TITLE
from core.app_router import AppRouter

# Setup App
def main(page: ft.Page):
    page.title = APP_TITLE
    page.window.width = 402
    page.window.height = 874

    # Setup Navigation and Routing with AppRouter
    AppRouter(page)

    page.go("/")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
