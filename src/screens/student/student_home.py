# src/screens/student/student_home.py
import flet as ft
from controllers.student_controller import StudentController
from components.shared_navbar import SharedNavBar


def StudentHome(page: ft.Page):
    controller = StudentController()

    # 🌟 ดึงข้อมูลจาก Session มาเตรียมไว้ให้พร้อม
    user_name = page.session.get("user_full_name") or "นักศึกษา"
    user_id = page.session.get("user_id")

    # --- 1. เตรียมตัวแปร UI ---
    name_text = ft.Text(user_name, size=20, weight=ft.FontWeight.BOLD, color="black")
    doc_name_text = ft.Text(
        "Doc Name: Loading...", weight=ft.FontWeight.BOLD, color="black"
    )
    status_label_text = ft.Text("สถานะ :", color="black54")
    status_value_text = ft.Text(
        "Loading...", size=16, weight=ft.FontWeight.BOLD, color="black"
    )

    activities_list = ft.Column(spacing=15)

    # --- 2. ฟังก์ชันโหลดข้อมูล (จุดที่แก้ไข) ---
    def load_data():
        # 🌟 แก้ไข: ส่ง user_name เข้าไปเป็น argument ที่ 2 ตามที่ Controller ต้องการ
        result = controller.get_dashboard_data(user_id, user_name)

        if result["success"]:
            data = result["data"]

            # อัปเดตชื่อบนหน้าจอ (เผื่อมีการเปลี่ยนแปลง)
            name_text.value = data["user_name"]

            doc_name_text.value = f"Doc Name: {data['current_doc']['doc_name']}"
            status_label_text.value = data["current_doc"]["status_label"]
            status_value_text.value = data["current_doc"]["status_text"]

            activities_list.controls.clear()
            for act in data["activities"]:
                act_item = ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.FOLDER_OUTLINED, color="black54", size=20
                                ),
                                bgcolor="#F0F0F0",
                                padding=10,
                                border_radius=10,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        act["title"],
                                        size=14,
                                        color="black",
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    ft.Text(
                                        f"Status : {act['status']}",
                                        size=12,
                                        color="black54",
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ]
                    ),
                    bgcolor="#FAFAFA",
                    padding=15,
                    border_radius=10,
                    border=ft.border.all(1, "#E0E0E0"),
                )
                activities_list.controls.append(act_item)

            page.update()

    # --- 3. สร้าง UI Components ---
    status_card = ft.Container(
        content=ft.Column(
            [
                doc_name_text,
                ft.Container(height=10),
                status_label_text,
                status_value_text,
            ]
        ),
        bgcolor="white",
        padding=20,
        border_radius=15,
        width=float("inf"),
        shadow=ft.BoxShadow(blur_radius=15, color="black12", offset=ft.Offset(0, 5)),
    )

    activities_card = ft.Container(
        content=activities_list,
        bgcolor="white",
        padding=20,
        border_radius=15,
        width=float("inf"),
        shadow=ft.BoxShadow(blur_radius=15, color="black12", offset=ft.Offset(0, 5)),
    )

    # รันฟังก์ชันโหลดข้อมูล
    load_data()

    # --- 4. ประกอบร่าง Layout ---
    main_content = ft.Container(
        content=ft.Column(
            [
                ft.Text("Home", color="black26", size=16),
                name_text,
                ft.Container(height=10),
                status_card,
                ft.Container(height=20),
                ft.Text(
                    "Lastest Activities",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="black",
                ),
                activities_card,
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        padding=ft.padding.only(left=20, right=20, top=50),
        expand=True,
    )

    return ft.View(
        route="/student_home",
        bgcolor="#FFF6FE",
        padding=0,
        controls=[main_content],
        # 🌟 เรียกใช้ SharedNavBar แล้วบอกว่าเราอยู่หน้า "/student_home"
        bottom_appbar=SharedNavBar(page, current_route="/student_home"),
    )
