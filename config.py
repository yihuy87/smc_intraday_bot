import os
from dotenv import load_dotenv

load_dotenv()

# === TELEGRAM ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# === BINANCE ===
BINANCE_REST_URL = "https://api.binance.com"
BINANCE_STREAM_URL = "wss://stream.binance.com:9443/stream"

# Berapa pair USDT yang mau discan (50 cukup ideal)
MAX_USDT_PAIRS = 1000

# Tier minimum yang dikirim: "A+", "A", atau "B"
MIN_TIER_TO_SEND = "A"  # default: kirim Tier A & A+ saja

# Cooldown sinyal per pair (dalam detik)
SIGNAL_COOLDOWN_SECONDS = 1800  # 600 detik = 10 menit
