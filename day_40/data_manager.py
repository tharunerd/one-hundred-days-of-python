import os
import requests

class DataManager:
    """
    Handles Google Sheets via Sheety.
    Requires:
      - SHEETY_PRICES_ENDPOINT (e.g., .../prices)
      - SHEETY_USERS_ENDPOINT  (e.g., .../users)
      - SHEETY_TOKEN (optional Bearer token)
    """

    def __init__(self):
        self.prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        token = os.getenv("SHEETY_TOKEN")
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

        if not self.prices_endpoint or not self.users_endpoint:
            raise ValueError("Missing Sheety endpoints. Set SHEETY_PRICES_ENDPOINT and SHEETY_USERS_ENDPOINT in .env")

    def get_destinations(self):
        r = requests.get(self.prices_endpoint, headers=self.headers, timeout=20)
        r.raise_for_status()
        # Sheety typically wraps with resource name; infer it:
        data = r.json()
        # Use first key
        resource = next(iter(data))
        return data[resource]

    def update_iata_code(self, row_id: int, iata_code: str):
        url = f"{self.prices_endpoint}/{row_id}"
        # Infer singular name: e.g. prices -> price
        singular = self._infer_singular(self.prices_endpoint)
        body = {singular: {"iataCode": iata_code}}
        r = requests.put(url, json=body, headers=self.headers, timeout=20)
        r.raise_for_status()
        return r.json()

    def get_users(self):
        r = requests.get(self.users_endpoint, headers=self.headers, timeout=20)
        r.raise_for_status()
        data = r.json()
        resource = next(iter(data))
        return data[resource]

    def add_user(self, first: str, last: str, email: str):
        singular = self._infer_singular(self.users_endpoint)  # e.g. users -> user
        body = {singular: {"firstName": first, "lastName": last, "email": email}}
        r = requests.post(self.users_endpoint, json=body, headers=self.headers, timeout=20)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def _infer_singular(url: str) -> str:
        # crude but effective for .../prices and .../users
        if url.endswith("/prices"):
            return "price"
        if url.endswith("/users"):
            return "user"
        # fallback: drop trailing 's'
        return url.rstrip("/").split("/")[-1].rstrip("s")
