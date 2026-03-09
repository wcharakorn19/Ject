# src/screens/forms/form4_detail.py
import flet as ft
from controllers.form_controller import FormController


def FormFourDetailScreen(page: ft.Page, submission_id: str):
    controller = FormController()
    user_role = page.session.get("user_role")

    # --- 1. สร้างตัวแปร UI รอรับข้อมูล ---
    student_name_val = ft.Text("Loading...", size=14, color="#333333")
    student_id_val = ft.Text("Loading...", size=14, color="#333333")
    degree_val = ft.Text("-", size=14, color="#333333")
    program_val = ft.Text("-", size=14, color="#333333")
    dept_val = ft.Text("-", size=14, color="#333333")

    approve_date_val = ft.Text("-", size=14, color="#333333")
    title_th_val = ft.Text("-", size=14, color="#333333")
    title_en_val = ft.Text("-", size=14, color="#333333")

    expert_title_val = ft.Text("-", size=14, color="#333333")
    expert_name_val = ft.Text("-", size=14, color="#333333")
    expert_surname_val = ft.Text("-", size=14, color="#333333")
    expert_org_val = ft.Text("-", size=14, color="#333333")
    expert_phone_val = ft.Text("-", size=14, color="#333333")
    expert_email_val = ft.Text("-", size=14, color="#333333")

    # --- 2. ฟังก์ชันดึงข้อมูลจาก Controller ---
    def load_data():
        result = controller.get_form4_detail(submission_id)

        if result["success"]:
            data = result["data"]
            # หยอดข้อมูลลงช่อง UI
            student_name_val.value = data["student_name"]
            student_id_val.value = data["student_id"]
            degree_val.value = data["degree"]
            program_val.value = data["program_name"]
            dept_val.value = data["department_name"]

            approve_date_val.value = data["approve_date"]
            title_th_val.value = data["title_th"]
            title_en_val.value = data["title_en"]

            expert_title_val.value = data["expert_title"]
            expert_name_val.value = data["expert_name"]
            expert_surname_val.value = data["expert_surname"]
            expert_org_val.value = data["expert_org"]
            expert_phone_val.value = data["expert_phone"]
            expert_email_val.value = data["expert_email"]
        else:
            student_name_val.value = result["message"]
            student_name_val.color = "red"

        page.update()

    # --- 3. UI Helper ---
    def create_row(label, value_control):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=140, content=ft.Text(label, size=14, color="#888888")
                ),
                ft.Container(expand=True, content=value_control),
            ],
        )

    # --- 4. Layout ประกอบร่าง ---
    student_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("ข้อมูลนักศึกษา", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                create_row("ชื่อ-นามสกุล:", student_name_val),
                create_row("รหัสนักศึกษา:", student_id_val),
                create_row("ระดับปริญญา:", degree_val),
                create_row("หลักสูตรและสาขาวิชา:", program_val),
                create_row("ภาควิชา:", dept_val),
            ],
        ),
    )

    thesis_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text(
                    "ข้อมูลหัวข้อวิทยานิพนธ์ (ที่ได้อนุมัติ)", size=16, weight="bold", color="black"
                ),
                ft.Divider(height=10, color="transparent"),
                create_row("วันที่เสนอเค้าโครงได้รับอนุมัติ:", approve_date_val),
                create_row("ชื่อเรื่อง (TH):", title_th_val),
                create_row("ชื่อเรื่อง (ENG):", title_en_val),
            ],
        ),
    )

    expert_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("ข้อมูลผู้ทรงคุณวุฒิ คนที่ 1", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                create_row("คำนำหน้า/ ยศ(ตำแหน่ง):", expert_title_val),
                create_row("ชื่อ:", expert_name_val),
                create_row("นามสกุล:", expert_surname_val),
                create_row("สถาบัน/หน่วยงาน:", expert_org_val),
                create_row("เบอร์โทรศัพท์:", expert_phone_val),
                create_row("อีเมล:", expert_email_val),
            ],
        ),
    )

    load_data()

    return ft.View(
        route=f"/form4/{submission_id}",
        bgcolor="#FFF5F7",
        scroll=ft.ScrollMode.AUTO,
        appbar=ft.AppBar(
            # 🌟 ปุ่ม Back สับรางตาม Role
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="black",
                on_click=lambda _: page.go(
                    "/advisor_home" if user_role == "advisor" else "/student_home"
                ),
            ),
            title=ft.Text("KMITL", color="black", weight="bold"),
            center_title=True,
            bgcolor="#FFF5F7",
            elevation=0,
        ),
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=20, right=20, bottom=10, top=20),
                        content=ft.Text(
                            "แบบขอหนังสือเชิญเป็นผู้ทรงคุณวุฒิ\nตรวจและประเมิน...เพื่อวิจัย",
                            size=18,
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    student_card,
                    ft.Container(padding=5),
                    thesis_card,
                    ft.Container(padding=5),
                    expert_card,
                    ft.Container(padding=20),
                ]
            )
        ],
    )
