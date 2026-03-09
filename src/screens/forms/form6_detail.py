# src/screens/forms/form6_detail.py
import flet as ft
from controllers.form_controller import FormController


def FormSixDetailScreen(page: ft.Page, submission_id: str):
    controller = FormController()
    user_role = page.session.get("user_role")

    # --- 1. เตรียมตัวแปร UI ---
    student_name_val = ft.Text("Loading...", size=14, color="#333333")
    student_id_val = ft.Text("Loading...", size=14, color="#333333")
    degree_val = ft.Text("-", size=14, color="#333333")
    program_val = ft.Text("-", size=14, color="#333333")
    dept_val = ft.Text("-", size=14, color="#333333")

    start_semester_val = ft.Text("-", size=14, color="#333333")
    start_year_val = ft.Text("-", size=14, color="#333333")
    phone_val = ft.Text("-", size=14, color="#333333")
    address_val = ft.Text("-", size=14, color="#333333")
    workplace_val = ft.Text("-", size=14, color="#333333")

    thesis_th_val = ft.Text("-", size=14, color="#333333")
    thesis_en_val = ft.Text("-", size=14, color="#333333")

    main_advisor_val = ft.Text("-", size=14, color="#333333")
    co_advisor_val = ft.Text("-", size=14, color="#333333")
    chair_val = ft.Text("-", size=14, color="#333333")
    committee_val = ft.Text("-", size=14, color="#333333")
    member5_val = ft.Text("-", size=14, color="#333333")
    reserve_ext_val = ft.Text("-", size=14, color="#333333")
    reserve_int_val = ft.Text("-", size=14, color="#333333")

    # --- 2. ฟังก์ชันดึงข้อมูลจาก Controller ---
    def load_data():
        result = controller.get_form6_detail(submission_id)

        if result["success"]:
            data = result["data"]
            student_name_val.value = data["student_name"]
            student_id_val.value = data["student_id"]
            degree_val.value = data["degree"]
            program_val.value = data["program_name"]
            dept_val.value = data["department_name"]
            phone_val.value = data["phone"]

            start_semester_val.value = data["start_semester"]
            start_year_val.value = data["start_year"]
            address_val.value = data["address"]
            workplace_val.value = data["workplace"]

            thesis_th_val.value = data["thesis_th"]
            thesis_en_val.value = data["thesis_en"]

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
                    width=130, content=ft.Text(label, size=14, color="#888888")
                ),
                ft.Container(expand=True, content=value_control),
            ],
        )

    # --- 4. Layout ---
    info_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("ข้อมูลผู้ยื่นคำร้อง", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                create_row("ชื่อ-สกุล:", student_name_val),
                create_row("รหัสประจำตัว:", student_id_val),
                create_row("ระดับปริญญา:", degree_val),
                create_row("สาขาวิชา:", program_val),
                create_row("ภาควิชา:", dept_val),
                create_row("เริ่มศึกษาภาคเรียนที่:", start_semester_val),
                create_row("ปีการศึกษา:", start_year_val),
                create_row("เบอร์โทร:", phone_val),
                create_row("ที่อยู่ปัจจุบัน:", address_val),
                create_row("สถานที่ทำงาน:", workplace_val),
                ft.Divider(height=10, color="#EEEEEE"),
                create_row("ชื่อวิทยานิพนธ์ (TH):", thesis_th_val),
                create_row("ชื่อวิทยานิพนธ์ (EN):", thesis_en_val),
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
                    "คณะกรรมการสอบและอาจารย์ที่ปรึกษา",
                    size=16,
                    weight="bold",
                    color="black",
                ),
                ft.Divider(height=10, color="transparent"),
                create_row("ที่ปรึกษาหลัก:", main_advisor_val),
                create_row("ที่ปรึกษาร่วม 1:", co_advisor_val),
                ft.Divider(height=20, color="#EEEEEE"),
                ft.Text("คณะกรรมการสอบ", size=15, weight="bold", color="black"),
                create_row("ประธานกรรมการสอบ:", chair_val),
                create_row("กรรมการ (ร่วม 2):", committee_val),
                create_row("กรรมการสอบ (คนที่ 5):", member5_val),
                ft.Divider(height=20, color="#EEEEEE"),
                ft.Text("กรรมการสำรอง", size=15, weight="bold", color="black"),
                create_row("สำรอง (ภายนอก):", reserve_ext_val),
                create_row("สำรอง (ภายใน):", reserve_int_val),
            ],
        ),
    )

    load_data()

    return ft.View(
        route=f"/form6/{submission_id}",
        bgcolor="#FFF5F7",
        scroll=ft.ScrollMode.AUTO,
        appbar=ft.AppBar(
            # 🌟 ปุ่ม Back สับราง
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
                            "บันทึกข้อความ: ขอแต่งตั้งคณะกรรมการ\nสอบวิทยานิพนธ์ขั้นสุดท้าย",
                            size=18,
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    info_card,
                    ft.Container(padding=5),
                    committee_card,
                    ft.Container(padding=20),
                ]
            )
        ],
    )
