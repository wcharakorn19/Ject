# src/controllers/advisor_controller.py
from services.advisor_service import AdvisorService


class AdvisorController:
    def __init__(self):
        self.service = AdvisorService()

    # 🌟 ฟังก์ชันดึงข้อมูล (Data Logic) ที่คลีนและเบาที่สุด
    def get_dashboard_data(self, user_id):
        data, error = self.service.fetch_dashboard_data(user_id)

        if error:
            return {"success": False, "message": error, "data": None}

        # ตอนนี้หน้า UI (advisor_home.py) ดึงข้อมูล JSON ไปจัดการวาดหน้าจอเองแล้ว
        # Controller เลยทำหน้าที่แค่เช็ค Error และส่งข้อมูลดิบ (data) กลับไปให้ครบๆ ก็พอครับ
        return {"success": True, "data": data}
