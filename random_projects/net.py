import speedtest
import csv
from datetime import datetime

st = speedtest.Speedtest()
download = st.download() / 1_000_000  # Convert to Mbps
upload = st.upload() / 1_000_000

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("net_speed_log.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([now, round(download, 2), round(upload, 2)])

