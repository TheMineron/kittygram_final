import requests

BOT_TOKEN = "8345082485:AAFMmmc_fT6gbfMtR9rnwE38s3ty3ZI9xgM"


# Получаем обновления (бот должен быть администратором)
response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
)

# ID группы будет в chat.id (отрицательное число)
print(response.json())
for update in response.json().get("result", []):
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        print(f"Chat ID: {chat_id}")