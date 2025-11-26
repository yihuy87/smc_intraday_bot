# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# === TELEGRAM ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
# ID admin utama (chat_id Telegram kamu)
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID", "")

# === BINANCE ===
BINANCE_REST_URL = "https://api.binance.com"
BINANCE_STREAM_URL = "wss://stream.binance.com:9443/stream"

# Berapa banyak pair USDT yang discan
MAX_USDT_PAIRS = 1000

# Tier minimum sinyal yang dikirim: "A+", "A", "B"
MIN_TIER_TO_SEND = "A"  # balanced default

# Cooldown default antar sinyal per pair (detik)
SIGNAL_COOLDOWN_SECONDS = 900  # 15 menit
