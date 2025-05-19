import requests
import asyncio
from telegram import Bot

TOKEN = '7713996684:AAHu0ZAZQf1HmJFckAPn9P-Ffh_idJI94vg'
CHAT_ID = 5686594211  # ID cá nhân của bạn

async def main():
    bot = Bot(token=TOKEN)
    url = 'https://raw.githubusercontent.com/Kulo8910/valuebet-telegram-bot/main/value_bet.txt'
    try:
        response = requests.get(url)
        content = response.text
        lines = content.splitlines()
        for line in lines:
            if "|" in line:
                try:
                    value = float(line.split("|")[-1].replace("%", "").strip())
                    if value >= 10:
                        await bot.send_message(chat_id=CHAT_ID, text=line.strip())
                        print("Đã gửi:", line.strip())
                except Exception as e:
                    print("Lỗi dòng:", line.strip(), "|", e)
    except Exception as e:
        print("Không tải được file từ GitHub:", e)

asyncio.run(main())
