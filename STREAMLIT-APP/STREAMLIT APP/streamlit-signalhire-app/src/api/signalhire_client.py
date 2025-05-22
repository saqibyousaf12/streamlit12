class SignalHireClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.signalhire.com/v1"

    def search_candidates(self, items: list, callback_url: str):
        url = f"{self.base_url}/candidates/search"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "items": items,
            "callback_url": callback_url
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("request_id")
        else:
            response.raise_for_status()