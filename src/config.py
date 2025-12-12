import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
HONEYPOT_CHANNEL = int(os.getenv("HONEYPOT_CHANNEL"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
BOT_ACTION = os.getenv("BOT_ACTION", "kick").lower()
PURGE_TIMEFRAME = int(os.getenv("PURGE_TIMEFRAME", 300))
