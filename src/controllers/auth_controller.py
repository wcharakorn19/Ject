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
        role = student_data.get("role", "student") # ถ้าใน JSON ไม่มี role ให้เป็น student ไว้ก่อน

        print(f"[DEBUG] Login Success: {user_name} (ID: {user_id})")

        # 4. ส่งข้อมูลกลับไปให้หน้าจอเซ็ตลง Session
        return {
            "success": True,
            "session_data": {
                "user_id": str(user_id),       # เก็บ ID จริงจาก Postman
                "user_full_name": user_name,   # เก็บชื่อจริงจาก Postman
                "user_role": role
            },
            "route": "/advisor_home" if role == "advisor" else "/student_home"
        }