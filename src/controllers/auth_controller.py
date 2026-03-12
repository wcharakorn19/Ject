# src/controllers/auth_controller.py
from services.auth_service import AuthService


class AuthController:
    def __init__(self):
        self.service = AuthService()

    def process_login(self, email, password):
        # 1. ตรวจสอบเบื้องต้น (Validation)
        if not email or not email.strip():
            return {"success": False, "message": "กรุณากรอกอีเมล"}
        if not password or not password.strip():
            return {"success": False, "message": "กรุณากรอกรหัสผ่าน"}

        # 2. สั่ง Service ยิง API ไปหา Postman
        # Postman จะคาย JSON ของ Student 1 หรือ 2 ออกมาตาม Example ที่เราเลือก
        data, error = self.service.login_api(email, password)

        if error:
            return {"success": False, "message": error}

        # 3. 🌟 จุดสำคัญ: ดึงข้อมูลจาก JSON ของจริงที่ได้รับมา
        # อ้างอิงตามโครงสร้าง JSON ใน Postman ของนาย
        student_data = data.get("student", {})

        # ถ้าไม่มีก้อน student ให้ลองหาในก้อน user (เผื่อโครงสร้างเปลี่ยน)
        if not student_data:
            student_data = data.get("user", {})

        user_id = student_data.get("id")
        user_name = student_data.get("name", "Unknown User")
        role = student_data.get(
            "role", "student"
        )  # ถ้าใน JSON ไม่มี role ให้เป็น student ไว้ก่อน

        print(f"[DEBUG] Login Success: {user_name} (ID: {user_id})")

        # --- ดึงข้อมูลเพิ่มเติมสำหรับหน้า Profile ตามโครงสร้างใหม่ ---
        education_level = student_data.get("education_level", "-")
        study_plan = student_data.get("study_plan", "-")
        program = student_data.get("program", "-")
        department = student_data.get("department", "-")
        faculty = student_data.get("faculty", "-")
        status = student_data.get("status", "-")
        phone = student_data.get("phone", "-")

        # ข้อมูลวิทยานิพนธ์
        thesis_data = student_data.get("thesis", {})
        thesis_th = thesis_data.get("title_th", "-")
        thesis_en = thesis_data.get("title_en", "-")
        main_advisor = thesis_data.get("main_advisor", "-")
        co_advisor_1 = thesis_data.get("co_advisor_1", "-")
        co_advisor_2 = thesis_data.get("co_advisor_2", "-")

        # ข้อมูลสรุปผลการดำเนินการ
        progress_data = student_data.get("progress", {})
        topic_exam_date = progress_data.get("topic_exam_date", "-")
        topic_status = progress_data.get("topic_status", "-")
        topic_approve_date = progress_data.get("topic_approve_date", "-")

        final_exam_date = progress_data.get("final_exam_date", "-")
        final_status = progress_data.get("final_status", "-")
        final_approve_date = progress_data.get("final_approve_date", "-")

        english_test_type = progress_data.get("english_test_type", "-")
        english_test_date = progress_data.get("english_test_date", "-")
        english_test_status = progress_data.get("english_test_status", "-")

        # 4. ส่งข้อมูลกลับไปให้หน้าจอเซ็ตลง Session
        return {
            "success": True,
            "session_data": {
                "user_id": str(user_id)
                if user_id
                else "65030130",  # เก็บ ID จริงจาก Postman
                "user_full_name": user_name,  # เก็บชื่อจริงจาก Postman
                "user_role": role,
                "user_email": email
                if email
                else "65030130@kmitl.ac.th",  # เก็บอีเมลที่กรอกตอน Login ใส่ไปใน Profile
                # เก็บข้อมูลใหม่ลง Session
                "education_level": education_level,
                "study_plan": study_plan,
                "program": program,
                "department": department,
                "faculty": faculty,
                "status": status,
                "phone": phone,
                "thesis_th": thesis_th,
                "thesis_en": thesis_en,
                "main_advisor": main_advisor,
                "co_advisor_1": co_advisor_1,
                "co_advisor_2": co_advisor_2,
                "topic_exam_date": topic_exam_date,
                "topic_status": topic_status,
                "topic_approve_date": topic_approve_date,
                "final_exam_date": final_exam_date,
                "final_status": final_status,
                "final_approve_date": final_approve_date,
                "english_test_type": english_test_type,
                "english_test_date": english_test_date,
                "english_test_status": english_test_status,
            },
            "route": "/advisor_home" if role == "advisor" else "/student_home",
        }
