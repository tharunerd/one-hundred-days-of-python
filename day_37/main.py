import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME") 
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "1",  # change this to the value of your habit (like "5", "2.5", etc.)
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Delete endpoint
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)


