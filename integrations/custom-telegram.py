import requests

# Replace with your Telegram bot token
TOKEN = "YOUR_BOT_TOKEN"

# Replace with your Telegram chat ID
CHAT_ID = "YOUR_CHAT_ID"

# Example alert message
message = "🚨 Test alert from Wazuh SOC Lab"

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.status_code)
