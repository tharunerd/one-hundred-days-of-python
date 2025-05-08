import time
from plyer import notification

while True:
    notification.notify(
        title="Reminder!",
        message="It's time for a break or to check something!",
        timeout=5  # Notification stays for 5 seconds
    )
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
