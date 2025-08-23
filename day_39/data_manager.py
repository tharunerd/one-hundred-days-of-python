import os
import requests

class DataManager:
    """
    Handles Google Sheet data via Sheety.
    Expects the sheet to have: city, iataCode, lowestPrice, id
    """
    def __init__(self):
        self.endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.token = os.getenv("SHEETY_TOKEN")
        self.resource = os.getenv("SHEETY_RESOURCE_NAME", "prices")
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get_destinations(self):
        r = requests.get(self.endpoint, headers=self.headers, timeout=20)
        r.raise_for_status()
        # Sheety wraps rows by resource name
        return r.json()[self.resource]

    def update_iata_code(self, row_id: int, iata_code: str):
        url = f"{self.endpoint}/{row_id}"
        body = {self.resource[:-1] if self.resource.endswith('s') else self.resource: {"iataCode": iata_code}}
        r = requests.put(url, json=body, headers=self.headers, timeout=20)
        r.raise_for_status()
        return r.json()
