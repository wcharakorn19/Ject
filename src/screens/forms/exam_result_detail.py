# src/screens/forms/exam_result_detail.py
import flet as ft
from controllers.form_controller import FormController


def ExamResultDetailScreen(page: ft.Page, submission_id: str):
    controller = FormController()
    user_role = page.session.get("user_role")

    # --- 1. เตรียมตัวแปร UI ---
    student_name_val = ft.Text("Loading...", size=14, color="#333333")
    student_id_val = ft.Text("Loading...", size=14, color="#333333")
    degree_val = ft.Text("-", size=14, color="#333333")
    program_val = ft.Text("-", size=14, color="#333333")

    doc_type_val = ft.Text("-", size=14, color="#333333")
    exam_type_val = ft.Text("-", size=14, color="#333333")
    exam_date_val = ft.Text("-", size=14, color="#333333")
    result_val = ft.Text("-", size=14, color="#333333")

    file_list_container = ft.Column(spacing=10)

    # --- 2. ฟังก์ชันดึงข้อมูลจาก Controller ---
    def load_data():
        result = controller.get_exam_result_detail(submission_id)

        if result["success"]:
            data = result["data"]
            student_name_val.value = data["student_name"]
            student_id_val.value = data["student_id"]
            degree_val.value = data["degree"]
            program_val.value = data["program_name"]

            doc_type_val.value = data["doc_type"]
            exam_type_val.value = data["exam_type"]
            exam_date_val.value = data["exam_date"]
            result_val.value = data["result_score"]

            # จัดการไฟล์แนบ
            file_list_container.controls.clear()
            base_url = "https://www.google.com/search?q="

            if data["files"]:
                for f in data["files"]:
                    file_name = f.get("name", "Unknown File")
                    full_url = f"{base_url}{file_name}"

                    file_row = ft.Container(
                        padding=10,
                        bgcolor="#F9F9F9",
                        border_radius=10,
                        on_click=lambda e, url=full_url: page.launch_url(url),
                        content=ft.Row(
                            [
                                ft.Icon(
                                    ft.Icons.INSERT_DRIVE_FILE, color="#5E5CE6", size=30
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            file_name,
                                            size=14,
                                            color="#333333",
                                            weight="bold",
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                        ft.Text(
                                            "แตะเพื่อเปิดไฟล์ (Mock)", size=12, color="grey"
                                        ),
                                    ],
                                    spacing=2,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    )
                    file_list_container.controls.append(file_row)
            else:
                file_list_container.controls.append(
                    ft.Text("ไม่มีไฟล์แนบ", size=14, color="grey")
                )
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

    # --- 4. Layout ---
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
            ],
        ),
    )

    exam_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("ข้อมูลผลสอบ", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                create_row("ประเภทเอกสาร:", doc_type_val),
                create_row("ประเภทการสอบ:", exam_type_val),
                create_row("วันที่สอบ:", exam_date_val),
                create_row("ผลสอบ/คะแนน:", result_val),
            ],
        ),
    )

    file_card = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=25,
        shadow=ft.BoxShadow(
            spread_radius=0, blur_radius=15, color="#08000000", offset=ft.Offset(0, 4)
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text("หลักฐานยื่นสอบ", size=16, weight="bold", color="black"),
                ft.Divider(height=10, color="transparent"),
                file_list_container,
            ],
        ),
    )

    load_data()

    return ft.View(
        route=f"/exam_result/{submission_id}",
        bgcolor="#FFF5F7",
        scroll=ft.ScrollMode.AUTO,
        appbar=ft.AppBar(
            # 🌟 ปุ่ม Back สับรางให้ถูก Role
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
                            "รายละเอียดการยื่นผลสอบ",
                            size=18,
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    student_card,
                    ft.Container(padding=5),
                    exam_card,
                    ft.Container(padding=5),
                    file_card,
                    ft.Container(padding=20),
                ]
            )
        ],
    )
