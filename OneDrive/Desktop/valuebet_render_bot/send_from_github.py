
import requests
import asyncio
from telegram import Bot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = YOUR_CHAT_ID  # Số, không có dấu nháy

async def main():
    bot = Bot(token=TOKEN)
    url = 'https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/value_bet.txt'
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
