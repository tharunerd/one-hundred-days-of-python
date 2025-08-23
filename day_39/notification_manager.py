import os
from twilio.rest import Client

class NotificationManager:
    """
    Sends SMS via Twilio. Falls back to print if creds are missing.
    """
    def __init__(self):
        self.sid = os.getenv("TWILIO_SID")
        self.token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("FROM_NUMBER")
        self.to_number = os.getenv("TO_NUMBER")

        self.enabled = all([self.sid, self.token, self.from_number, self.to_number])
        self.client = Client(self.sid, self.token) if self.enabled else None

    def send_sms(self, message: str):
        if not self.enabled:
            print(f"[SMS (dry-run)] {message}")
            return
        self.client.messages.create(body=message, from_=self.from_number, to=self.to_number)
        print("📲 SMS sent!")
