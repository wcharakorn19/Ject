# src/core/app_router.py
import flet as ft

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


class AppRouter:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

    def route_change(self, route):
        t_route = ft.TemplateRoute(self.page.route)
        print(f"🚦 Router สับรางไปที่: {self.page.route}")

        if t_route.match("/"):
            self.page.views.clear()
            self.page.views.append(WelcomeScreen(self.page))

        elif t_route.match("/login"):
            self.page.views.append(LoginScreen(self.page))

        elif t_route.match("/student_home"):
            self.page.views.clear()
            self.page.views.append(StudentHome(self.page))

        elif t_route.match("/profile"):
            self.page.views.clear()
            self.page.views.append(ProfileScreen(self.page))

        elif t_route.match("/advisor_home"):
            self.page.views.clear()
            self.page.views.append(AdvisorHome(self.page))

        # --- โซน Route ของฟอร์มทั้ง 7 ---
        elif self.page.route.startswith("/form1/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormOneDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/form2/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormTwoDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/form3/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormThreeDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/form4/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormFourDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/form5/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormFiveDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/form6/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(FormSixDetailScreen(self.page, submission_id))

        elif self.page.route.startswith("/exam_result/"):
            submission_id = self.page.route.split("/")[-1]
            self.page.views.append(ExamResultDetailScreen(self.page, submission_id))

        else:
            print("❌ หา Route ไม่เจอ! เตะกลับไปหน้า Login")
            self.page.views.clear()
            self.page.views.append(LoginScreen(self.page))

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()

        if len(self.page.views) > 0:
            top_view = self.page.views[-1]
            self.page.go(top_view.route)
        else:
            self.page.go("/")
