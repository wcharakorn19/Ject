import flet as ft

def AppTextField(label: str, is_password: bool = False):
    return ft.TextField(
        label=label,
        password=is_password,
        can_reveal_password=is_password,
        border_radius=10,
        bgcolor="white",
        color="black",
        height=50
    )