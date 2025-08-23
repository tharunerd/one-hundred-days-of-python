import os
import smtplib
from email.mime.text import MIMEText

class NotificationManager:
    """
    Sends emails via SMTP. If env vars are missing, prints the message.
    Requires:
      - SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, FROM_EMAIL
    """

    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.user = os.getenv("SMTP_USER")
        self.password = os.getenv("SMTP_PASS")
        self.from_email = os.getenv("FROM_EMAIL")

        self.enabled = all([self.smtp_host, self.smtp_port, self.user, self.password, self.from_email])

    def send_emails(self, emails, message: str):
        if not emails:
            print("ℹ️ No recipient emails provided.")
            return

        if not self.enabled:
            print("[Email (dry-run)] Would send to:", ", ".join(emails))
            print(message)
            return

        msg = MIMEText(message, "plain")
        msg["Subject"] = "✈️ New Flight Deal!"
        msg["From"] = self.from_email

        with smtplib.SMTP(self.smtp_host, self.smtp_port) as conn:
            conn.starttls()
            conn.login(self.user, self.password)
            for email in emails:
                msg["To"] = email
                conn.sendmail(self.from_email, email, msg.as_string())
        print(f"📧 Sent email to {len(emails)} user(s).")
