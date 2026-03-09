import flet as ft
from controllers.form_controller import FormController  # 🌟 ดึง Controller มาใช้


def FormOneDetailScreen(page: ft.Page, submission_id: str):
    controller = FormController()
    user_role = page.session.get("user_role")

    # UI Components (รอรับข้อมูล)
    student_name_val = ft.Text("Loading...", size=14, color="#333333")
    student_id_val = ft.Text("Loading...", size=14, color="#333333")
    degree_val = ft.Text("-", size=14, color="#333333")
    program_val = ft.Text("-", size=14, color="#333333")
    dept_val = ft.Text("-", size=14, color="#333333")
    faculty_val = ft.Text("-", size=14, color="#333333")
    plan_val = ft.Text("-", size=14, color="#333333")
    phone_val = ft.Text("-", size=14, color="#333333")
    email_val = ft.Text("-", size=14, color="#333333")
    main_advisor_val = ft.Text("Loading...", size=14, color="#333333")
    co_advisor_val = ft.Text("-", size=14, color="#333333")

    # 🌟 ฟังก์ชันโหลดข้อมูลที่คลีนสุดๆ
    def load_data():
        result = controller.get_form1_detail(submission_id)

        if result["success"]:
            data = result["data"]
            # เอาข้อมูลที่ Controller จัดเรียงมาให้แล้ว หยอดลง UI เลย
            student_name_val.value = data["student_name"]
            student_id_val.value = data["student_id"]
            degree_val.value = data["degree"]
            program_val.value = data["program_name"]
            dept_val.value = data["department_name"]
            faculty_val.value = data["faculty"]
            plan_val.value = data["plan"]
            phone_val.value = data["phone"]
            email_val.value = data["email"]
            main_advisor_val.value = data["main_advisor"]
            co_advisor_val.value = data["co_advisor"]
        else:
            student_name_val.value = result["message"]
            student_name_val.color = "red"

        page.update()

    # --- UI Helper Function ---
    def create_row(label, value_control):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=120, content=ft.Text(label, size=14, color="#888888")
                ),
                ft.Container(expand=True, content=value_control),
            ],
        )

    # --- ประกอบร่าง Layout ---
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
                create_row("ระดับการศึกษา:", degree_val),
                create_row("หลักสูตร:", program_val),
                create_row("ภาควิชา:", dept_val),
                create_row("คณะ:", faculty_val),
                create_row("แผนการเรียน:", plan_val),
                create_row("เบอร์โทรศัพท์:", phone_val),
                create_row("อีเมล:", email_val),
            ],
        ),
    )

    advisor_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("อาจารย์ที่ปรึกษา", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                create_row("อาจารย์ที่ปรึกษาหลัก:", main_advisor_val),
                ft.Divider(height=1, color="#EEEEEE"),
                create_row("อาจารย์ที่ปรึกษาร่วม:", co_advisor_val),
            ],
        ),
    )

    load_data()

    return ft.View(
        route=f"/form1/{submission_id}",
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
                            "แบบฟอร์มขอรับรองการเป็นอาจารย์\nที่ปรึกษาวิทยานิพนธ์ หลัก/ร่วม",
                            size=18,
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    student_card,
                    ft.Container(padding=5),
                    advisor_card,
                    ft.Container(padding=20),
                ]
            )
        ],
    )
