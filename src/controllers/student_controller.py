from services.student_service import StudentService

class StudentController:
    def __init__(self):
        self.service = StudentService()

    def get_dashboard_data(self, user_id, user_name_from_session):
        # 1. สั่งแมสเซนเจอร์ไปดึงข้อมูล JSON ของจริงมา
        data, error = self.service.fetch_home_data(user_id)
        
        if error:
            return {"success": False, "message": error}

        # 2. เตรียมพจนานุกรมแปลสถานะ (ดึงจาก API มาแปลเป็นไทยให้ UI สวยๆ)
        status_map = {
            "pending": "รอดำเนินการ",
            "approved": "อนุมัติเรียบร้อย",
            "rejected": "ถูกปฏิเสธ แก้ไขด่วน"
        }

        # 3. หางานที่กำลัง "รอดำเนินการ" มาโชว์เป็นการ์ดหลักด้านบน (Status Card)
        documents = data.get("documents", [])
        active_doc = {"name": "-", "status_text": "-"}
        
        for doc in documents:
            if doc["status"] == "pending":
                active_doc["name"] = doc["name"]
                active_doc["status_text"] = status_map.get(doc["status"], doc["status"])
                break # เจออันแรกที่รอดำเนินการปุ๊บ หยุดหาเลย เอาอันนี้แหละโชว์

        # 4. จัดเรียงรายการ Activities ทั้งหมด
        activities = []
        for doc in documents:
            activities.append({
                "title": doc["name"],
                "status": status_map.get(doc["status"], doc["status"])
            })

        # 5. ประกอบร่างข้อมูลเป็นก้อนมาตรฐาน ส่งให้หน้าจอ (Screen) เอาไปหยอดใส่ UI
        formatted_data = {
            "user_name": user_name_from_session,
            "current_doc": {
                "doc_name": active_doc["name"],
                "status_label": "สถานะ :",
                "status_text": active_doc["status_text"]
            },
            "activities": activities
        }
            
        return {"success": True, "data": formatted_data}