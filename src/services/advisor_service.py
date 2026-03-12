import requests
from core.config import API_BASE_URL

class AdvisorService:
    def __init__(self):
        # ใช้ Base URL 
        self.base_url = API_BASE_URL

    def fetch_dashboard_data(self, advisor_id):
        try:
            url = f"{self.base_url}/advisor/home?advisor_id={advisor_id}"
            print(f"DEBUG: Requesting URL -> {url}")

            headers = {"x-mock-match-request-query_params": "true"}

            # 🌟 แก้ไขตรงนี้: ใส่ headers=headers เข้าไปด้วย!
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                return response.json(), None
            return None, f"Error: {response.status_code}"
        except Exception as e:
            return None, str(e)
