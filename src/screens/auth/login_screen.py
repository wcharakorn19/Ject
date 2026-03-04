# src/screens/auth/login_screen.py
import flet as ft
from components.buttons import PrimaryButton     # 🧱 หยิบปุ่มของนายมาใช้
from components.inputs import AppTextField       # 🧱 หยิบช่องกรอกของนายมาใช้
from controllers.auth_controller import AuthController # 🧠 หยิบสมองมาใช้

def LoginScreen(page: ft.Page):
    print("[INFO] LoginScreen")
    
    # 🌟 เรียกใช้ Controller (สมอง)
    controller = AuthController()

    siet_logo = ft.Image(src="logo_1.jpeg", width=150, height=150, fit=ft.ImageFit.FIT_WIDTH)
    
    # กลุ่มข้อความยืนยันตัวตน
    txt_group = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", size=16, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text("โดยใช้ E-mail Account ของสถาบันฯ", color="#000000"),
            ]
        )
    )

    # ฟิลด์สำหรับกรอกอีเมลและรหัสผ่าน
    email_field = AppTextField(label="E-mail Account")
    password_field = AppTextField(label="Password", is_password=True)
    
    # --- 2. ฟังก์ชันตรวจสอบข้อมูลและล็อกอิน (UI Logic) ---
    def do_login(e):
        email = email_field.value.strip() if email_field.value else ""
        password = password_field.value.strip() if password_field.value else ""
        
        # คลีน Error เก่าทิ้งก่อน
        email_field.error_text = None
        password_field.error_text = None
        has_error = False

        # เช็คช่องว่าง (Validation)
        if not email:
            email_field.error_text = "กรุณากรอกอีเมล"
            has_error = True
        if not password:
            password_field.error_text = "กรุณากรอกรหัสผ่าน"
            has_error = True

        if has_error:
            page.update()
            return

        # โชว์วงแหวนโหลด
        login_btn_actual.content = ft.ProgressRing(width=20, height=20, color="#FFF6FE")
        login_btn_actual.disabled = True
        page.update()

        # 🧠 โยนให้ Controller คิดและยิง API
        result = controller.process_login(email, password)

        # คืนค่าปุ่มกลับมาเป็นตัวหนังสือ
        login_btn_actual.content = ft.Text("LOG IN", weight=ft.FontWeight.BOLD)
        login_btn_actual.disabled = False

        # ประมวลผลลัพธ์จาก Controller
        if result["success"]:
            # เก็บ Session และเปลี่ยนหน้า
            for key, value in result["session_data"].items():
                page.session.set(key, value)
            page.go(result["route"])
        else:
            # แจ้งเตือนถ้ารหัสผิด
            page.snack_bar = ft.SnackBar(ft.Text(result["message"]), bgcolor="red")
            page.snack_bar.open = True

        page.update()

    # --- 3. ปุ่มล็อกอินและจัด Layout (กล่องซ้อนกล่องของนาย) ---
    login_btn_actual = PrimaryButton(
        text="LOG IN",
        on_click=do_login,
        padding=ft.padding.symmetric(horizontal=40, vertical=20)
    )
    
    login_btn_container = ft.Container(content=login_btn_actual)
            
    # จัดกลุ่มฟิลด์และปุ่มล็อกอิน
    field_group = ft.Container(
        content=ft.Column(
            controls=[email_field, password_field, login_btn_container],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        margin=ft.margin.only(top=50)
    )
   
    # กล่องล็อกอิน (กล่องเทา)
    login_box = ft.Container(
        content=ft.Column(
            controls=[txt_group, field_group]
        ),
        bgcolor="#E0E0E0",
        border_radius=20,
        padding=ft.padding.only(left=30, right=30, top=30, bottom=30)
    )
    
    # กล่องสีแดง (กล่องนอกสุด)
    red_box = ft.Container(
        content=login_box,
        bgcolor="#EF3961",
        margin=ft.margin.only(top=50),
        padding=ft.padding.only(left=25, right=25, top=50, bottom=50)
    )

    # ส่งออกหน้าจอ Login
    return ft.View(
        route="/login",
        bgcolor="#FFF6FE",
        appbar=ft.AppBar(
            title=ft.Text("KMITL"), 
            center_title=True,
            color="#FFF6FE", 
            bgcolor="#EF3961"
        ),
        controls=[
            siet_logo,
            red_box   
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.END,
        padding=0
    )