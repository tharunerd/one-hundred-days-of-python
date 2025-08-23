import os
import requests
from datetime import datetime, timedelta

class FlightSearch:
    """
    Kiwi (Tequila) API wrapper.
    - get_iata(city_name)
    - search_flight(fly_from, fly_to, months_ahead, nights_in_dst_from, nights_in_dst_to)
    """

    def __init__(self):
        self.api_key = os.getenv("TEQUILA_API_KEY")
        if not self.api_key:
            raise ValueError("Missing TEQUILA_API_KEY in .env")
        self.base = "https://api.tequila.kiwi.com"
        self.headers = {"apikey": self.api_key}
        self.currency = os.getenv("CURRENCY", "INR")
        self.max_stopovers = int(os.getenv("MAX_STOPOVERS", "0"))

    def get_iata(self, city_name: str) -> str:
        params = {"term": city_name, "location_types": "city", "limit": 1}
        r = requests.get(f"{self.base}/locations/query", headers=self.headers, params=params, timeout=20)
        r.raise_for_status()
        locations = r.json().get("locations", [])
        return locations[0]["code"] if locations else ""

    def search_flight(self, fly_from: str, fly_to: str,
                      months_ahead: int = 6,
                      nights_in_dst_from: int = 7,
                      nights_in_dst_to: int = 28):
        date_from = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
        date_to = (datetime.today() + timedelta(days=30*months_ahead)).strftime("%d/%m/%Y")

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": self.currency,
            "max_stopovers": self.max_stopovers
        }

        r = requests.get(f"{self.base}/v2/search", headers=self.headers, params=params, timeout=25)
        r.raise_for_status()
        data = r.json().get("data", [])
        if not data:
            return None

        deal = data[0]
        return {
            "price": deal["price"],
            "origin_city": deal["cityFrom"],
            "origin_airport": deal["flyFrom"],
            "destination_city": deal["cityTo"],
            "destination_airport": deal["flyTo"],
            "out_date": deal["route"][0]["local_departure"][:10],
            "return_date": deal["route"][-1]["local_departure"][:10],
            "deep_link": deal.get("deep_link", "")
        }
