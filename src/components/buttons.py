import flet as ft

def PrimaryButton(text, on_click=None, padding=None):
    return ft.ElevatedButton(
        content=ft.Text(text, weight=ft.FontWeight.BOLD),
        bgcolor="#EF3961",  # สีชมพูแดงตามดีไซน์ของนาย
        color="white",
        width=300,
        height=50,
        on_click=on_click,
        style=ft.ButtonStyle(padding=padding) if padding else None
    )