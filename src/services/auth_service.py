import requests
from core.config import API_BASE_URL

class AuthService:
    def login_api(self, email, password):
        url = f"{API_BASE_URL}/login"
        
        try:
            # วิ่งไปคุยกับ Mock API
            res = requests.post(
                url, 
                json={"email": email, "password": password}, 
                headers={"x-mock-match-request-body": "true"}, 
                timeout=5
            )
            
            if res.status_code == 200:
                return res.json(), None # สำเร็จ: คืนค่าข้อมูล, ไม่มี Error
            
            return None, "อีเมลหรือรหัสผ่านไม่ถูกต้อง" # พัง: คืนค่า None, แจ้ง Error
            
        except Exception as e:
            return None, f"เซิร์ฟเวอร์มีปัญหา: {str(e)}"