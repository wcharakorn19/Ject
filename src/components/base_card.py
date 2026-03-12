# src/components/base_card.py
import flet as ft


class BaseCard(ft.Container):
    def __init__(self, content, **kwargs):
        # --- Default Styling ---
        kwargs.setdefault("bgcolor", "white")
        kwargs.setdefault("padding", 20)
        kwargs.setdefault("border_radius", 15)
        kwargs.setdefault("width", float("inf"))
        kwargs.setdefault(
            "shadow",
            ft.BoxShadow(blur_radius=15, color="black12", offset=ft.Offset(0, 5)),
        )

        super().__init__(**kwargs)
        self.content = content
