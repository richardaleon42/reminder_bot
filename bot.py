import os
import requests
from datetime import datetime

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

message = "Good morning everyone! ☀️"

system_time = datetime.now()

print("System time:", system_time.strftime("%Y-%m-%d %H:%M:%S %Z"))

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=30
)

response.raise_for_status()

print("Message sent successfully!")