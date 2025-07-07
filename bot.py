import feedparser
import asyncio
from telegram import Bot

# === CONFIGURATION ===
BOT_TOKEN = "8027558655:AAF1Idgdbnrymg68srXuUrcHHI6IVvaeiTk"
CHAT_ID = "@Newsbreaknb_bot"  # Telegram username or chat ID
RSS_FEED_URL = "https://mylolowcountry.com/feed/"
CHECK_INTERVAL = 300  # seconds (5 minutes)

# === Initialize Bot ===
bot = Bot(token=BOT_TOKEN)
sent_links = set()

async def fetch_and_send():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        if entry.link not in sent_links:
            message = f"📰 {entry.title}\n{entry.link}"
            await bot.send_message(chat_id=CHAT_ID, text=message)
            sent_links.add(entry.link)

async def main_loop():
    print("Telegram feed bot is running...")
    while True:
        try:
            await fetch_and_send()
        except Exception as e:
            print(f"Error occurred: {e}")
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main_loop())
