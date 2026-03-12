# src/services/student_service.py
import httpx
from core.config import API_BASE_URL


class StudentService:
    def __init__(self):
        # URL ของ Postman Mock Server
        self.base_url = API_BASE_URL

    async def fetch_home_data(self, user_id):
        try:
            # 🌟 จุดสำคัญ: พ่วง ?user_id ไปที่ URL เพื่อให้ Postman เลือก Example ที่ถูกต้อง
            url = f"{self.base_url}/student/home?user_id={user_id}"

            # 🚀 ยิง GET Request ไปหา Server ด้วย httpx แบบ Async
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url,
                    headers={"x-mock-match-request-query_params": "true"},
                    timeout=10.0,
                )

            # ตรวจสอบ Response Status
            if response.status_code == 200:
                data = response.json()
                print(f"[SUCCESS] ดึงข้อมูลหน้า Home สำเร็จ สำหรับ ID: {user_id}")
                return data, None
            else:
                return None, f"ไม่สามารถดึงข้อมูลได้ (Error: {response.status_code})"

        except Exception as e:
            print(f"[ERROR] StudentService: {e}")
            return None, f"เชื่อมต่อเซิร์ฟเวอร์ไม่ได้: {str(e)}"

    async def fetch_profile_data(self, user_id):
        try:
            url = f"{self.base_url}/student/profile?user_id={user_id}"

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url,
                    headers={"x-mock-match-request-query_params": "true"},
                    timeout=10.0,
                )

            if response.status_code == 200:
                data = response.json()
                print(f"[SUCCESS] ดึงข้อมูลหน้า Profile สำเร็จ สำหรับ ID: {user_id}")
                return data, None
            else:
                return None, f"ไม่สามารถดึงข้อมูลได้ (Error: {response.status_code})"

        except Exception as e:
            print(f"[ERROR] StudentProfile: {e}")
            return None, f"เชื่อมต่อเซิร์ฟเวอร์ไม่ได้: {str(e)}"
