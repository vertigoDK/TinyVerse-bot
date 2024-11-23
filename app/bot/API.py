import requests
import config

class APIHandler:
    BASE_URL = "https://api.tonverse.app"

    HEADERS = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "136",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "api.tonverse.app",
        "Origin": "https://app.tonverse.app",
        "Referer": "https://app.tonverse.app/",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        ),
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    def __init__(self):
        self.session_id = config.SESSION_ID
        if not self.session_id:
            raise ValueError("For start provide a session ID")

    def collect_stars(self) -> dict[str,str]:
        data = {
            "session": self.session_id,
        }

        response = requests.post(url=self.BASE_URL + "/galaxy/collect", data=data, headers=self.HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error occurred", "status_code": response.status_code}


    def check_stats(self) -> dict[str,str]:
        data = {
            "session": self.session_id,
        }
        response = requests.post(url=self.BASE_URL + "/user/info", data=data, headers=self.HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error occurred", "status_code": response.status_code}