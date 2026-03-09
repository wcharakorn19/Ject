# src/screens/forms/form2_detail.py
import flet as ft
from controllers.form_controller import FormController  # 🌟 ดึง Controller มาใช้งาน


def FormTwoDetailScreen(page: ft.Page, submission_id: str):
    controller = FormController()
    user_role = page.session.get("user_role")

    # --- 1. เตรียมตัวแปร UI (รอรับข้อมูล) ---
    student_name_val = ft.Text("Loading...", size=14, color="#333333")
    student_id_val = ft.Text("Loading...", size=14, color="#333333")
    degree_val = ft.Text("-", size=14, color="#333333")
    program_val = ft.Text("-", size=14, color="#333333")
    dept_val = ft.Text("-", size=14, color="#333333")

    main_advisor_val = ft.Text("Loading...", size=14, color="#333333")
    co_advisor_val = ft.Text("-", size=14, color="#333333")
    chair_val = ft.Text("-", size=14, color="#333333")
    committee_val = ft.Text("-", size=14, color="#333333")
    member5_val = ft.Text("-", size=14, color="#333333")
    reserve_ext_val = ft.Text("-", size=14, color="#333333")
    reserve_int_val = ft.Text("-", size=14, color="#333333")

    # --- 2. ฟังก์ชันโหลดข้อมูลที่คลีนสุดๆ ---
    def load_data():
        # โยนภาระไปให้ Controller ทำงาน
        result = controller.get_form2_detail(submission_id)

        if result["success"]:
            data = result["data"]
            # เอาข้อมูลที่ Controller จัดเรียงมาให้แล้ว หยอดลง UI เลย
            student_name_val.value = data["student_name"]
            student_id_val.value = data["student_id"]
            degree_val.value = data["degree"]
            program_val.value = data["program_name"]
            dept_val.value = data["department_name"]

            main_advisor_val.value = data["main_advisor"]
            co_advisor_val.value = data["co_advisor"]
            chair_val.value = data["chair"]
            committee_val.value = data["committee"]
            member5_val.value = data["member5"]
            reserve_ext_val.value = data["reserve_ext"]
            reserve_int_val.value = data["reserve_int"]
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

    committee_card = ft.Container(
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
                    "อาจารย์ที่ปรึกษาและคณะกรรมการสอบ",
                    size=16,
                    weight="bold",
                    color="black",
                ),
                ft.Divider(height=10, color="transparent"),
                create_row("อาจารย์ที่ปรึกษาหลัก:", main_advisor_val),
                create_row("อาจารย์ที่ปรึกษาร่วม:", co_advisor_val),
                ft.Divider(height=20, color="#EEEEEE"),
                ft.Text("ชื่อคณะกรรมการสอบ", size=15, weight="bold", color="black"),
                create_row("ประธานกรรมการสอบ:", chair_val),
                create_row("กรรมการ (ที่ปรึกษาร่วม 2):", committee_val),
                create_row("กรรมการสอบ (คนที่ 5):", member5_val),
                ft.Divider(height=20, color="#EEEEEE"),
                ft.Text("ชื่อคณะกรรมการสำรอง", size=15, weight="bold", color="black"),
                create_row("กรรมการสำรอง (ภายนอก):", reserve_ext_val),
                create_row("กรรมการสำรอง (ภายใน):", reserve_int_val),
            ],
        ),
    )

    load_data()

    return ft.View(
        route=f"/form2/{submission_id}",
        bgcolor="#FFF5F7",
        scroll=ft.ScrollMode.AUTO,
        appbar=ft.AppBar(
            leading=ft.IconButton(
                icon="arrow_back",
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
                            "แบบเสนอหัวข้อและเค้าโครงวิทยานิพนธ์",
                            size=18,
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    student_card,
                    ft.Container(padding=5),
                    committee_card,
                    ft.Container(padding=20),
                ]
            )
        ],
    )
