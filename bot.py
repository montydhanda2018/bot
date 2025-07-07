import feedparser
import time
import os
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# === Config ===
BOT_TOKEN = os.getenv(8027558655:AAF1Idgdbnrymg68srXuUrcHHI6IVvaeiTk)  # Set this in your .env or Render env
CHAT_ID = os.getenv(Newsbreaknb_bot)      # Your Telegram user/channel ID
RSS_FEED_URL = 'https://mylolowcountry.com/feed/'
CHECK_INTERVAL = 300  # Check every 5 minutes

bot = Bot(token=BOT_TOKEN)
sent_links = set()

def fetch_and_send():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        if entry.link not in sent_links:
            message = f"📰 {entry.title}\n{entry.link}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            sent_links.add(entry.link)

if __name__ == "__main__":
    print("Bot is running...")
    while True:
        try:
            fetch_and_send()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(CHECK_INTERVAL)
