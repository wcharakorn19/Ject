# src/controllers/advisor_controller.py
from services.advisor_service import AdvisorService
from models.document_model import AdvisorDashboardModel, StudentSummaryModel, ActivityModel

class AdvisorController:
    def __init__(self):
        self.service = AdvisorService()

    # 🌟 ฟังก์ชันดึงข้อมูล (Data Logic) ที่คลีนและเบาที่สุด
    def get_dashboard_data(self, user_id):
        data, error = self.service.fetch_dashboard_data(user_id)

        if error:
            return {"success": False, "message": error, "data": None}

        students = [
            StudentSummaryModel(name=s.get("name", "N/A"), doc_status=s.get("doc_status", "-")) 
            for s in data.get("students", [])
        ]
        
        activities = [
            ActivityModel(
                title=a.get("doc_name", "N/A"), 
                status=a.get("status", "-"),
                name=a.get("name", ""),
                form_type=a.get("form_type", "form1"),
                submission_id=a.get("submission_id", "12345")
            ) 
            for a in data.get("activities", [])
        ]
        
        model = AdvisorDashboardModel(
            student_count=data.get("student_count", 0),
            students=students,
            activities=activities
        )

        return {"success": True, "data": model}
