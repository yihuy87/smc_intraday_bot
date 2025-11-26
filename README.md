# SMC Intraday Bot

Bot Telegram untuk sinyal trading **SMC–ICT intraday (LONG only)** yang otomatis scan semua pair USDT di Binance dan mengirim sinyal ke Telegram.

- Timeframe analisa: **1H / 15m / 5m**
- Mode scoring SMC Balanced (score 0–150 → Tier B/A/A+)
- FREE user: **maks 2 sinyal per hari**
- VIP user: **unlimited sinyal selama masa aktif**
- Kontrol penuh lewat **panel admin di Telegram**

---

## ✨ Fitur Utama

- Scan otomatis semua pair **USDT** via WebSocket Binance.
- Deteksi:
  - Bias 1H
  - Struktur 15m
  - Sweep & CHoCH 5m
  - Discount zone (50–62 / 62–79)
  - FVG, Mitigation Block, Breaker Block
  - Liquidity target
  - Anti fake-pump + momentum filter (RSI & MACD)
- Hitung:
  - **Entry**, **SL**, **TP1/TP2/TP3**
  - SMC SCORE (0–150) → Tier **B / A / A+**
- Sistem:
  - **FREE vs VIP**
  - **Cooldown per pair**
  - **Daily limit sinyal untuk FREE user**

---

## 🧱 Struktur Project

```text
smc_intraday_bot/
├─ config.py          # konfigurasi dasar (Telegram, Binance, dll)
├─ main.py            # Telegram bot + WebSocket Binance + logic bebas
├─ smc_logic.py       # SMC detector & entry/SL/TP
├─ smc_scoring.py     # scoring & tiering sinyal
├─ requirements.txt   # dependensi Python
├─ .env.example       # contoh konfigurasi environment
├─ .gitignore
└─ README.md

```
## Setup

### 1. Buat bot Telegram

- Chat ke **@BotFather**
- `/newbot` → ambil **BOT TOKEN**

### 2. Ambil chat ID

- Chat ke **@userinfobot**
- Catat `Your user ID` → itu **TELEGRAM_CHAT_ID**

### 3. Clone / download repo ini
```

```bash
git clone ...
cd smc-intraday-bot
