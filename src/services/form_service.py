import requests


class FormService:
    def __init__(self):
        self.base_url = "https://0e73cfd5-6b5f-4082-9c37-514cf7941cc1.mock.pstmn.io"

    def fetch_form1_detail(self, submission_id: str):
        try:
            url = f"{self.base_url}/submissions/{submission_id}"
            res = requests.get(url, timeout=5)

            if res.status_code == 200:
                return res.json(), None
            return None, f"API Error: {res.status_code}"
        except Exception as e:
            return None, f"Connection Error: {str(e)}"
