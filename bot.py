import feedparser
import time
from telegram import Bot

# === CONFIGURATION ===
BOT_TOKEN = "8027558655:AAF1Idgdbnrymg68srXuUrcHHI6IVvaeiTk"
CHAT_ID = "@Newsbreaknb_bot"  # This is your channel username

RSS_FEED_URL = "https://mylolowcountry.com/feed/"
CHECK_INTERVAL = 300  # Check every 5 minutes

# === Initialize Bot ===
bot = Bot(token=BOT_TOKEN)
sent_links = set()

def fetch_and_send():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        if entry.link not in sent_links:
            message = f"📰 {entry.title}\n{entry.link}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            sent_links.add(entry.link)

# === Run the Bot Loop ===
if __name__ == "__main__":
    print("Telegram feed bot is running...")
    while True:
        try:
            fetch_and_send()
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(CHECK_INTERVAL)
