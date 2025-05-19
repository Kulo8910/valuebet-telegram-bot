import requests
import asyncio
from telegram import Bot

TOKEN = '7713996684:AAHu0ZAZQf1HmJFckAPn9P-Ffh_idJI94vg'
CHAT_ID = 5686594211

async def main():
    bot = Bot(token=TOKEN)
    url = 'https://raw.githubusercontent.com/Kulo8910/valuebet-telegram-bot/main/value_bet.txt'
    sent_file = "sent_lines.txt"

    try:
        response = requests.get(url)
        content = response.text
        lines = content.splitlines()
    except Exception as e:
        print(f"Không tải được file: {e}")
        return

    # Tải danh sách dòng đã gửi trước đó (nếu có)
    try:
        with open(sent_file, "r", encoding="utf-8") as f:
            sent_lines = set(f.read().splitlines())
    except FileNotFoundError:
        sent_lines = set()

    for line in lines:
        if "|" in line:
            try:
                if line in sent_lines:
                    continue
                value = float(line.split("|")[-1].replace("%", "").strip())
                if value >= 10:
                    await bot.send_message(chat_id=CHAT_ID, text=line.strip())
                    print("Đã gửi:", line)
                    sent_lines.add(line)
            except Exception as e:
                print(f"Lỗi dòng: {line} => {e}")

    # Ghi lại danh sách dòng đã gửi
    with open(sent_file, "w", encoding="utf-8") as f:
        f.write("\n".join(sent_lines))

asyncio.run(main())
