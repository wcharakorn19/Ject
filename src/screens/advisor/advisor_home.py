# src/screens/advisor/advisor_home.py
import flet as ft
from controllers.advisor_controller import AdvisorController
from components.shared_navbar import SharedNavBar
from components.base_card import BaseCard
from components.error_banner import ErrorBanner


def AdvisorHome(page: ft.Page):
    controller = AdvisorController()

    # 1. ดึงข้อมูลจาก Session
    user_id = page.session.get("user_id")
    if not user_id:
        page.go("/login")
        return ft.View(
            route="/advisor_home", controls=[ft.Text("Redirecting to login...")]
        )

    user_full_name = page.session.get("user_full_name") or "อาจารย์ที่ปรึกษา"
    print(f"DEBUG: โหลดหน้า Home -> user_id = {user_id}, name = {user_full_name}")

    # --- 2. เตรียม UI Components (State) ---
    name_text = ft.Text(
        user_full_name, size=24, weight=ft.FontWeight.BOLD, color="black"
    )
    student_list_column = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
    activities_list = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)
    student_count_text = ft.Text(
        "นักศึกษาในความดูแล (กำลังโหลด...)",
        size=16,
        weight=ft.FontWeight.BOLD,
        color="black",
    )
    error_container = ft.Column(spacing=0)

    # --- 3. โหลดข้อมูลและประกอบเข้า UI ก่อนสร้างหน้า View ---
    result = controller.get_dashboard_data(user_id)
    raw_data = result.get("data")
    error = result.get("message") if not result.get("success") else None

    if not error and raw_data:
        # 1. อัปเดตจำนวนนักศึกษา
        student_count_text.value = f"นักศึกษาในความดูแล ({raw_data.student_count} คน)"

        # 2. วาดรายชื่อนักศึกษา
        students_list = raw_data.students
        for student in students_list:
            student_list_column.controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color="#EF3961", size=35),
                            ft.Column(
                                [
                                    ft.Text(
                                        student.name,
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color="black",
                                    ),
                                    ft.Text(
                                        student.doc_status,
                                        size=12,
                                        color="black54",
                                    ),
                                ],
                                spacing=0,
                                expand=True,
                            ),
                        ]
                    ),
                    padding=ft.padding.only(bottom=10),
                    border=ft.border.only(bottom=ft.border.BorderSide(1, "#F0F0F0")),
                )
            )

        # 3. วาดกิจกรรมล่าสุด
        activities = raw_data.activities
        for act in activities:
            # 🌟 ส่วนที่อัปเกรด: ดึงประเภทฟอร์มและ ID เพื่อสร้าง Route อัจฉริยะ
            # ถ้า API ส่งมาเป็น form1 กับ SUB-001 มันจะได้ route เป็น /form1/SUB-001
            form_type = act.form_type
            sub_id = act.submission_id  # 12345 คือไอดีสมมติเผื่อ API ไม่มี
            target_route = f"/{form_type}/{sub_id}"

            activities_list.controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.FOLDER_OUTLINED, color="black54", size=24
                                ),
                                bgcolor="#F5F5F5",
                                padding=12,
                                border_radius=10,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        act.title,
                                        size=16,
                                        color="black",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        f"Name: {act.name}",
                                        size=14,
                                        color="black",
                                    ),
                                    ft.Text(
                                        f"Status: {act.status}",
                                        size=14,
                                        color="#EF3961",
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ]
                    ),
                    bgcolor="white",
                    padding=15,
                    border_radius=10,
                    border=ft.border.all(1, "#E5E5E5"),
                    # 🌟 ยิงคำสั่งไปที่เป้าหมายที่เราเพิ่งปั้นเสร็จเมื่อกี้!
                    on_click=lambda e, route=target_route: page.go(route),
                )
            )
    else:
        # กรณีเกิด Error ให้แสดงแบนเนอร์
        error_container.controls.append(
            ErrorBanner(f"เกิดข้อผิดพลาดในการโหลดข้อมูล: {error}")
        )

    # --- 4. ประกอบร่าง Layout ---
    students_card = BaseCard(
        content=ft.Column(
            [
                student_count_text,
                ft.Container(height=5),
                ft.Container(content=student_list_column, height=220),
            ]
        )
    )

    activities_card = BaseCard(
        content=activities_list,
        expand=True,
    )

    return ft.View(
        route="/advisor_home",
        bgcolor="#FFF6FE",
        padding=0,
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        name_text,
                        error_container,  # เพิ่มตำแหน่งแสดง Error ด้านบนสุด
                        students_card,
                        ft.Text(
                            "Tasks & Activities",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="black",
                        ),
                        activities_card,
                    ],
                    expand=True,
                ),
                padding=ft.padding.only(left=20, right=20, top=60),
                expand=True,
            )
        ],
        bottom_appbar=SharedNavBar(page, current_route="/advisor_home"),
    )
