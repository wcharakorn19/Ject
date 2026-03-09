import flet as ft
from components.shared_navbar import SharedNavBar  # 🌟 1. Import ตัว Navbar อัจฉริยะเข้ามา


def ProfileScreen(page: ft.Page):
    # 🌟 ดึงข้อมูลจาก Session มาแสดงผล
    user_role = page.session.get("user_role")
    user_full_name = page.session.get("user_full_name") or "ผู้ใช้งาน"

    # (Logic การคำนวณ Route หายไปแล้ว เพราะ SharedNavBar จัดการให้หมด!)

    return ft.View(
        route="/profile",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Hello Profile", size=24, weight="bold"),
                        ft.Text(f"ชื่อ: {user_full_name}", size=16),
                        ft.Text(f"สถานะ: {user_role}", size=16, color="grey"),
                    ]
                ),
                padding=50,
            )
        ],
        # 🌟 2. เรียกใช้ SharedNavBar แล้วบอกมันว่าตอนนี้ฉันอยู่หน้า "/profile" นะ!
        bottom_appbar=SharedNavBar(page, current_route="/profile"),
    )
