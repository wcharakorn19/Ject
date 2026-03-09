import flet as ft

# --- 🌟 โซน Import หน้าจอที่สร้างเสร็จแล้ว ---
from screens.auth.welcome_screen import WelcomeScreen
from screens.auth.login_screen import LoginScreen
from screens.student.student_home import StudentHome
from screens.advisor.advisor_home import AdvisorHome
from screens.profile_screen import ProfileScreen

from screens.forms.form1_detail import FormOneDetailScreen
from screens.forms.form2_detail import FormTwoDetailScreen
from screens.forms.form3_detail import FormThreeDetailScreen
from screens.forms.form4_detail import FormFourDetailScreen
from screens.forms.form5_detail import FormFiveDetailScreen
from screens.forms.form6_detail import FormSixDetailScreen
from screens.forms.exam_result_detail import ExamResultDetailScreen


# Setup App
def main(page: ft.Page):
    page.title = "Graduate Student Tracking System"
    page.window.width = 402
    page.window.height = 874

    # Setup Navigation and Routing
    def route_change(route):
        t_route = ft.TemplateRoute(page.route)
        # (เพิ่ม Print ดักจับไว้ดูเล่นๆ ว่ามันวิ่งไปไหน)
        print(f"🚦 Router สับรางไปที่: {page.route}")

        if t_route.match("/"):
            page.views.clear()
            page.views.append(WelcomeScreen(page))

        elif t_route.match("/login"):
            page.views.append(LoginScreen(page))

        # 🌟 วิ่งเข้าหน้านี้เมื่อล็อกอินสำเร็จ!
        elif t_route.match("/student_home"):
            page.views.append(StudentHome(page))

        elif t_route.match("/profile"):
            page.views.append(ProfileScreen(page))

        # ---------------------------------------------------------
        # ⚠️ โซนหน้าจออื่นๆ (Andy คอมเมนต์ไว้ให้ก่อนชั่วคราว)
        # ถ้านายสร้างไฟล์พวกนี้เสร็จ และ Import ข้างบนแล้ว ค่อยเอาเครื่องหมาย # ออกนะ
        # ---------------------------------------------------------
        # elif t_route.match("/contact"):
        #     page.views.append(ContactScreen(page))
        elif t_route.match("/advisor_home"):
            page.views.append(AdvisorHome(page))

        # --- โซน Route ของฟอร์มทั้ง 7 ---
        elif page.route.startswith("/form1/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormOneDetailScreen(page, submission_id))

        elif page.route.startswith("/form2/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormTwoDetailScreen(page, submission_id))

        elif page.route.startswith("/form3/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormThreeDetailScreen(page, submission_id))

        elif page.route.startswith("/form4/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormFourDetailScreen(page, submission_id))

        elif page.route.startswith("/form5/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormFiveDetailScreen(page, submission_id))

        # 🌟 เติมดักจับ Route ของฟอร์ม 6
        elif page.route.startswith("/form6/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(FormSixDetailScreen(page, submission_id))

        # 🌟 เติมดักจับ Route ของผลสอบ (ฟอร์ม 7)
        elif page.route.startswith("/exam_result/"):
            submission_id = page.route.split("/")[-1]
            page.views.append(ExamResultDetailScreen(page, submission_id))

        # --- 3. ดักจับ Error (Fallback) ---
        else:
            print("❌ หา Route ไม่เจอ! เตะกลับไปหน้า Login")
            page.views.append(LoginScreen(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
